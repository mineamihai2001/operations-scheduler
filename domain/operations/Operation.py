from .procedures.Anaesthesia import Anaesthesia
from .procedures.Surgery import Surgery


class Operation:
    start: float | None
    finish: float | None
    anaesthesia: Anaesthesia
    surgical: Surgery

    def __init__(self, anaesthesia: Anaesthesia, surgical: Surgery) -> None:
        self.start = None
        self.finish = None
        self.anaesthesia = anaesthesia
        self.surgical = surgical

    def print(self) -> None:
        print((self.anaesthesia.print(), self.surgical.print()))
