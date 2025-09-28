# -*- coding: utf-8 -*-

"""
SFTP-based ETL Module
=====================

This module provides ETL base classes for processing files retrieved from SFTP servers.

Key Features:
    - Abstract base class for SFTP file processing tasks
    - Built-in SFTP connection management and authentication
    - File filtering by extension and prefix
    - Optional automatic file cleanup after processing
    - Comprehensive error handling and logging

Example:
    >>> class DataProcessor(IBaseEtlFromFtpFile):
    ...     def process_file(self, path: str, **kwargs):
    ...         # Custom file processing logic
    ...         print(f"Processing {path}")
    ...
    >>> task = DataProcessor(
    ...     host="data.server.com",
    ...     user="admin",
    ...     path="/data/csv",
    ...     file_ext=".csv",
    ...     delete_file_on_success=True
    ... )
    >>> task.execute()
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Iterator, Optional

from core_etl.file_based import IBaseEtlFromFile

from core_ftp.clients.sftp import SftpClient


class IBaseEtlFromFtpFile(IBaseEtlFromFile, ABC):
    """
    Base class for ETL tasks that process files retrieved from an SFTP server.

    This class extends IBaseEtlFromFile to provide SFTP-specific functionality,
    including connection management, file filtering, and optional cleanup.
    It handles the complete lifecycle of SFTP-based file processing.

    Features:
        - SFTP connection management with authentication support
        - File filtering by extension and prefix
        - Optional file deletion after successful processing
        - Proper resource cleanup

    Example:

        .. code-block:: python

            # Start test SFTP server
            docker run -v /home/user/Documents:/home/foo/upload \
                       -p 22:22 \
                       -d atmoz/sftp foo:pass:::upload

            class SftpTask(IBaseEtlFromFtpFile):
                @classmethod
                def registered_name(cls) -> str:
                    return "SftpTask"

                def process_file(self, path: str, *args, **kwargs):
                    # Process the file here
                    pass

            # Execute the task
            SftpTask(
                host="localhost",
                user="foo",
                password="pass",
                path="/upload",
                file_prefix="data_",
                file_ext=".csv",
                delete_file_on_success=True
            ).execute()
        ..
    """

    def __init__(
        self,
        host: str,
        port: int = 22,
        user: Optional[str] = None,
        password: Optional[str] = None,
        path: Optional[str] = None,
        file_prefix: Optional[str] = None,
        file_ext: Optional[str] = None,
        delay_in_days: int = 1,
        monthly_basis: bool = False,
        private_key_path: str = "",
        delete_file_on_success: bool = False,
        **kwargs,
    ) -> None:
        """
        Initialize the SFTP-based ETL task.

        :param host: SFTP server hostname or IP address.
        :type host: str
        :param port: SFTP server port (default: 22).
        :type port: int
        :param user: Username for SFTP authentication.
        :type user: Optional[str]
        :param password: Password for SFTP authentication.
        :type password: Optional[str]
        :param private_key_path: Path to private key file for key-based authentication.
        :type private_key_path: str
        :param path: Remote directory path to scan for files.
        :type path: Optional[str]
        :param file_prefix: Filter files by prefix (default: no filtering).
        :type file_prefix: Optional[str]
        :param file_ext: Filter files by extension (default: no filtering).
        :type file_ext: Optional[str]
        :param delay_in_days: Number of days before today to retrieve files if applicable.
        :type delay_in_days: int
        :param monthly_basis: Whether data should be collected on a monthly basis.
        :type monthly_basis: bool
        :param delete_file_on_success: If True, files will be deleted after successful processing.
        :type delete_file_on_success: bool
        :param kwargs: Additional arguments passed to the parent class.
        """

        super().__init__(**kwargs)

        self.host = host
        self.port = port

        self.user = user
        self.password = password
        self.private_key_path = private_key_path

        self.path = path
        self.delete_file_on_success = delete_file_on_success
        self.file_prefix = file_prefix
        self.file_ext = file_ext

        self.delay_in_days = delay_in_days
        self.monthly_basis = monthly_basis

        self.ftp_client = SftpClient(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            private_key_path=self.private_key_path,
            disabled_algorithms=True,
        )

    def pre_processing(self, *args, **kwargs) -> None:
        super(IBaseEtlFromFtpFile, self).pre_processing(**kwargs)
        self.ftp_client.connect()

    def get_paths(self, last_processed: Any = None, *args, **kwargs) -> Iterator[str]:
        """
        Retrieves file paths from the remote SFTP server.

        Filters files by extension and prefix if specified. Handles connection
        errors gracefully and logs them appropriately.

        :param last_processed: Last processed item (not used in this implementation).
        :type last_processed: Any
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: Iterator of filtered file names.
        :rtype: Iterator[str]
        :raises: Logs errors but doesn't re-raise to allow graceful handling.
        """

        if self.path is None:
            self.warning("No path specified for SFTP file scanning")
            return

        try:
            for file_name, attr in self.ftp_client.list_files(self.path):
                if not self.file_ext or file_name.endswith(self.file_ext):
                    if not self.file_prefix or file_name.startswith(self.file_prefix):
                        yield file_name
        
        except Exception as error:
            self.error(f"Error listing files from SFTP path '{self.path}': {error}")
            return

    def process_file(self, path: str, *args, **kwargs):
        """
        Processes a single file from the SFTP server.

        This method should be overridden by subclasses to implement
        specific file processing logic.

        :param path: Path to the remote file to process.
        :type path: str
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        """

        self.info(f"Processing remote file: {path}...")

    def on_success(self, path: str, **kwargs):
        """
        Called after successful file processing.

        Optionally deletes the processed file from the SFTP server
        if delete_file_on_success is enabled.

        :param path: Path to the successfully processed file.
        :type path: str
        :param kwargs: Additional keyword arguments.
        """

        if self.delete_file_on_success:
            try:
                self.ftp_client.delete(path)
                self.info(f'File "{path}" was deleted successfully!')
            
            except Exception as error:
                self.error(f'Failed to delete file "{path}": {error}')
                # Don't re-raise to avoid failing the entire process

    def clean_resources(self):
        """
        Cleans up SFTP connection resources.
        Safely closes the SFTP connection, handling any cleanup
        errors gracefully.
        """

        try:
            self.ftp_client.close()
            self.info("SFTP connection closed successfully")
        
        except Exception as error:
            self.warning(f"Error closing SFTP connection: {error}")
