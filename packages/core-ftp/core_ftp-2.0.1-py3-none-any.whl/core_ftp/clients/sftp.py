# -*- coding: utf-8 -*-

"""
SFTP Client Module
==================

This module provides a high-level SFTP client wrapper around Paramiko for secure file operations.

Key Features:
    - Simplified SFTP connection management
    - Comprehensive error handling with custom exceptions
    - Context manager support for automatic resource cleanup
    - Support for both password and key-based authentication
    - File upload, download, listing, and deletion operations

Example:
    >>> from core_ftp.clients.sftp import SftpClient
    >>>
    >>> with SftpClient("server.com", user="admin", password="secret") as client:
    ...     files = list(client.list_files("/data"))
    ...     client.download_file("remote.txt", "local.txt")
"""

try:
    from typing import Self

except ImportError:
    # For earlier versions...
    from typing_extensions import Self

from typing import (
    Any,
    Callable,
    cast,
    Dict,
    IO,
    Iterator,
    List,
    Optional,
    Tuple,
)

from paramiko import Transport, RSAKey
from paramiko.sftp_attr import SFTPAttributes
from paramiko.sftp_client import SFTPClient
from paramiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import BadHostKeyException
from paramiko.ssh_exception import NoValidConnectionsError
from paramiko.ssh_exception import SSHException


