from uuid import uuid4
from datetime import datetime
from Parking_Lot_Design.models.vehicle import Vehicle
from Parking_Lot_Design.models.gate import Gate
from Parking_Lot_Design.models.spot import Spot
from Parking_Lot_Design.models.user import User
class Ticket:
    def __init__(self,vehicle:Vehicle,entry_gate:Gate,spot:Spot,user:User):
        self.id = uuid4()
        self.spot = spot
        self.vehicle = vehicle
        self.entry_gate = entry_gate
        self.entry_time = datetime.now()
        self.exit_gate = None
        self.exit_time = None
        self.is_active = True
        self.user = user

