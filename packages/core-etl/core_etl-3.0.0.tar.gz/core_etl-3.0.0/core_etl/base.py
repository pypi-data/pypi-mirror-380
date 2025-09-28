# -*- coding: utf-8 -*-

"""
This file defines IBaseETL, an abstract base class for ETL (Extract, Transform, Load) tasks. Here's the analysis:

Structure & Design:
  - Inherits from ITask and ABC (Abstract Base Class)
  - Follows the Template Method pattern with execute() orchestrating the ETL workflow
  - Well-documented with clear docstrings

Key Features:
  - Timezone support via time_zone parameter (defaults to UTC)
  - Temporary folder management for local file operations
  - Status tracking using TaskStatus enum
  - Error handling with proper exception capture and logging
  - Lifecycle hooks: pre_processing(), _execute(), post_processing(), clean_resources()

Workflow:
  1. Sets status to EXECUTING
  2. Runs pre-processing
  3. Executes main ETL logic (_execute() - abstract method)
  4. Runs post-processing
  5. Handles errors with logging and status updates
  6. Cleans up resources in finally block
"""

from abc import ABC, abstractmethod
from datetime import timezone
from typing import List, Dict, Optional

from core_mixins.exceptions import get_exception_data
from core_mixins.interfaces.task import ITask
from core_mixins.interfaces.task import TaskStatus


class IBaseETL(ITask, ABC):
    """
    Base class for an ETL task. A task defines the operations
    over a service or a platform from where you need to
    extract, transform and/or store information...

    This class defines some commons (maybe useful) attributes/methods for future
    implementations of the ETL tasks.
    """

    def __init__(
        self,
        time_zone: timezone = timezone.utc,
        temp_folder: Optional[str] = None,
        **kwargs,
    ) -> None:
        """
        :param time_zone: The time zone to use in the ETL for date/datetime processing.
        :param temp_folder: For task that need to store local files temporarily.
        """

        super().__init__(**kwargs)

        self.status = TaskStatus.CREATED
        self.temp_folder = temp_folder
        self.time_zone = time_zone

    def execute(self, *args, **kwargs) -> int:
        """
        Executes the ETL task following the template method pattern.

        Orchestrates the complete ETL workflow:
            1. Sets status to EXECUTING.
            2. Runs pre-processing actions.
            3. Executes main ETL logic via `_execute()`.
            4. Runs post-processing actions.
            5. Handles errors with logging and status updates.
            6. Cleans up resources.

        :param args: Positional arguments passed to lifecycle methods.
        :param kwargs: Keyword arguments passed to lifecycle methods.
        :return: Number of processed elements (0 if error or invalid return).
        """

        self.status = TaskStatus.EXECUTING
        res = 0

        try:
            self.info("Executing pre-processing actions...")
            self.pre_processing()

            self.info("Executing main flow...")
            res = self._execute(*args, **kwargs)
            if not type(res) == int:
                # Expecting number of processed elements as integer,
                # if not valid value is provided, setting
                # it as zero.
                res = 0

            self.info("Executing post-processing actions...")
            self.post_processing()

        except Exception as error:
            self.status = TaskStatus.ERROR
            type_, message, traceback = get_exception_data()
            self.error(f"{type_} -- {error}")
            self.error(traceback)

            self.save_logs(
                error_type=type_,
                error_message=message,
                error_traceback=traceback,
            )

        else:
            self.status = TaskStatus.SUCCESS
            self.save_logs(processed_elements=res)
            self.info(f"Were processed {res} elements.")
            self.info(f"Finished -> {self.name}!")

        finally:
            self.clean_resources()

        return res

    def pre_processing(self, *args, **kwargs) -> None:
        """Pre-processing actions..."""

    @abstractmethod
    def _execute(self, *args, **kwargs) -> int:
        """
        Generic implementation for all the extract, transform
        and load processes...

        :return: It returns the number of elements were processed.
        """

    def post_processing(self, *args, **kwargs) -> None:
        """Post-processing actions..."""

    def save_logs(
        self,
        processed_elements: int = 0,
        error_type: str = "",
        error_message: str = "",
        error_traceback: Optional[List[Dict]] = None,
        **kwargs,
    ) -> None:
        """
        Save executions logs/metadata if required...

        :param processed_elements: The number of processed elements.
        :param error_type: The error type if exists.
        :param error_message: The error message if exists.
        :param error_traceback: The error traceback if exists.
        """

    def clean_resources(self, *args, **kwargs) -> None:
        """In case you need to close/remove some resources"""
