from .account import sql_crud_account
from .account_type import sql_crud_account_type
from .audit_log import sql_crud_audit_log
from .bank import sql_crud_bank
from .category import sql_crud_category
from .currency_link import sql_crud_currency_link
from .currency import sql_crud_currency
from .party import sql_crud_party
from .payment import sql_crud_payment
from .payment_type import sql_crud_payment_type
from .reconcile import sql_crud_reconcile
from .scheduled import sql_crud_scheduled
from .sub_category import sql_crud_sub_category
from .transact import sql_crud_transact
from .user import sql_crud_user

import qsbi.api.crud
qsbi.api.crud.account = sql_crud_account
qsbi.api.crud.account_type = sql_crud_account_type
qsbi.api.crud.audit_log = sql_crud_audit_log
qsbi.api.crud.bank = sql_crud_bank
qsbi.api.crud.category = sql_crud_category
qsbi.api.crud.currency_link = sql_crud_currency_link
qsbi.api.crud.currency = sql_crud_currency
qsbi.api.crud.party = sql_crud_party
qsbi.api.crud.payment = sql_crud_payment
qsbi.api.crud.payment_type = sql_crud_payment_type
qsbi.api.crud.reconcile = sql_crud_reconcile
qsbi.api.crud.scheduled = sql_crud_scheduled
qsbi.api.crud.sub_category = sql_crud_sub_category
qsbi.api.crud.transact = sql_crud_transact
qsbi.api.crud.user = sql_crud_user
