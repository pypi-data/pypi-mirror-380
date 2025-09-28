# -*- coding: utf-8 -*-

"""
Base class for record-based ETL operations that process data records/rows
from various sources like APIs, databases, files, SQS queues, etc.

Structure & Design:
  - Extends IBaseETL for record-based data processing.
  - Implements configurable transformation pipeline.
  - Processes data in memory-efficient batches.
  - Provides built-in transformations (rename, remove, type cast).

Key Features:

  1. Batch Processing Pipeline:
    - Retrieves records in configurable batches.
    - Applies transformation sequence per record.
    - Processes complete batches for efficiency.
    - Tracks total processed record count.

  2. Built-in Transformations:
    - Field removal via attrs_to_remove.
    - Field renaming via name_mapper.
    - Data type casting via type_mapper.
    - Configurable batch size for memory management.

  3. Transformation Hooks:
    - pre_transformations(): Custom logic before built-in transforms.
    - post_transformations(): Custom logic after built-in transforms.
    - Extensible pipeline for specific business logic.

  4. Abstract Interface:
    - retrieve_records(): Must implement data source integration.
    - process_records(): Must implement data destination handling.

Error Handling:
  - Individual record errors don't stop batch processing.
  - Batch-level processing with configurable sizes.
  - Memory-efficient for large datasets.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Iterator, List, Optional

from core_mixins.utils import convert_data_type
from core_mixins.utils import remove_attributes
from core_mixins.utils import rename_attributes

from .base import IBaseETL


class IBaseEtlFromRecord(IBaseETL, ABC):
    """
    Base class for an ETL task that need to do ETLs processes over data (records,
    rows) retrieved from different sources like: file, sFTP server, SQS queues, APIs
    or another data source...
    """

    def __init__(
        self,
        name_mapper: Optional[Dict[str, str]] = None,
        type_mapper: Optional[Dict[str, str]] = None,
        max_per_batch: int = 1000,
        attrs_to_remove: Optional[List[str]] = None,
        **kwargs,
    ) -> None:
        """
        Initialize record-based ETL with transformation configuration.

        :param name_mapper:
            Dictionary mapping old field names to new field names.
            Example: {"old_name": "new_name", "id": "user_id"}.

        :param type_mapper:
            Dictionary defining data type conversions for fields.
            Example: {"age": "int", "price": "float", "active": "bool"}

        :param max_per_batch:
            Maximum number of records to process in each batch.
            Controls memory usage and processing efficiency. Default: 1000.

        :param attrs_to_remove:
            List of field names to remove from each record.
            Example: ["temp_field", "internal_id", "debug_info"].

        :param kwargs: Additional keyword arguments passed to parent IBaseETL.
        """

        super().__init__(**kwargs)

        self.name_mapper = name_mapper or {}
        self.attrs_to_remove = attrs_to_remove or []
        self.type_mapper = type_mapper or {}
        self.max_per_batch = max_per_batch

    def _execute(self, *args, **kwargs) -> int:
        """
        Executes record processing workflow with configurable transformations.

        Workflow:
            1. Retrieves records in batches via retrieve_records()
            2. For each batch:
               - Logs batch processing start
               - For each record in batch:
                 a. Applies pre_transformations() (custom logic).
                 b. Removes unwanted attributes (attrs_to_remove).
                 c. Renames fields (name_mapper).
                 d. Converts data types (type_mapper).
                 e. Applies post_transformations() (custom logic).
               - Processes complete transformed batch via process_records().
            3. Returns total number of records processed across all batches.

        The transformation pipeline is applied consistently to each record,
        ensuring data consistency and quality.

        :param args: Additional positional arguments passed to `retrieve_records()`.
        :param kwargs: Additional keyword arguments passed to `retrieve_records()`.
        :return: Total number of records processed across all batches.
        """

        batch_number = 1
        count = 0

        for batch in self.retrieve_records(**kwargs):
            self.info(f"Processing batch # {batch_number}...")
            records = []

            for record in batch:
                # Apply transformations required before the base ones...
                self.pre_transformations(record)

                remove_attributes(record, self.attrs_to_remove)
                rename_attributes(record, self.name_mapper)
                convert_data_type(record, self.type_mapper)

                # Apply transformations required after the base ones...
                self.post_transformations(record)

                records.append(record)
                count += 1

            if records:
                self.process_records(records)

            batch_number += 1

        return count

    @abstractmethod
    def retrieve_records(
        self,
        last_processed: Any = None,
        start: Any = None,
        end: Any = None,
        **kwargs,
    ) -> Iterator[List[Dict]]:
        """
        Retrieves records from data sources in batches.

        This method must be implemented by subclasses to define how records
        are fetched from the source system. Returns batches of records to
        enable memory-efficient processing and prevent resource exhaustion.

        Common implementations include:
            - Database queries with pagination.
            - API calls with page-based retrieval.
            - File reading with chunk processing.
            - Message queue consumption.
            - Stream processing.

        :param last_processed:
            Marker for incremental processing, used to resume
            from a specific point (e.g., timestamp, ID, offset).

        :param start: Start boundary for data retrieval (e.g., date, ID).
        :param end: End boundary for data retrieval (e.g., date, ID).
        :param kwargs: Additional parameters for source-specific configuration.

        :return:
            Iterator yielding batches (lists) of records as
            dictionaries. Each batch should respect the
            max_per_batch configuration.
        """

    def pre_transformations(self, record: Dict) -> None:
        """
        Apply custom transformations before built-in transformations.

        Override this method to implement custom business logic that should
        be applied before the standard transformations (remove, rename, cast).
        This allows for data preparation, validation, or enrichment.

        Common use cases:
            - Data validation and cleanup.
            - Field normalization (e.g., date formatting).
            - Data enrichment from external sources.
            - Business-specific calculations.
            - Record filtering or marking.

        :param record: Record dictionary to transform (modified in-place).
        """

    def post_transformations(self, record: Dict) -> None:
        """
        Apply custom transformations after built-in transformations.

        Override this method to implement custom business logic that should
        be applied after the standard transformations (remove, rename, cast).
        This allows for final data processing before the load phase.

        Common use cases:
            - Final data validation.
            - Derived field calculations.
            - Data formatting for destination system.
            - Business rule application.
            - Data quality checks.

        :param record: Record dictionary to transform (modified in-place).
        """

    @abstractmethod
    def process_records(self, records: List[Dict], **kwargs):
        """
        Processes a batch of transformed records.

        This method must be implemented by subclasses to define what happens
        to records after all transformations have been applied. This is the
        "Load" phase of the ETL process.

        Common implementations include:
            - Storing records in databases (SQL, NoSQL).
            - Writing to files (CSV, JSON, Parquet).
            - Sending to message queues (SQS, Kafka).
            - Uploading to cloud storage (S3, Azure Blob).
            - Streaming to real-time systems (Kinesis, Pub/Sub).
            - Calling external APIs for data ingestion.

        :param records: List of transformed record dictionaries ready for processing.
        :param kwargs: Additional parameters for destination-specific configuration.
        :raises: Should raise exceptions on processing failures to trigger error handling.
        """
