# Copyright (c) 2025, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

import cudf
import rmm.mr
from rapidsmpf.buffer.buffer import MemoryType
from rapidsmpf.buffer.resource import BufferResource, LimitAvailableMemory
from rapidsmpf.shuffler import partition_and_pack, unpack_and_concat
from rapidsmpf.statistics import Statistics
from rapidsmpf.utils.cudf import cudf_to_pylibcudf_table, pylibcudf_to_cudf_dataframe
from rapidsmpf.utils.ray_utils import BaseShufflingActor

from nemo_curator.stages.deduplication.gpu_utils import align_down_to_256, get_device_free_memory

if TYPE_CHECKING:
    from collections.abc import Iterator

    import pylibcudf as plc
    from rapidsmpf.shuffler import Shuffler


class BulkRapidsMPFShuffler(BaseShufflingActor):
    """
    Class that performs a bulk shuffle operation.
    This class is compatible with Ray Actors communicating with each other using UCXX communication.
    Parameters
    ----------
    nranks
        Number of ranks in the communication group.
    total_nparts
        Total number of output partitions.
    shuffle_on
        List of column names to shuffle on.
    output_path
        Path to write output files.
    rmm_pool_size
        Size of the RMM GPU memory pool in bytes.
        If "auto", the memory pool is set to 90% of the free GPU memory.
        If None, the memory pool is set to 50% of the free GPU memory that can expand if needed.
    spill_memory_limit
        Device memory limit in bytes for spilling to host.
        If "auto", the limit is set to 80% of the RMM pool size.
        If None spilling is disabled.
    enable_statistics
        Whether to collect shuffle statistics.
    read_kwargs
        Keyword arguments for cudf.read_parquet method.
    write_kwargs
        Keyword arguments for cudf.to_parquet method.
    """

    def __init__(  # noqa: PLR0913
        self,
        nranks: int,
        total_nparts: int,
        shuffle_on: list[str],
        output_path: str = "./",
        rmm_pool_size: int | Literal["auto"] | None = "auto",
        spill_memory_limit: int | Literal["auto"] | None = "auto",
        *,
        enable_statistics: bool = False,
        read_kwargs: dict[str, Any] | None = None,
        write_kwargs: dict[str, Any] | None = None,
    ):
        super().__init__(nranks)
        self.shuffle_on = shuffle_on
        self.output_path = output_path
        self.total_nparts = total_nparts

        if isinstance(rmm_pool_size, int):
            self.rmm_pool_size = align_down_to_256(rmm_pool_size)
        elif rmm_pool_size == "auto":
            free_memory = get_device_free_memory()
            self.rmm_pool_size = align_down_to_256(int(free_memory * 0.9)) if free_memory is not None else None
        elif rmm_pool_size is None:
            self.rmm_pool_size = None
        else:
            err_msg = f"Invalid rmm_pool_size: {rmm_pool_size}"
            raise ValueError(err_msg)
        if isinstance(spill_memory_limit, int):
            self.spill_memory_limit = align_down_to_256(spill_memory_limit)
        elif spill_memory_limit == "auto":
            self.spill_memory_limit = (
                align_down_to_256(int(0.8 * self.rmm_pool_size)) if self.rmm_pool_size is not None else None
            )
        elif spill_memory_limit is None:
            self.spill_memory_limit = None
        else:
            err_msg = f"Invalid spill_memory_limit: {spill_memory_limit}"
            raise ValueError(err_msg)

        self.enable_statistics = enable_statistics
        self.read_kwargs = read_kwargs if read_kwargs is not None else {}
        self.write_kwargs = write_kwargs if write_kwargs is not None else {}

    def setup_worker(self, root_address_bytes: bytes) -> None:
        """
        Setup the UCXX communication and a shuffle operation.

        Parameters
        ----------
        root_address_bytes
            Address of the root worker for UCXX initialization.
        """
        super().setup_worker(root_address_bytes)

        # Initialize the RMM memory resource
        mr = rmm.mr.StatisticsResourceAdaptor(
            rmm.mr.PoolMemoryResource(
                rmm.mr.CudaMemoryResource(),
                initial_pool_size=self.rmm_pool_size,
                maximum_pool_size=None,
            )
        )
        rmm.mr.set_current_device_resource(mr)
        # Create a buffer resource that limits device memory if spill_memory_limit is set
        memory_available = (
            None
            if self.spill_memory_limit is None
            else {MemoryType.DEVICE: LimitAvailableMemory(mr, limit=self.spill_memory_limit)}
        )
        br = BufferResource(mr, memory_available)
        # Create a statistics object
        self.stats = Statistics(self.enable_statistics)
        # Create a shuffler
        self.shuffler: Shuffler = self.create_shuffler(
            0,
            total_num_partitions=self.total_nparts,
            buffer_resource=br,
            statistics=self.stats,
        )

    def cleanup(self) -> None:
        """Cleanup the UCXX communication and the shuffle operation."""
        if self.enable_statistics and self.stats is not None:
            self.comm.logger.info(self.stats.report())
        if self.shuffler is not None:
            self.shuffler.shutdown()

    def read_batch(self, paths: list[str]) -> tuple[cudf.DataFrame | None, list[str]]:
        """
        Read a single batch of Parquet files using cuDF.

        Parameters
        ----------
        paths
            List of file paths to the Parquet files.

        Returns
        -------
            A tuple containing the DataFrame (or None if empty) and the column names.
        """
        df = cudf.read_parquet(paths, **self.read_kwargs)
        column_names = list(df.columns)
        return (df, column_names)

    def write_table(
        self,
        table: plc.Table,
        output_path: str,
        partition_id: int | str,
        column_names: list[str],
    ) -> str:
        """
        Write a pylibcudf Table to a Parquet file using cuDF.

        Parameters
        ----------
        table
            The table to write.
        output_path
            The path to write the table to.
        partition_id
            Partition id used for naming the output file.
        column_names
            The column names of the table.
        """
        path = f"{output_path}/part.{partition_id}.parquet"
        write_kwargs = self.write_kwargs.copy()
        write_kwargs["index"] = write_kwargs.get("index", False)
        pylibcudf_to_cudf_dataframe(
            table,
            column_names=column_names,
        ).to_parquet(path, **write_kwargs)
        return path

    def insert_chunk(self, table: plc.Table | cudf.DataFrame, column_names: list[str]) -> None:
        """
        Insert a pylibcudf Table or cuDF DataFrame into the shuffler.

        Parameters
        ----------
        table
            The table or DataFrame to insert.
        column_names
            The column names of the table.
        """
        from rmm.pylibrmm.stream import DEFAULT_STREAM

        if isinstance(table, cudf.DataFrame):
            table = cudf_to_pylibcudf_table(table)
        columns_to_hash = tuple(column_names.index(val) for val in self.shuffle_on)
        packed_inputs = partition_and_pack(
            table,
            columns_to_hash=columns_to_hash,
            num_partitions=self.total_nparts,
            stream=DEFAULT_STREAM,
            device_mr=rmm.mr.get_current_device_resource(),
        )
        self.shuffler.insert_chunks(packed_inputs)

    def read_and_insert(self, paths: list[str], batchsize: int | None = None) -> list[str]:
        """
        Read the list of parquet files every batchsize and insert the partitions into the shuffler.

        Parameters
        ----------
        paths
            List of file paths to the Parquet files.
        batchsize
            Number of files to read in each batch.

        Returns
        -------
            The column names of the table.
        """
        column_names = None
        if batchsize is None:
            batchsize = len(paths)
        for i in range(0, len(paths), batchsize):
            df, batch_column_names = self.read_batch(paths[i : i + batchsize])
            if not column_names:
                column_names = batch_column_names
            self.insert_chunk(df, column_names)
        return column_names

    def insert_finished(self) -> None:
        """Tell the shuffler that we are done inserting data."""
        for pid in range(self.total_nparts):
            self.shuffler.insert_finished(pid)
        self.comm.logger.info("Insert finished")

    def extract(self) -> Iterator[tuple[int, plc.Table]]:
        """
        Extract shuffled partitions as they become ready.

        Returns
        -------
            An iterator over the shuffled partitions.
        """
        from rmm.pylibrmm.stream import DEFAULT_STREAM

        while not self.shuffler.finished():
            partition_id = self.shuffler.wait_any()
            packed_chunks = self.shuffler.extract(partition_id)
            partition = unpack_and_concat(
                packed_chunks,
                stream=DEFAULT_STREAM,
                device_mr=rmm.mr.get_current_device_resource(),
            )
            yield partition_id, partition

    def extract_and_write(self, column_names: list[str]) -> list[tuple[int, str]]:
        """
        Extract and write shuffled partitions.

        Parameters
        ----------
        column_names
            The column names of the table.
        """
        partition_paths = []
        for partition_id, partition in self.extract():
            path = self.write_table(partition, self.output_path, partition_id, column_names)
            partition_paths.append((partition_id, path))
        return partition_paths
