from Parking_Lot_Design.models.bill import Bill
from Parking_Lot_Design.services.paymentservice import PaymentService
from Parking_Lot_Design.models.payment import Payment


class PaymentController:
    def __init__(self, payment_service: PaymentService):
        self.payment_service = payment_service

    def make_payment(self, bill: Bill, payments) -> Bill:
        return self.payment_service.process_payment(bill, payments)