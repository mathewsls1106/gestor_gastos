from datetime import datetime

from src.exceptions.exceptions import NegativeQuantityError
from src.utils.db_connection import DatabaseConnection


class BillingRepository:
    def __init__(self, db: DatabaseConnection) -> None:
        self._db = db

    def save(self, amount: float, description: str) -> int | None:

        if amount <= 0:
            raise NegativeQuantityError("El numero no puede ser inferior o igual a 0")

        with self._db.transaction() as cursor:
            fecha = datetime.now().isoformat()
            cursor.execute("INSERT INTO gastos (amount, description, created_at, updated_at) values ( ?, ?, ?, ?)" ,
                (amount, description, fecha, fecha))
            return cursor.lastrowid
