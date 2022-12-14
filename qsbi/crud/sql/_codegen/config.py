from module import CRUDModule

CRUDModule("account", "Account", ["id_and_name.j2"])
CRUDModule("account_type", "AccountType", ["id_and_name.j2"])
CRUDModule("audit_log", "AuditLog")
CRUDModule("bank", "Bank", ["id_and_name.j2"])
CRUDModule("category", "Category", ["id_and_name.j2"])
CRUDModule("currency", "Currency", ["currency.j2"])
CRUDModule("currency_link", "CurrencyLink")
CRUDModule("party", "Party", ["id_and_name.j2"])
CRUDModule("payment", "Payment")
CRUDModule("payment_type", "PaymentType", ["id_and_name.j2"])
CRUDModule("reconcile", "Reconcile")
CRUDModule("scheduled", "Scheduled")
CRUDModule("sub_category", "SubCategory")
CRUDModule("transact", "Transact")
CRUDModule("user", "User", ["user.j2"])
