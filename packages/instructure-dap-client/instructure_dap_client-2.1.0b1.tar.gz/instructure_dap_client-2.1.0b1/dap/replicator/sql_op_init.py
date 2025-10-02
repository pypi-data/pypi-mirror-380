import logging
import os
from typing import Type, Optional

import aiofiles
from pysqlsync.base import BaseContext, Explorer
from pysqlsync.data.exchange import AsyncTextReader
from strong_typing.inspection import DataclassInstance

from .. import ui
from ..api import DAPSession
from ..dap_types import SnapshotQuery, Format, Mode
from ..replicator import meta_schema
from ..replicator.sql_metatable_handler import (
    get_table_meta_record,
    initdb_insert_table_metadata,
)
from ..replicator.sql_op import (
    SqlOp,
    _TabularLabelMapping,
    fetch_schema_for_table,
    AsyncCountingIterator,
)

logger: logging.Logger = logging.getLogger(__name__)


class SqlOpInit(SqlOp):
    use_upsert: bool

    def __init__(
        self,
        conn: BaseContext,
        namespace: str,
        table_name: str,
        explorer: Explorer,
        session: Optional[DAPSession] = None,
        use_upsert: bool = False,
    ) -> None:
        super().__init__(conn, namespace, table_name, explorer, session)
        self.use_upsert = use_upsert

    async def run(self) -> None:
        if not self.session:
            raise ValueError("Internal error: session is not set")

        ui.info("Fetching schema and synchronizing with local schema")
        entity_type, schema, versioned_schema = await fetch_schema_for_table(
            self.session, self.namespace, self.table_name
        )
        await self.explorer.synchronize(modules=[meta_schema, self.namespace_module])

        logger.debug(
            f"Start operation - initialize. Namespace: {self.namespace}, table: {self.table_name}, conn: {self.conn}"
        )

        logger.debug(f"fetching meta-data about table {self.table_name}")
        record = await get_table_meta_record(self.conn, self.namespace, self.table_name)
        if record:
            raise ValueError("Table already initialized. Please run syncdb to update it.")

        logger.debug("fetching data for table from DAP API")
        table_data = await self.session.get_table_data(
            self.namespace,
            self.table_name,
            SnapshotQuery(format=Format.TSV, mode=Mode.condensed),
        )

        async with aiofiles.tempfile.TemporaryDirectory() as temp_dir:
            await self.session.download_objects(
                table_data.objects, temp_dir, decompress=True
            )
            ui.info(f"Downloaded data for table [bold]{self.table_name}[/bold]")
            await self.init_insert_data_from_files_to_db(
                self.conn, entity_type, temp_dir
            )
            await initdb_insert_table_metadata(
                self.conn,
                self.namespace,
                table_data,
                schema,
                self.table_name,
                versioned_schema,
            )

    async def init_insert_data_from_files_to_db(
        self,
        conn: BaseContext,
        entity_type: Type[DataclassInstance],
        temp_dir: str,
    ) -> None:
        logger.debug(
            "init: insert data from resources saved to disk into database table"
        )

        mapping = SqlOpInit._get_init_tabular_mapping(entity_type)

        file_names = []
        for filename in os.listdir(temp_dir):
            if filename.endswith(".tsv"):
                file_names.append(filename)
        file_names.sort()
        total_files = len(file_names)
        total_inserted_records = 0

        with ui.JobProgress("Inserting data from files into database table...",
                            total_steps=total_files) as progress:
            for index, filename in enumerate(file_names):
                logger.debug(f"processing file {index+1} of {total_files}")

                filepath = os.path.join(temp_dir, filename)

                async with aiofiles.open(filepath, mode="rb") as f:
                    reader = AsyncTextReader(f, mapping.labels_to_types)
                    await reader.read_header()
                    columns, field_types = reader.columns, reader.field_types
                    records = reader.records()

                    logger.debug(f"insert/update data from {filepath} into database table")
                    table = conn.get_table(entity_type)

                    records_with_counter = AsyncCountingIterator(records)
                    operation = conn.upsert_rows if self.use_upsert else conn.insert_rows
                    await operation(
                        table,
                        field_names=tuple(
                            mapping.labels_to_fields[c] for c in columns
                        ),
                        field_types=field_types,
                        records=records_with_counter,
                    )
                    total_inserted_records += records_with_counter.count
                progress.update(advance=1)
        if total_inserted_records > 0:
            total_inserted_str = f"inserted [bold]{total_inserted_records}[/bold] records"
        else:
            total_inserted_str = "no records inserted"
        ui.info(f"Data import completed successfully, {total_inserted_str}")
        logger.info(f"Inserted {total_inserted_records} records into table")

    @staticmethod
    def _get_init_tabular_mapping(
        entity_type: type[DataclassInstance],
    ) -> _TabularLabelMapping:
        mapping = _TabularLabelMapping(
            labels_to_types={"meta.ts": type(None)},
            labels_to_fields={"meta.ts": ""},
        )
        return SqlOp.get_tabular_mapping(entity_type, mapping)

