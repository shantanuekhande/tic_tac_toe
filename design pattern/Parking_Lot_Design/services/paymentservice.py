from Parking_Lot_Design.repository.paymentrepository import PaymentRepository
from Parking_Lot_Design.repository.billrepository import BillRepository
from Parking_Lot_Design.models.payment import Payment
from Parking_Lot_Design.models.bill import Bill


class PaymentService:
    def __init__(self):
        self.payment_repo = PaymentRepository()
        self.bill_repo = BillRepository()

    def process_payment(self, bill: Bill ,payments) -> Bill:
        for payment in payments:
            bill.add_payment(payment)
            self.payment_repo.add(payment)
        self.bill_repo.add(bill)
        return bill
