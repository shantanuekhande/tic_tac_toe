from Parking_Lot_Design.repository.base_repositorie import BaseRepository
class VehicleRepository(BaseRepository):
    def find_by_user(self, user_id):
        for vehicle in self.storage:
            if vehicle.user.id == user_id:
                return vehicle.user.Vehicles # Return all vehicles of the user
        return []
