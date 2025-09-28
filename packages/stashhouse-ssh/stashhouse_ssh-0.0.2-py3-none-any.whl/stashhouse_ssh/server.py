"""
SSH-based file transfer protocol implementations.

Implementation of a Secure Copy Protocol (SCP) and
Secure File Transfer Protocol (SFTP) server.
"""

import asyncio
import functools
import logging
import multiprocessing
import os
import uuid
from typing import TYPE_CHECKING

import asyncssh
import asyncssh.misc

if TYPE_CHECKING:
    from stashhouse import server

logger = logging.getLogger(__name__)


class _SSHServer(asyncssh.SSHServer):
    """
    Secure Shell (SSH) server without authentication.
    """

    def connection_made(self, conn) -> None:
        remote_host, remote_port = conn.get_extra_info("peername")
        logger.info("Connection received from %s:%s", remote_host, remote_port)

    # noinspection PyUnusedLocal
    def begin_auth(self, username: str) -> bool:
        """
        The client has requested authentication.

        Indicates that authentication is never required for any client.

        Args:
            username: Name of the user being authenticated.

        Returns:
            A `bool` indicating whether authentication is required.
        """

        del username
        return False


class _SFTPServer(asyncssh.SFTPServer):
    """
    Secure File Transfer Protocol (SFTP) automatically creating directories.

    SFTP typically requires that directories are already created before
    placing files into them. This SFTP server implementation automatically
    creates parent directories without requiring additional client interaction.
    """

    def __init__(self, chan, directory: str):
        """
        Initializes the SFTP server.

        Args:
            chan: SSH server channel.
            directory: Directory to store files in.
        """
        self.directory = os.path.join(directory, str(uuid.uuid4()))
        super().__init__(chan, chroot=self.directory.encode())

    def open(
        self, path: bytes, pflags: int, attrs: asyncssh.SFTPAttrs
    ) -> asyncssh.misc.MaybeAwait[object]:
        """
        Open a file to serve a remote client.

        Args:
            path: Name of the fil to open.
            pflags: Access mode of the file to open.
            attrs: SFTP attributes.

        Returns:
            An object to access the file.

        Raises:
            asyncssh.sftp.SFTPError to return an error to the client.
        """

        writing = (
            (pflags & os.O_WRONLY) or (pflags & os.O_RDWR) or (pflags & os.O_APPEND)
        )
        creating = (pflags & os.O_CREAT) != 0

        if writing or creating:
            logger.debug("Received write request: %s", path)

            mapped_path = self.map_path(path)
            if os.path.exists(mapped_path):
                return super().open(path, pflags, attrs)

            os.makedirs(os.path.dirname(mapped_path), exist_ok=True)

        return super().open(path, pflags, attrs)


# pylint: disable=too-few-public-methods
class SSHServer:
    """
    Plugin to accept files over SSH-based protocols without authentication.

    Attributes:
        server_options: Server options applied globally.
        exited: Whether shutdown should be performed.
        port: Port to listen on.
        host_key: SSH host key.
    """

    # pylint: disable=too-many-arguments,too-many-positional-arguments
    def __init__(
        self,
        server_options: "server.ServerOptions",
        exited: multiprocessing.Event,
        port: int = 22,
        host_key_file: str | None = None,
        save_host_key: bool = True,
    ):
        """
        Initialize the SSH server.

        Args:
            server_options: Server options applied globally.
            exited: Whether shutdown should be performed.
            port: Port to listen on.
            host_key_file: File path to load the host key from.
            save_host_key: If the host key file does not exist, whether to save one.
        """

        self.server_options = server_options
        self.exited = exited
        self.port = port

        if host_key_file:
            self.host_key = host_key_file
            self._check_host_key(save_host_key)
        else:
            self.host_key = asyncssh.generate_private_key("ssh-rsa")

    def _check_host_key(self, save_host_key: bool = True) -> None:
        """
        Check if the host key is valid and generate one if needed

        If a host key file path is set but the file does not exist,
        generates a new SSH-RSA key and saves it at the specified path

        :param save_host_key: Whether to save the host key to the specified file
        """
        if isinstance(self.host_key, str) and not os.path.isfile(self.host_key):
            if not save_host_key:
                raise RuntimeError(
                    f"The specified host key file does not exist, "
                    f"but host key saving is disabled: {self.host_key}"
                )

            asyncssh.generate_private_key("ssh-rsa").write_private_key(self.host_key)

    async def _run(self) -> None:
        """
        Starts the SSH server.

        Every second, the `exited` attribute is checked
        to determine whether the server should stop.
        """

        ssh_server = await asyncssh.listen(
            self.server_options.host,
            self.port,
            allow_scp=True,
            server_host_keys=[self.host_key],
            server_factory=_SSHServer,
            sftp_factory=functools.partial(
                _SFTPServer, directory=self.server_options.directory
            ),
        )

        for address, port in ssh_server.get_addresses():
            logger.info("Started SSH server on %s:%d", address, port)

        while not self.exited.is_set():
            await asyncio.sleep(1.0)

        logger.info("Stopping server")
        ssh_server.close()
        await ssh_server.wait_closed()

    def run(self) -> None:
        """
        Executes the SSH server using asyncio.
        """

        asyncio.run(self._run())


__all__ = ("SSHServer",)
