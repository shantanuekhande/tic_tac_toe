from uuid import uuid4
from Parking_Lot_Design.models.spot import Spot
class Floor:
    def __init__(self,floor_number:int):
        self.id = uuid4()
        self.floor_number = floor_number
        self.spots = []

    def add_spot(self,spot:Spot):
        self.spots.append(spot)

    def remove_spot(self,spot:Spot):
        self.spots.remove(spot)

    def get_available_spots(self):
        return [spot for spot in self.spots if spot.is_available]

    def get_occupied_spots(self):
        return [spot for spot in self.spots if not spot.is_available]

    def __repr__(self):
        return f"Floor(floor_id={self.id}, floor_number={self.floor_number}, total_spots={len(self.spots)})"