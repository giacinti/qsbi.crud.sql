from typing import Tuple  # noqa: F401
from qsbi.backend.sql.models.payment_type import PaymentType as Model
from qsbi.api.schemas.payment_type import PaymentType as Schema
from qsbi.api.schemas.payment_type import PaymentTypeCreate as Create
from qsbi.api.schemas.payment_type import PaymentTypeRead as Read
from qsbi.api.schemas.payment_type import PaymentTypeUpdate as Update
from qsbi.api.schemas.payment_type import PaymentTypeDelete as Delete

from .base import SQLCRUDBase


class SQLCRUDPaymentType(SQLCRUDBase[Model, Schema, Create, Update, Read, Delete]):
    def _fields_filter(self) -> Tuple:
        return ('id', 'name')


sql_crud_payment_type = SQLCRUDPaymentType(Model, Schema, Create, Update, Read, Delete)
