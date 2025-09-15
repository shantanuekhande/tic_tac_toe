from Parking_Lot_Design.repository.billrepository import BillRepository
from Parking_Lot_Design.repository.paymentrepository import PaymentRepository
from Parking_Lot_Design.services.billservice import BillService
import datetime

class ExitService:
    def __init__(self, bill_repo: BillRepository, payment_repo: PaymentRepository):
        self.bill_repo = bill_repo
        self.payment_repo = payment_repo



    def initialize_bill_service(self):
        return BillService(self.bill_repo)



    def process_exit(self, ticket):
        bill_service = self.initialize_bill_service()


        # lets calculate the base amount based on duration

        duration = datetime.datetime.now() - ticket.entry_time
        hours_parked = duration.total_seconds() / 3600
        base_amount = 5.0 * hours_parked  # Assuming $5 per hour

        # Calculate final amount using BillService
        final_amount = bill_service.calculate_amount(ticket, base_amount)

        # Generate bill
        bill = bill_service.generate_bill(ticket, final_amount)

        return bill
        #
        # # Process payment (Assuming payment is always successful for simplicity)
        # payment = Payment(bill=bill, amount=bill.amount, payment_method="Credit Card", status="Completed")
        # self.payment_repo.add(payment)
        #
        # # Mark the ticket as paid
        # ticket.is_paid = True
        #
        # return payment