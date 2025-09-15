from uuid import uuid4
from datetime import datetime
from Parking_Lot_Design.models.payment_type import PaymentType
from Parking_Lot_Design.models.bill import Bill
class Payment:
    def __init__(self, amount: float, method: PaymentType,bill:Bill):
        self.amount = amount
        self.method = method  # e.g., 'cash', 'card', 'mobile'
        self.id = uuid4()
        self.timestamp = datetime.now()
        self.bill = bill

    def __repr__(self):
        return f"Payment(payment_id={self.id}, amount={self.amount}, method={self.method}, timestamp={self.timestamp})"

