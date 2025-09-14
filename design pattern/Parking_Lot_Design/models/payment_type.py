from enum import Enum
class PaymentType(Enum):
    CASH = "Cash"
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
    MOBILE_PAYMENT = "Mobile Payment"
    ONLINE_PAYMENT = "Online Payment"
    OTHER = "Other"