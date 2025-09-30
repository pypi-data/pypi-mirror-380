import asyncio
import re
from typing import Any

import mysql.connector

from .connection_base import ConnectionBase
from .managed_cursor import ManagedCursor

class MySqlConnection(ConnectionBase):
    def __init__(self, connection_string: str = ""):
        self.provider_name = "mysql"
        if connection_string == "":
            return
        super().__init__(connection_string)

        match = re.match(r"mysql:\/\/(\w+):(\w+)@(\w+)\/(\w+)", self.connection_string)
        if match:
            self.user = match.group(1)
            self.password = match.group(2)
            self.hostname = match.group(3)
            self.database = match.group(4)
        else:
            raise Exception("Invalid connection string")

        self.connection = mysql.connector.connect(user=self.user, password=self.password, host=self.hostname,
                                                  database=self.database)
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

        return await asyncio.get_event_loop().run_in_executor(None, lambda cur: lam, self.cursor)

    async def fetch(self, query: str, params=None) -> ManagedCursor:
        if params is None:
            params = {}
        cursor = self.connection.cursor()

        await asyncio.get_event_loop().run_in_executor(None, lambda cur: cur.execute(query, params), cursor)
        return ManagedCursor(cursor)

    async def close(self):
        return await asyncio.get_event_loop().run_in_executor(None, lambda conn: conn.close(), self.connection)
