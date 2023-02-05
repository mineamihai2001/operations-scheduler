from .procedures.Anaesthesia import Anaesthesia
from .procedures.Surgical import Surgical


class Operation:
    start: float | None
    finish: float | None
    anaesthesia: Anaesthesia
    surgical: Surgical

    def __init__(self, anaesthesia: Anaesthesia, surgical: Surgical) -> None:
        self.start = None
        self.finish = None
        self.anaesthesia = anaesthesia
        self.surgical = surgical

    def print(self) -> None:
        print((self.anaesthesia.print(), self.surgical.print()))
