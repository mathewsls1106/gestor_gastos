from .db_connection import DatabaseConnection


class DBBuilder:
    def __init__(self, database: DatabaseConnection) -> None:
        self.db = database

    def build_db(self) -> None:
        with self.db.transaction() as cursor:
            cursor.execute(""" create table if not exists gastos (
                id integer primary key autoincrement,
                amount real not null,
                description text,
                created_at datetime,
                updated_at datetime
            )""")
