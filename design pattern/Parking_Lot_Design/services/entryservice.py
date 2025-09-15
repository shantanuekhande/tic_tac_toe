from Parking_Lot_Design.services.userservice import UserService
from Parking_Lot_Design.services.vehicleservice import VehicleService
from Parking_Lot_Design.services.parkingservice import ParkingService
from Parking_Lot_Design.services.ticketservice import TicketService

from Parking_Lot_Design.repository.vehiclerepository import VehicleRepository
from Parking_Lot_Design.repository.ticketrepository import TicketRepository
from Parking_Lot_Design.repository.userrepository import UserRepository
from Parking_Lot_Design.repository.spotrepository import SpotRepository

from Parking_Lot_Design.models.user import User

class EntryService:
    def __init__(self, user_repo: UserRepository, vehicle_repo: VehicleRepository, ticket_repo: TicketRepository,spot_repo:SpotRepository):
        self.user_repo = user_repo
        self.vehicle_repo = vehicle_repo
        self.ticket_repo = ticket_repo
        self.spot_repo = spot_repo

    def initialize_user_service(self,user,user_repo):
        return UserService(user,user_repo)

    def initialize_vehicle_service(self,vehicle_repo):
        return VehicleService(vehicle_repo)

    def initialize_ticket_service(self,ticket_repo):
        return TicketService(ticket_repo)

    def initialize_parking_service(self,parking_repo):
        return ParkingService(parking_repo)


    def process_entry(self, user, vehicle):
        user_service = self.initialize_user_service(user,self.user_repo)
        vehicle_service = self.initialize_vehicle_service(self.vehicle_repo)
        ticket_service = self.initialize_ticket_service(self.ticket_repo)
        parking_service = self.initialize_parking_service(self.spot_repo)

        # Add or get existing user
        user = user_service.add_user(user)

        # Register vehicle
        vehicle = vehicle_service.register_vehicle(vehicle.license_plate, vehicle.vehicle_type, user)

        # Add vehicle to user
        user_service.add_vehicle_to_user(user.id, vehicle)

        # find parking spot

        spot = parking_service.assign_spot(vehicle.vehicle_type)
        if not spot:
            raise Exception("No available spots for this vehicle type")
        # Create ticket
        ticket = ticket_service.create_ticket(vehicle, spot,user.entry_gate,user)

        return ticket



