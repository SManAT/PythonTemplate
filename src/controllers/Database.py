import os
import sqlite3
from contextlib import contextmanager
import logging


class Database():
    """ a class to manage SQLite Database """
    db_name = "database.db"

    def __init__(self, dbdir):
        self.dbdir = dbdir
        self.logger = logging.getLogger(__file__)
        self.connect()

    @contextmanager
    def connect(self):
        """
        connect to a SQLite DB, execute Query and Close Connection
        using Contextmanager and decorator
        Usage:
        with connect() as cur:
            cur.execute('create table if not exists temp (id int, name text)')
        """
        dbfile = os.path.join(self.dbdir, self.db_name)
        self.conn = sqlite3.connect(dbfile)
        cursor = self.conn.cursor()
        yield cursor
        self.conn.commit()
        self.conn.close()

    def close(self):
        """ close an open SQLite Connection """
        if self.conn:
            self.conn.close()
