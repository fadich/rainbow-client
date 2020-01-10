import os
import sys


class Console:

    def __init__(self, quiet: bool = False):
        devnull = open(os.devnull)

        if quiet:
            sys.stdin = devnull
            sys.stdout = devnull
            sys.stderr = devnull

        self._quiet = quiet
        self._stdin = sys.stdin
        self._stdout = sys.stdout
        self._stderr = sys.stderr

    @property
    def is_quiet(self):
        return self._quiet

    @property
    def stdin(self):
        return self._stdin

    @property
    def stdout(self):
        return self._stdout

    @property
    def stderr(self):
        return self._stderr

    def read(self, hint: str = None):
        if self.is_quiet:
            return None

        if hint is not None:
            self.write(hint, endline='')

        return self.stdin.readline().strip()

    def write(self, line: str = None, endline: str = '\n'):
        line = line or ''
        self.stdout.write(f'{line}{endline}')
        self.stdout.flush()

    def error(self, line: str = None, endline: str = '\n'):
        line = line or ''
        self.stderr.write(f'{line}{endline}')
        self.stderr.flush()
