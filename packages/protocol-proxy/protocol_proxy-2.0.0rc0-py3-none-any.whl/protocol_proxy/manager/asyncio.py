import asyncio
import atexit
import logging
import os
import signal

from abc import ABC
from asyncio.subprocess import Process
from uuid import uuid4
from typing import Type

from ..ipc import callback, ProtocolHeaders, ProtocolProxyPeer
from ..ipc.asyncio import AsyncioIPCConnector, AsyncioProtocolProxyPeer
from ..proxy import ProtocolProxy
from . import ProtocolProxyManager

_log = logging.getLogger(__name__)


class AsyncioProtocolProxyManager(ProtocolProxyManager, AsyncioIPCConnector, ABC):
    def __init__(self, proxy_class: Type[ProtocolProxy], **kwargs):
        super().__init__(proxy_class=proxy_class, **kwargs)

    async def wait_peer_registered(self, peer, timeout, func=None, *args, **kwargs):
        """ Waits for a peer to be ready, optionally calling a function when it is.
            If the peer does not register within the timeout, it is removed and a warning is logged.
        """
        try:
            async with peer.ready:
                await peer.ready.wait_for(lambda: peer.socket_params is not None)
                if func:
                    func(*args, **kwargs)
                peer.ready.notify_all()
        except asyncio.TimeoutError:
            _log.warning(f"Peer {peer.proxy_id} did not register within {timeout} seconds. Removing peer.")
            del self.peers[peer.proxy_id]
        except Exception as e:
            _log.error(f"Error while waiting for peer {peer.proxy_id} to be ready: {e}. Removing peer.")
            del self.peers[peer.proxy_id]

    async def get_proxy(self, unique_remote_id: tuple, **kwargs) -> ProtocolProxyPeer:
        command, proxy_id, proxy_name = self._setup_proxy_process_command(unique_remote_id, **kwargs)  # , proxy_env
        if command:
            proxy_process = await asyncio.create_subprocess_exec(*command, stdin=asyncio.subprocess.PIPE)
            # , stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
            # TODO: Implement logging along lines of AIP.start_agent() (uncomment PIPES above too).
            _log.info(f"PPM: Created new ProtocolProxy {proxy_name} with ID {str(proxy_id)}, pid: {proxy_process.pid}")
            peer_token = uuid4()
            proxy_process.stdin.write(peer_token.hex.encode())
            proxy_process.stdin.write(self.token.hex.encode())
            await proxy_process.stdin.drain()
            proxy_process.stdin.close()
            proxy_process.stdin = open(os.devnull)
            self.peers[proxy_id] = AsyncioProtocolProxyPeer(process=proxy_process, proxy_id=proxy_id, token=peer_token)
            self._setup_exit(proxy_process)
            atexit.register(self.finalize_process, proxy_process)
        return self.peers[proxy_id]

    @callback
    async def handle_peer_registration(self, headers: ProtocolHeaders, raw_message: bytes):
        proxy: AsyncioProtocolProxyPeer | None = self.peers.get(headers.sender_id)
        if not proxy:
            _log.error(f'PPM: Received registration message from unknown peer: {headers.sender_id}.')
            return False
        async with proxy.ready:
            success = super().handle_peer_registration(headers, raw_message)
            proxy.ready.notify_all()
            return success

    @staticmethod
    def _setup_exit(process: Process):
        """Set up cleanup for the proxy process on exit."""
        def cleanup_func(process):
            if process.returncode is None:
                try:
                    process.terminate()
                except ProcessLookupError:
                    pass
        asyncio.get_event_loop().add_signal_handler(signal.SIGTERM, cleanup_func, process)
        asyncio.get_event_loop().add_signal_handler(signal.SIGINT, cleanup_func, process)

    @staticmethod
    def finalize_process(process: Process):
        try:
            process.kill()
        except ProcessLookupError:
            pass
