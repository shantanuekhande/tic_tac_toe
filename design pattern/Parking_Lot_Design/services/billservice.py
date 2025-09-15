from Parking_Lot_Design.models.bill import Bill
from Parking_Lot_Design.models.ticket import Ticket
from Parking_Lot_Design.repository.billrepository import BillRepository
from Parking_Lot_Design.services.billingdecorator import  *
from Parking_Lot_Design.models.user_type import UserType
from Parking_Lot_Design.models.vehicle_type import VehicleType
class BillService:
    def __init__(self, bill_repository: BillRepository):
        self.bill_repository = bill_repository


    def _apply_vehicle_decorator(self, vehicle_type: VehicleType, billing: Billing) -> Billing:
        mapping = {
            VehicleType.CAR: CarBilling,
            VehicleType.MOTORCYCLE: BikeBilling,
            VehicleType.TRUCK: TruckBilling,
            VehicleType.EV: EVBilling,
        }
        decorator_class = mapping.get(vehicle_type)
        if decorator_class:
            return decorator_class(billing)
        return billing

    def _apply_user_decorator(self, user_type_: UserType, billing: Billing) -> Billing:
        mapping = {
            UserType.REGULAR: RegularBilling,
            UserType.VIP: VIPBilling,
            UserType.EMPLOYEE: EmployeeBilling,
        }
        decorator_class = mapping.get(user_type_)
        if decorator_class:
            return decorator_class(billing)
        return billing

    def calculate_amount(self, ticket, base_amount: float) -> float:
        billing: Billing = BaseBilling()

        # Apply vehicle decorator
        billing = self._apply_vehicle_decorator(ticket.vehicle.vehicle_type, billing)

        # Apply user decorator
        billing = self._apply_user_decorator(ticket.user.usertype, billing)

        return billing.calculate(base_amount)



    def generate_bill(self, ticket: Ticket, amount: float) -> Bill:
        bill = Bill(ticket=ticket, amount=amount)
        self.bill_repository.add(bill)
        return bill



    def get_bill_by_ticket(self, ticket_id):
        for bill in self.bill_repository.storage:
            if bill.ticket.id == ticket_id:
                return bill
        return None




