from Parking_Lot_Design.models.user_type import UserType
from uuid import uuid4
class User:
    def __init__(self, userName:str, userType:UserType):
        self.id = uuid4()
        self.userName = userName
        self.userType = userType
        self.Vehicles = []
        self.email = None
        self.phone = None

    def add_vehicle(self, vehicle):
        self.Vehicles.append(vehicle)
    def remove_vehicle(self, vehicle):
        self.Vehicles.remove(vehicle)
    def get_vehicles(self):
        return self.Vehicles

    def __repr__(self):
        return f"User(user_id={self.id}, userName={self.userName}, userType={self.userType}, vehicles={self.Vehicles})"