class SftpClient:
    """
    It provides a wrapper for an SFTP connection...

    .. code-block:: python

        client = SftpClient("test.rebex.net", "demo", "password")
        client.connect()

        for x in client.list_files("/"):
            print(x)

        client.close()

        with SftpClient("test.rebex.net", "demo", "password") as _client:
            _client.download_file("readme.txt", "/tmp/readme.txt")
    ..
    """

    def __init__(
        self,
        host: str,
        port: int = 22,
        user: Optional[str] = None,
        password: Optional[str] = None,
        private_key_path: str = "",
        passphrase: Optional[str] = None,
        transport_kwargs: Optional[Dict[str, Any]] = None,
        connection_kwargs: Optional[Dict[str, Any]] = None,
        disabled_algorithms: bool = False,
        algorithms_to_disable: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize SFTP client with connection parameters.

        :param host: Host or IP of the remote machine.
        :param port: Port number for SSH connection (default: 22).
        :param user: Username at the remote machine.
        :param password: Password at the remote machine.
        :param private_key_path: Path to private key file.
        :param passphrase: Passphrase to use along the private key.
        :param transport_kwargs: Named arguments for transport.
        :param connection_kwargs: Named arguments for connection.
        :param disabled_algorithms: If true, a list of algorithms will be disabled.
        :param algorithms_to_disable: Algorithms to disable.
        """

        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.private_key_path = private_key_path
        self.passphrase = passphrase

        self.connection_kwargs = connection_kwargs or {}
        self.transport_kwargs = transport_kwargs or {}
        self._sftp_client: Optional[SFTPClient] = None
        self._transport: Optional[Transport] = None

        # It's a bug in Paramiko. It does not handle correctly absence
        # of server-sig-algs extension on the server side...
        # https://stackoverflow.com/questions/70565357/paramiko-authentication-fails-with-agreed-upon-rsa-sha2-512-pubkey-algorithm
        if disabled_algorithms:
            self.transport_kwargs["disabled_algorithms"] = {
                "pubkeys": algorithms_to_disable or ["rsa-sha2-512", "rsa-sha2-256"]
            }

    @property
    def client(self) -> SFTPClient:
        """
        Provides access to the underlying Paramiko SFTP client.
        Auto-connects if not already connected.

        :return: The underlying `SFTPClient` instance.
        :rtype: `SFTPClient`.
        :raises SftpClientError: If connection fails.
        """

        if self._sftp_client is None:
            self.connect()

        return cast(SFTPClient, self._sftp_client)

    def _ensure_transport(self) -> Transport:
        """
        Ensures transport connection exists, creating it if necessary.

        :return: The transport instance.
        :rtype: `Transport`.
        """

        if self._transport is None:
            self._transport = Transport(
                (self.host, self.port),
                **self.transport_kwargs,
            )

        return self._transport

    def __enter__(self) -> Self:
        """
        Context manager entry point.

        :return: The SFTP client instance.
        :rtype: Self
        """

        self.connect()
        return self

    def connect(self) -> Self:
        """
        Establishes SFTP connection to the remote server.

        :return: The SFTP client instance for method chaining.
        :rtype: Self

        :raises SftpClientError:
            If connection fails due to authentication,
            host key, SSH, or other errors.
        """

        data: Dict[str, Any] = {
            "username": self.user,
            "password": self.password,
        }

        try:
            if self.private_key_path:
                data["pkey"] = RSAKey.from_private_key_file(
                    self.private_key_path,
                    self.passphrase,
                )

            _transport = self._ensure_transport()
            _transport.connect(**data, **self.connection_kwargs)
            self._sftp_client = SFTPClient.from_transport(_transport)
            return self

        except AuthenticationException as error:
            raise SftpClientError(f"Authentication error: {error}.")

        except BadHostKeyException as error:
            raise SftpClientError(f"HostKeys error: {error}.")

        except SSHException as error:
            raise SftpClientError(f"SSH error: {error}.")

        except NoValidConnectionsError as error:
            raise SftpClientError(f"Connection error: {error}")

        except Exception as error:
            raise SftpClientError(f"Error: {error}.")

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """
        Context manager exit point.

        :param exc_type: Exception type.
        :param exc_val: Exception value.
        :param exc_tb: Exception traceback.
        """

        self.close()

    def close(self) -> None:
        """
        Closes the SFTP connection and transport.
        Safe to call multiple times or on unopened connections.
        """

        if self._sftp_client is not None:
            self._sftp_client.close()

        if self._transport is not None:
            self._transport.close()

    def get_cwd(self) -> Optional[str]:
        """
        Returns the current working directory on the remote server.

        :return: Current working directory path, or None if not set.
        :rtype: Optional[str]
        :raises SftpClientError: If unable to get current directory.
        """

        try:
            return self.client.getcwd()

        except IOError as error:
            raise SftpClientError(f"Error getting current directory: {error}")

    def chdir(self, remote_path: str) -> None:
        """
        Changes the current working directory on the remote server.

        :param remote_path: Path to change to.
        :type remote_path: str
        :raises SftpClientError: If unable to change directory.
        """

        try:
            self.client.chdir(remote_path)

        except IOError as error:
            raise SftpClientError(f"Error changing directory: {error}")

    def list_files(self, remote_path: str) -> Iterator[Tuple[str, SFTPAttributes]]:
        """
        Read files under a remote directory.

        :param remote_path: Remote directory path.
        :return: Iterator of tuples in the form ("file_name", SFTPAttributes)
        """

        try:
            for attr in self.client.listdir_attr(remote_path):
                yield attr.filename, attr

        except IOError as error:
            raise SftpClientError(f"Error accessing directory: {error}")

    def download_file(self, remote_file_path: str, local_file_path: str) -> str:
        """
        Downloads a file from the remote server to local filesystem.

        :param remote_file_path: Path to the remote file.
        :type remote_file_path: str
        :param local_file_path: Local path where file will be saved.
        :type local_file_path: str
        :return: The local file path where file was saved.
        :rtype: str
        :raises SftpClientError: If download fails.
        """

        try:
            self.client.get(remote_file_path, local_file_path)
            return local_file_path

        except IOError as error:
            raise SftpClientError(f"Error downloading file: {error}")

    def upload_file(
        self,
        file_path: str,
        remote_path: str,
        callback: Optional[Callable[[int, int], Any]] = None,
        confirm: bool = False,
    ) -> SFTPAttributes:
        """
        Uploads a local file to the remote server.

        :param file_path: Local path to the file to upload.
        :type file_path: str
        :param remote_path: Remote path where file will be stored.
        :type remote_path: str
        :param callback: Optional callback for progress monitoring.
        :type callback: Optional[Callable[[int, int], Any]]
        :param confirm: Whether to confirm the upload.
        :type confirm: bool
        :return: File attributes of the uploaded file.
        :rtype: SFTPAttributes
        :raises SftpClientError: If upload fails.
        """

        try:
            return self.client.put(
                file_path,
                remotepath=remote_path,
                callback=callback,
                confirm=confirm,
            )

        except IOError as error:
            raise SftpClientError(f"Error uploading file: {error}")

    def upload_object(
        self,
        file_like: IO[Any],
        remote_path: str,
        file_size: int = 0,
        callback: Optional[Callable[[int, int], Any]] = None,
        confirm: bool = False,
    ) -> SFTPAttributes:
        """
        Uploads a file-like object to the remote server.

        :param file_like: File-like object to upload.
        :type file_like: IO[Any]
        :param remote_path: Remote path where object will be stored.
        :type remote_path: str
        :param file_size: Size of the file-like object (default: 0).
        :type file_size: int
        :param callback: Optional callback for progress monitoring.
        :type callback: Optional[Callable[[int, int], Any]]
        :param confirm: Whether to confirm the upload.
        :type confirm: bool
        :return: File attributes of the uploaded object.
        :rtype: SFTPAttributes
        :raises SftpClientError: If upload fails.
        """

        try:
            return self.client.putfo(
                file_like,
                remote_path,
                file_size=file_size,
                callback=callback,
                confirm=confirm,
            )

        except IOError as error:
            raise SftpClientError(f"Error uploading object: {error}")

    def delete(self, remote_path: str, is_folder: bool = False) -> None:
        """
        Deletes a file or directory on the remote server.

        :param remote_path: Path to the remote file or directory.
        :type remote_path: str
        :param is_folder: Whether the target is a folder (default: False).
        :type is_folder: bool
        :raises SftpClientError: If deletion fails.
        """

        try:
            if is_folder:
                self.client.rmdir(remote_path)

            else:
                self.client.remove(remote_path)

        except IOError as error:
            raise SftpClientError(f"Error deleting {'directory' if is_folder else 'file'}: {error}")


class SftpClientError(Exception):
    """
    Custom exception for SFTP operations.

    Raised when SFTP operations fail due to connection issues,
    authentication failures, or file system errors.
    """
