from uuid import UUID
from datetime import datetime
from Parking_Lot_Design.models.vehicle import Vehicle
from Parking_Lot_Design.models.gate import Gate
from Parking_Lot_Design.models.spot import Spot
class Ticket:
    def __init__(self,vehicle:Vehicle,entry_gate:Gate,spot:Spot):
        self.id = UUID()
        self.spot = spot
        self.vehicle = vehicle
        self.entry_gate = entry_gate
        self.entry_time = datetime.now()
        self.exit_gate = None
        self.exit_time = None
        self.is_active = True

