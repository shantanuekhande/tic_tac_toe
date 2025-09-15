from Parking_Lot_Design.repository.base_repositorie import BaseRepository

class TicketRepository(BaseRepository):
    def find_by_vehicle(self, vehicle_id):
        for ticket in self.storage:
            if ticket.vehicle.id == vehicle_id:
                return ticket
        return None

    def find_active_tickets(self):
        return [ticket for ticket in self.storage if ticket.is_active]