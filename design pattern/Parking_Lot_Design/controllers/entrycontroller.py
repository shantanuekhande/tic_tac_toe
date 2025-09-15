from Parking_Lot_Design.services.entryservice import EntryService
from Parking_Lot_Design.models.user import User
from Parking_Lot_Design.models.vehicle import Vehicle
class EntryController:
    def __init__(self,entry_service:EntryService):
        self.entry_service = entry_service

    def issue_ticket(self,user:User,vehicle:Vehicle):
        return self.entry_service.process_entry(user, vehicle)

