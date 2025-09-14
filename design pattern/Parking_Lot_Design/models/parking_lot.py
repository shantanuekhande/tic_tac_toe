from uuid import uuid4
class ParkingLot:
    def __init__(self,name:str,location:str,number_of_floors:int,number_of_spots_per_floor:int):
        self.parking_lot_id = uuid4()
        self.name = name
        self.location = location
        self.number_of_floors = number_of_floors
        self.number_of_spots_per_floor = number_of_spots_per_floor
