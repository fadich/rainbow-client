import time
import socket


class Socket:

    def __init__(self, host: str, port: int,
                 idle_time: float = 1.0, buffsize: int = 1024):
        self._last_message = 0
        self._connection = None
        self._idle_time = idle_time
        self._buffsize = buffsize

        self._host = host
        self._port = port

        # Create UDP-socket
        self._sock = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_DGRAM,
            proto=socket.IPPROTO_UDP)

        if self._host:
            self._sock.bind((self._host, self._port))

    @property
    def idle_time(self):
        return self._idle_time

    @property
    def buffsize(self):
        return self._buffsize

    @property
    def is_online(self):
        return time.time() - self._last_message <= self.idle_time

    def broadcast(self, msg: bytes):
        self._sock.sendto(msg, ('', self._port))

    def read_data(self):
        while True:
            data, connection = self._sock.recvfrom(self.buffsize)

            if self.is_online and self._connection != connection:
                continue

            self._connection = connection
            self._last_message = time.time()

            yield data

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.read_data())


if __name__ == '__main__':
    sock = Socket('127.0.0.1', 5005)
    for msg in sock:
        print(msg)
