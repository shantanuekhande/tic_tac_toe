from uuid import uuid4
from Parking_Lot_Design.models.gate_type import GateType
class Gate:
    def __init__(self,gate_type:GateType):
        self.id = uuid4()
        self.gate_type = gate_type