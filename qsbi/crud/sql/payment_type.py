from typing import Tuple
from qsbi.backend.sql.models.payment_type import PaymentType as Model
from qsbi.api.schemas.payment_type import PaymentType as Schema
from qsbi.api.schemas.payment_type import PaymentTypeDict as Dict
from qsbi.api.schemas.payment_type import PaymentTypeCreate as Create
from qsbi.api.schemas.payment_type import PaymentTypeRead as Read
from qsbi.api.schemas.payment_type import PaymentTypeUpdate as Update
from qsbi.api.schemas.payment_type import PaymentTypeDelete as Delete

from .base import SQLCRUDBase

class SQLCRUDPaymentType(SQLCRUDBase[Model, Schema, Dict, Create, Update, Read, Delete]):
    def _fields_filter(self) -> Tuple:
        return ('id','name')

sql_crud_payment_type = SQLCRUDPaymentType(Model, Schema, Dict, Create, Update, Read, Delete)
