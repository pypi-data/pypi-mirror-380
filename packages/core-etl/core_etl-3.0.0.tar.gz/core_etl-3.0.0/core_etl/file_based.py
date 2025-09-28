# -*- coding: utf-8 -*-

"""
Base class for an ETL task that need to do something with a
file retrieved from a source. Like copy the file
from sFTP to S3...

Structure & Design:
  - Extends IBaseETL for file-based ETL operations
  - Implements the abstract _execute() method with file processing logic
  - Uses iterator pattern for handling multiple files

Key Features:

  1. File Processing Pipeline:
    - Iterates through file paths from get_paths()
    - Processes each file individually with error isolation
    - Tracks processed file count
    - Handles success/error callbacks per file
  2. Abstract Interface:
    - get_paths() must be implemented by subclasses
    - process_file() must be implemented by subclasses
    - Returns iterator of file paths to process
    - Supports last_processed parameter for incremental processing
  3. Lifecycle Hooks:
    - process_file(): Core file processing logic (required implementation)
    - on_success(): Success callback for cleanup/archiving
    - on_error(): Error callback for error handling

Error Handling:
  - Individual file errors don't stop the entire batch
  - Errors are logged with file path context
  - Failed files are tracked via on_error() callback
"""

from abc import ABC, abstractmethod
from typing import Any, Iterator

from .base import IBaseETL


class IBaseEtlFromFile(IBaseETL, ABC):
    """
    Base class for an ETL task that need to do something with a
    file retrieved from a source. Like copy the file
    from sFTP to S3...
    """

    def _execute(self, *args, **kwargs) -> int:
        """
        Executes file processing workflow for all files from the source.

        Workflow:
        1. Retrieves file paths via get_paths() iterator
        2. For each file path:
           - Logs processing start
           - Calls process_file() with the path
           - Calls on_success() callback if processing succeeds
           - Calls on_error() callback if processing fails
           - Increments processed count only on success
        3. Returns total number of successfully processed files

        Individual file errors do not stop the batch processing.

        :param args: Positional arguments passed to get_paths() and process_file()
        :param kwargs: Keyword arguments passed to get_paths() and process_file()
        :return: Number of files successfully processed
        """

        processed_files = 0

        for path in self.get_paths():
            try:
                self.info(f"Processing file in path: {path}...")
                self.process_file(path, *args, **kwargs)
                self.on_success(path)

                self.info("Processed!")
                processed_files += 1

            except Exception as error:
                self.error(f"Error processing the file: {path}. Error: {error}")
                self.on_error(path)

        return processed_files

    @abstractmethod
    def get_paths(self, *args, last_processed: Any = None, **kwargs) -> Iterator[str]:
        """
        Retrieves file paths from the source and returns an iterator.

        This method must be implemented by subclasses to define how files
        are discovered and listed from the source system (e.g., SFTP, local
        filesystem, cloud storage, etc.).

        :param args: Additional positional arguments for file discovery
        :param last_processed: Optional marker for incremental processing,
                              can be used to resume from a specific point
        :param kwargs: Additional keyword arguments for file discovery
        :return: Iterator yielding file paths as strings
        """

    @abstractmethod
    def process_file(self, path: str, *args, **kwargs):
        """
        Processes a single file from the given path.

        This method must be implemented by subclasses to define the core
        file processing logic. Common implementations include:
            - Copying/moving files between systems (SFTP → S3).
            - Transforming file formats (CSV → JSON).
            - Validating and processing file contents.
            - Uploading files to cloud storage.

        :param path: File path to process.
        :param args: Additional positional arguments from `_execute()`.
        :param kwargs: Additional keyword arguments from `_execute()`.
        :raises: Should raise exceptions on processing failures.
        """

    def on_success(self, path: str, **kwargs):
        """
        Called after a file is successfully processed.

        Override this method to implement post-processing actions such as:
        - Archiving processed files
        - Moving files to a "completed" directory
        - Updating processing logs or databases
        - Sending notifications

        :param path: Path of the successfully processed file.
        :param kwargs: Additional keyword arguments for extensibility.
        """

    def on_error(self, path: str, **kwargs):
        """
        Called when an error occurs during file processing.

        Override this method to implement error handling actions such as:
            - Moving failed files to an "error" directory
            - Logging detailed error information
            - Sending error notifications
            - Quarantining problematic files

        :param path: Path of the file that failed processing.
        :param kwargs: Additional keyword arguments for extensibility.
        """
