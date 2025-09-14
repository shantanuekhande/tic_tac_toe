from uuid import uuid4
class Gate:
    def __init__(self,gate_type:str):
        self.id = uuid4()
        self.gate_type = gate_type