from typing import Tuple
from qsbi.backend.sql.models.payment import Payment as Model
from qsbi.api.schemas.payment import Payment as Schema
from qsbi.api.schemas.payment import PaymentCreate as Create
from qsbi.api.schemas.payment import PaymentRead as Read
from qsbi.api.schemas.payment import PaymentUpdate as Update
from qsbi.api.schemas.payment import PaymentDelete as Delete

from .base import SQLCRUDBase

class SQLCRUDPayment(SQLCRUDBase[Model, Schema, Create, Update, Read, Delete]):
    ...

sql_crud_payment = SQLCRUDPayment(Model, Schema, Create, Update, Read, Delete)
