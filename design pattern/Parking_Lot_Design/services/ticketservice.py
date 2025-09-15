from Parking_Lot_Design.models.ticket import Ticket
from Parking_Lot_Design.repository.ticketrepository import TicketRepository
from Parking_Lot_Design.models.gate import Gate
from Parking_Lot_Design.models.spot import Spot
from Parking_Lot_Design.models.user import User

from datetime import datetime
class TicketService:
    def __init__(self, ticket_repo: TicketRepository):
        self.ticket_repo = ticket_repo

    def create_ticket(self, vehicle, spot:Spot,gate:Gate,user:User):
        ticket = Ticket(vehicle=vehicle ,entry_gate= gate,spot= spot,user=user)
        ticket.is_active = True
        self.ticket_repo.add(ticket)
        return ticket

    def close_ticket(self, ticket_id):
        ticket = self.ticket_repo.get_by_id(ticket_id)
        if ticket and not ticket.exit_time:
            ticket.exit_time = datetime.now()
            ticket.spot.is_available = True
            # self.ticket_repo.remove(ticket_id) # not sure whether we should remove ticket or keep it for history
            ticket.is_active = False
            return ticket
        return None

    def get_tickets_by_vehicle_id(self, vehicle_id):
        return self.ticket_repo.find_by_vehicle(vehicle_id)

    def get_active_tickets(self):
        return self.ticket_repo.find_active_tickets()