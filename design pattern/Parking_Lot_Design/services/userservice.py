from Parking_Lot_Design.repository.userrepository import UserRepository
class UserService:
    def __init__(self,user):
        self.user_repo = UserRepository()
        self.user = user

    def check_and_add_user(self,user):
        existing_user = self.user_repo.get_by_id(user.id)
        if existing_user:
            return existing_user
        else:
            return self.user_repo.add(user)

    def add_vehicle_to_user(self,user_id,vehicle):
        user = self.user_repo.get_by_id(user_id)
        if user:
            user.Vehicles.append(vehicle)
            return user
        else:
            raise ValueError("User not found")


    def remove_vehicle_from_user(self,user_id,vehicle):
        user = self.user_repo.get_by_id(user_id)
        if user:
            user.Vehicles.remove(vehicle)
            return user
        else:
            raise ValueError("User not found")

    def remove_user(self,user_id):
        return self.user_repo.remove(user_id)