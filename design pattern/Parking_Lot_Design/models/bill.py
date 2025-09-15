from uuid import uuid4
from Parking_Lot_Design.models.ticket import Ticket
from Parking_Lot_Design.models.payment import Payment
from Parking_Lot_Design.models.bill_status import BillStatus

class Bill:
    def __init__(self, ticket: Ticket, amount: float):
        self.id = uuid4()
        self.ticket = ticket
        self.amount = amount
        self.status = BillStatus.PENDING
        self.payments: list[Payment] = []

    def add_payment(self, payment: Payment):
        """Attach a new payment and update bill status"""
        self.payments.append(payment)
        self.update_status()

    def update_status(self):
        """Check total paid vs amount due and update status"""
        total_paid = sum(p.amount for p in self.payments)

        if total_paid == 0:
            self.status = BillStatus.PENDING
        elif total_paid < self.amount:
            self.status = BillStatus.PARTIALLY_PAID
        else:
            self.status = BillStatus.PAID

    # def get_due_amount(self) -> float:
    #     total_paid = sum(p.amount for p in self.payments)
    #     return max(0, self.amount - total_paid)
