

from Parking_Lot_Design.services.entryservice import EntryService
from Parking_Lot_Design.services.exitservice import ExitService
from Parking_Lot_Design.services.paymentservice import PaymentService

from Parking_Lot_Design.controllers.entrycontroller import EntryController
from Parking_Lot_Design.controllers.paymentcontroller import PaymentController
from Parking_Lot_Design.controllers.exitcontroller import ExitController

from Parking_Lot_Design.repository.vehiclerepository import VehicleRepository
from Parking_Lot_Design.repository.ticketrepository import TicketRepository
from Parking_Lot_Design.repository.userrepository import UserRepository
from Parking_Lot_Design.repository.spotrepository import SpotRepository
from Parking_Lot_Design.repository.paymentrepository import PaymentRepository
from Parking_Lot_Design.repository.billrepository import BillRepository
from Parking_Lot_Design.repository.floorrepository import FloorRepository

from Parking_Lot_Design.models.ticket import Ticket
from Parking_Lot_Design.models.payment import Payment
from Parking_Lot_Design.models.bill_status import BillStatus
from Parking_Lot_Design.models.user import User
from Parking_Lot_Design.models.parking_lot import ParkingLot
from Parking_Lot_Design.models.floor import Floor
from Parking_Lot_Design.models.payment import Payment
from Parking_Lot_Design.models.bill import Bill
from Parking_Lot_Design.models.spot import Spot
from Parking_Lot_Design.models.user_type import UserType
from Parking_Lot_Design.models.vehicle import Vehicle
from Parking_Lot_Design.models.vehicle_type import VehicleType
from Parking_Lot_Design.models.payment_type import PaymentType
from Parking_Lot_Design.models.gate_type import GateType
from Parking_Lot_Design.models.gate import Gate
# function to create parking lot with spots
def create_parking_lot(spot_repo: SpotRepository , floor_repo:FloorRepository):
    parking_lot = ParkingLot("Central Parking", "123 Main St", 2 , 2)
    add_spots_to_floor(parking_lot, spot_repo,floor_repo)
    return parking_lot

#  lets add spots to floor

def add_spots_to_floor(parking_lot: ParkingLot, spot_repo: SpotRepository,floor_repo:FloorRepository):
    # add slot per floor using parking lot capacity
    floores = []
    for floor_number in range(parking_lot.number_of_floors):
        new_floor = Floor(floor_number)
        for spot_number in range(parking_lot.number_of_spots_per_floor):
            new_spot = Spot(new_floor.id)
            spot_repo.add(new_spot)
            new_floor.add_spot(new_spot)
        floor_repo.add(new_floor)
        floores.append(new_floor)

    parking_lot.floors = floores
    return parking_lot





def main():
    # Initialize repositories
    user_repo = UserRepository()
    vehicle_repo = VehicleRepository()
    ticket_repo = TicketRepository()
    spot_repo = SpotRepository()
    bill_repo = BillRepository()
    payment_repo = PaymentRepository()
    floor_repo = FloorRepository()

    # Initialize services
    entry_service = EntryService(user_repo, vehicle_repo, ticket_repo, spot_repo)
    exit_service = ExitService(bill_repo, payment_repo)
    payment_service = PaymentService(payment_repo,bill_repo)


    # Initialize controllers
    entry_controller = EntryController(entry_service)
    exit_controller = ExitController(exit_service)
    payment_controller = PaymentController(payment_service)

    # Initialize parking lot
    parking_lot = create_parking_lot(spot_repo,floor_repo)

    # Simulate user entry
    user = User("John Doe", UserType.REGULAR)

    # Assign entry
    entry_gate = Gate(GateType.ENTRY)
    user.entry_gate = entry_gate
    # Simulate user vehicle
    vehicle = Vehicle("ABC123", VehicleType.CAR, user)

    # Issue ticket
    print("User entering the parking lot...")
    print("user:", user.username, "Type:", user.usertype)
    print("Vehicle:", vehicle.license_plate, "Type:", vehicle.vehicle_type)

    ticket = entry_controller.issue_ticket(user, vehicle)
    print(f"Ticket issued: {ticket.id} for vehicle {vehicle.license_plate}")

    # Simulate user exit
    print("\nUser exiting the parking lot...")

    # Assign exit gate
    exit_gate = Gate(GateType.EXIT)
    user.exit_gate = exit_gate

    bill = exit_controller.process_exit(ticket)
    print(f"Bill generated: {bill.id} with amount ${bill.amount:.2f} and status {bill.status}")

    # Simulate payment
    print('\nProcessing payment...')
    pa = [Payment(bill=bill, amount=bill.amount, method=PaymentType.CREDIT_CARD)]

    bill = payment_controller.make_payment(bill,pa)

    print("bill:", bill.id, f"Amount: ${bill.amount:.2f}, Status: {bill.status}")
    print(f"Bill status after payment: {bill.status}")


def test():
    main()

test()





