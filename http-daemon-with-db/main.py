"""http-daemon-with-db

Runs a python http daemon trying to connect to the database defined by the
DATABASE_URL env var.

Usage:
  main.py
  main.py dump-env-vars
  main.py no-daemon
  main.py (-h | --help)

Options:
  -h --help     Show this screen.

"""

import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from docopt import docopt
from sqlalchemy import create_engine
import datetime


class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(bytes("hi!\n", "utf8"))
        if test_database_connection(os.environ['DATABASE_URL']):
            self.wfile.write(bytes("Connection successful!\n", "utf8"))
        else:
            self.wfile.write(bytes("Connection failed =(\n", "utf8"))
        self.wfile.write(bytes("Bye.\n", "utf8"))


def test_database_connection(conn):
    """
    conn (unicode): Database URL.
    See http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls
    """
    engine = create_engine(conn)
    connection = engine.connect()
    result = connection.execute("SELECT NOW()")
    row = result.fetchone()
    dt = row[0]
    connection.close()

    return isinstance(dt, datetime.datetime)


def run_httpd():
    httpd = HTTPServer(('', 8000), SimpleServer)
    print('Starting httpd...')
    httpd.serve_forever()


if __name__ == '__main__':
    arguments = docopt(__doc__)

    if arguments['--env']:
        print(os.environ)
        sys.exit()

    if 'DATABASE_URL' not in os.environ:
        sys.exit('Error: Undefined DATABASE_URL env var.')

    if arguments['--no-daemon']:
        if test_database_connection(os.environ['DATABASE_URL']):
            print("Connection successful!")
            sys.exit()
        else:
            sys.exit("Connection failed =(")

    run_httpd()
