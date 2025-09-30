import sqlite3
from typing import Any
import asyncio

from .connection_base import ConnectionBase
from .managed_cursor import ManagedCursor
from .utils import get_fullname, get_filename

class SqliteConnection(ConnectionBase):
    def __init__(self, connection_string: str = ""):
        self.provider_name = "sqlite"
        if connection_string == "":
            return

        super().__init__(connection_string)
        connection_string = self.connection_string.replace("sqlite://", "")
        connection_string = get_fullname(connection_string)
        self.connection = sqlite3.connect(connection_string, check_same_thread=False)
        self.connection.isolation_level = None
        self.database = get_filename(connection_string)
        self.cursor = self.connection.cursor()

    async def start(self):
        await asyncio.get_event_loop().run_in_executor(None, lambda cursor: cursor.execute("BEGIN TRANSACTION;", {}),
                                                       self.cursor)

    async def commit(self):
        await asyncio.get_event_loop().run_in_executor(None, lambda cursor: cursor.execute("COMMIT;"), self.cursor)

    async def rollback(self):
        await asyncio.get_event_loop().run_in_executor(None, lambda cursor: cursor.execute("ROLLBACK;"), self.cursor)

    async def execute(self, query: str, params: None):
        if params is None:
            params = {}
        await asyncio.get_event_loop().run_in_executor(None, lambda cursor: cursor.execute(query, params), self.cursor)

    async def execute_lastrowid(self, query: str, params: None) -> Any:
        if params is None:
            params = {}

        def lam(cur):
            cur.execute(query, params)
            return cur.lastrowid

        await asyncio.get_event_loop().run_in_executor(None, lambda cursor: lam, self.cursor)

    async def fetch(self, query: str, params=None) -> ManagedCursor:
        if params is None:
            params = {}
        cursor = self.connection.cursor()

        await asyncio.get_event_loop().run_in_executor(None, lambda cur: cur.execute(query, params), cursor)
        return ManagedCursor(cursor)

    async def close(self):
        await asyncio.get_event_loop().run_in_executor(None, lambda conn: conn.close(), self.connection)
