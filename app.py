import os
import time
import socket
import tkinter as tk

from threading import Thread, Event
from logging import getLogger, DEBUG, basicConfig, ERROR


def read_color(canvas: tk.Canvas, break_event: Event):
    """Read the color from socket

        :param canvas:
        :param break_event:
        :return:
        """

    # Create UDP-socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.bind(('192.168.0.101', 5005))

    while not break_event.is_set():
        color, connection = sock.recvfrom(1024)
        canvas.config(bg=color)


logger = getLogger('MAIN')
basicConfig(level=DEBUG if os.environ.get('DEBUG', 0) else ERROR)

root = tk.Tk()
root.wm_attributes('-topmost', 1)
# root.wm_attributes('-disabled', True)
# root.resizable(0, 0)
root.geometry('260x160')
root.geometry('+0+0')
root.title('Rainbow')
# root.protocol('WM_DELETE_WINDOW', lambda: 0)

cv = tk.Canvas(name='img')
cv.config(bg='#000000')
cv.pack(side='top', fill='both', expand='yes')

event = Event()
thread = Thread(target=read_color, daemon=True, args=(cv, event,))
thread.start()

try:
    print('Press [Ctrl+C] to exit...')
    root.mainloop()
except KeyboardInterrupt:
    pass
finally:
    logger.info('Closing...')
    event.set()
    logger.info('Event is set...')
    thread.join()
    logger.info('Thread {} joined'.format(thread.name))
