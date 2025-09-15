from Parking_Lot_Design.repository.spotrepository import   SpotRepository

class ParkingService:
    def __init__(self,spot_repo:SpotRepository):
        self.spot_repo = spot_repo

    def assign_spot(self, vehicle_type):
        available_spot = self.spot_repo.find_available_spot(vehicle_type)
        if available_spot:
            available_spot.is_occupied = True
            return available_spot
        else:
            raise Exception("No available spots for this vehicle type")

    def release_spot(self, spot_id):
        spot = self.spot_repo.get_by_id(spot_id)
        if spot:
            spot.is_occupied = False
            return spot
        else:
            raise ValueError("Spot not found")




