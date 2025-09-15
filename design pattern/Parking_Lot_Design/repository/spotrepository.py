from Parking_Lot_Design.repository.base_repositorie import BaseRepository

class SpotRepository(BaseRepository):
    def find_available_spot(self, vehicle_type):
        for spot in self.storage:
            if spot.is_available and spot.spot_type == vehicle_type:
                return spot
        return None
