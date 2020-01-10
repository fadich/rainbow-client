#!/usr/bin/python3

import sys
import argparse

from ui import Console


def main():
    parser = argparse.ArgumentParser(description='Rainbow client app')
    parser.add_argument('-a', '--address', '--host', dest='host', type=str, help='Rainbow host IP address')
    parser.add_argument('-p', '--port', dest='port', type=int, help='Rainbow host port')
    parser.add_argument('-d', '--debug', dest='debug', action='store_true', help='set debug log level')
    parser.add_argument('-q', '--quiet', dest='quiet', action='store_true', help='disable output')
    args = parser.parse_args()

    console = Console(quiet=args.quiet)

    if console.is_quiet:
        host = args.host or '127.0.0.1'
        port = args.port or 5005
        debug = args.debug or False
    else:
        host = args.host or console.read('Host address: ')
        port = args.host or console.read('Host port: ')

    return 0


if __name__ == '__main__':
    sys.exit(main())
