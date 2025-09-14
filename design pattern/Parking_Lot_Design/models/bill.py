from uuid import uuid4
from datetime import datetime, timedelta
from Parking_Lot_Design.models.ticket import  Ticket
from Parking_Lot_Design.models.payment import  Payment
from Parking_Lot_Design.models.bill_status import BillStatus
class Bill:
    def __init__(self, ticket: Ticket, amount: float):
        self.id = uuid4()
        self.ticket = ticket
        self.amount = amount
        self.is_paid = BillStatus.PENDING
        self.payment = []



    def add_payment(self,payment:Payment):
        self.payment.append(payment)

    def check_payment_status(self,payment:Payment):
        total_paid = 0
        for pay in self.payment:
            total_paid += pay.amount

        if total_paid >= payment.amount:
            self.is_paid = BillStatus.PAID
            return True
        elif payment.amount > total_paid > 0:
            self.is_paid = BillStatus.PARTIALLY_PAID
            return False
        else:
            self.is_paid = BillStatus.PENDING
            return False

    def get_due_amount(self):
        total_paid = 0
        for pay in self.payment:
            total_paid += pay.amount
        return self.amount - total_paid


    def __repr__(self):
        return f"Bill(bill_id={self.id}, ticket={self.ticket}, amount={self.amount}, is_paid={self.is_paid}, payment_methods={self.payment})"