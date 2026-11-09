import sqlite3
from collections.abc import Generator
from contextlib import contextmanager


class DatabaseConnection:
    def __init__(self, path: str):
        self.connection = sqlite3.connect(path)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = ON")

    @contextmanager
    def transaction(self) -> Generator[sqlite3.Cursor]:
        cursor = self.connection.cursor()

        try:
            yield cursor
            self.connection.commit()

        except Exception:
            self.connection.rollback()
            raise
        finally:
                cursor.close()


    def close(self) -> None:
        self.connection.close()
