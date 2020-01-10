import time
import socket


class Socket:

    def __init__(self, host: str, port: int,
                 idle_time: float = 1.0, buffsize: int = 1024):
        self._last_message = 0
        self._connection = None
        self._idle_time = idle_time
        self._buffsize = buffsize

        # Create UDP-socket
        self._sock = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_DGRAM,
            proto=socket.IPPROTO_UDP)
        self._sock.bind((host, port))

    @property
    def idle_time(self):
        return self._idle_time

    @property
    def buffsize(self):
        return self._buffsize

    @property
    def is_online(self):
        return time.time() - self._last_message <= self.idle_time

    def __next__(self):
        data, connection = self._sock.recvfrom(self.buffsize)

        if self.is_online and self._connection != connection:
            return

        self._connection = connection
        self._last_message = time.time()

        yield data
