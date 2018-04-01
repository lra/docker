"""http-daemon-with-db

Runs a python http daemon trying to connect to the database defined by the
DB_URL env var.

Usage:
  main.py (-h | --help)
  main.py --env
  main.py

Options:
  -h --help     Show this screen.
  --env         Show environment variables.

"""

import os
import sys
import docopt
from http.server import BaseHTTPRequestHandler, HTTPServer
from docopt import docopt


class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("hi!\n", "utf8"))


def run_httpd():
    httpd = HTTPServer(('', 8000), SimpleServer)
    print('Starting httpd...')
    httpd.serve_forever()


if __name__ == '__main__':
    arguments = docopt(__doc__)

    if arguments['--env']:
        print(os.environ)
        sys.exit()

    run_httpd()
