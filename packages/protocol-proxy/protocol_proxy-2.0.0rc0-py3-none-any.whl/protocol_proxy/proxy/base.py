import abc
import json
import logging

from uuid import UUID

from ..ipc import IPCConnector, ProtocolProxyMessage, ProtocolProxyPeer, SocketParams

_log = logging.getLogger(__name__)


# noinspection PyMissingConstructor
class ProtocolProxy(IPCConnector):
    def __init__(self, *, manager_address: str, manager_port: int, manager_id: UUID, manager_token: UUID,
                 registration_retry_delay: float = 20.0, **kwargs):
        """NOTE: Proxy implementations MUST:
            1. Subclass a multitasking subclass of IPCConnector (gevent, asyncio, etc.)
            2. Subclass this "ProtocolProxy" class.
            3. Call super first to IPCConnector parent then this ProtocolProxy parent._
            4. Create a ProtocolProxyPeer subclass for the manager and store it in self.peers.
            5. Call send_registration asynchronously in their constructor after super calls.
        """
        _log.debug('PP: IN INIT.')
        super(ProtocolProxy, self).__init__(**kwargs)
        self.registration_retry_delay: float = registration_retry_delay
        self.manager_params = SocketParams(manager_address, manager_port)
        self.manager = manager_id


    @abc.abstractmethod
    def get_local_socket_params(self) -> SocketParams:
        pass

    @classmethod
    @abc.abstractmethod
    def get_unique_remote_id(cls, unique_remote_id: tuple) -> tuple:
        """Get a unique identifier for the proxy server
         given a unique_remote_id and protocol-specific set of parameters."""
        pass

    @abc.abstractmethod
    def send_registration(self, remote: ProtocolProxyPeer) -> ProtocolProxyMessage:
        """Send a registration message to the remote manager."""

    def _get_registration_message(self):
        # _log.debug(f'{self.proxy_name}: IN GET REGISTRATION MESSAGE')
        local_address, local_port = self.get_local_socket_params()
        message = ProtocolProxyMessage(
            method_name='REGISTER_PEER',
            payload= json.dumps({'address': local_address, 'port':local_port, 'proxy_id': self.proxy_id.hex,
                                 'token': self.token.hex}).encode('utf8'),
            response_expected=True
        )
        return message
