from enum import Enum
class BillStatus(Enum):
    PENDING = "Pending"
    PARTIALLY_PAID = "Partially Paid"
    PAID = "Paid"