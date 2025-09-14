from uuid import uuid4
from Parking_Lot_Design.models.user import User
from Parking_Lot_Design.models.vehicle_type import VehicleType
class Vehicle:
    def __init__(self,license_plate:str,vehicle_type:VehicleType,user:User):
        self.id = uuid4()
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
        self.user = user

    def __repr__(self):
        return f"Vehicle(vehicle_id={self.id}, license_plate={self.license_plate}, vehicle_type={self.vehicle_type}, user={self.user})"