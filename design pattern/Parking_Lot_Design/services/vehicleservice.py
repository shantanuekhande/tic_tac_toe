from Parking_Lot_Design.models.vehicle import Vehicle
from Parking_Lot_Design.repository.vehiclerepository import VehicleRepository

class VehicleService:
    def __init__(self, vehicle_repo: VehicleRepository):
        self.vehicle_repo = vehicle_repo

    def register_vehicle(self, license_plate, vehicle_type, user):
        vehicle = Vehicle(license_plate, vehicle_type, user)
        return self.vehicle_repo.add(vehicle)

    def get_vehicles_by_user_id(self, user_id):


        return self.vehicle_repo.find_by_user(user_id)

    def remove_vehicle(self, vehicle_id):


        return self.vehicle_repo.remove(vehicle_id)

    def get_vehicle_by_vehicle_id(self, vehicle_id):
        return self.vehicle_repo.get_by_id(vehicle_id)