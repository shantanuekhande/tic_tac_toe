from Parking_Lot_Design.services.exitservice import ExitService
from Parking_Lot_Design.models.ticket import Ticket

class ExitController:
    def __init__(self,exit_service:ExitService):
        self.exit_service = exit_service

    def process_exit(self,ticket:Ticket):
        return self.exit_service.process_exit(ticket)