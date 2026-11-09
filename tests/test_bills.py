import pytest

from src.exceptions import NegativeQuantityError
from src.repositories.billing_repository import BillingRepository
from src.utils.db_connection import DatabaseConnection

database = DatabaseConnection("mi_base_de_datos_local.db")
repository = BillingRepository(database)

def test_given_a_negative_amount_when_saving_then_raise():
    # dado
    amount = -10000

    # cuando / luego
    with pytest.raises(NegativeQuantityError):
        repository.save(amount, "pruebas")
