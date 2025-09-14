from uuid import uuid4
class Spot:
    def __init__(self,floor_id:int):
        self.id = uuid4()
        self.is_available = True
        self.vehicle = None
        self.floor_id = floor_id

    def assign_vehicle(self,vehicle):
        self.vehicle = vehicle
        self.is_available = False

    def remove_vehicle(self):
        self.vehicle = None
        self.is_available = True


    def __repr__(self):
        return f"Spot(spot_id={self.id}, is_available={self.is_available}, floor_id={self.floor_id})"
