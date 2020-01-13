import time

from socket_client import Socket


if __name__ == '__main__':
    sock = Socket('', 5005)

    _id = hash(time.time())
    print(_id)

    while True:
        sock.broadcast(f'test {_id}'.encode())
        time.sleep(0.25)
