from .Procedure import Procedure, ProcedureType


class Anaesthesia(Procedure):
    def __init__(self, procedure_length: float) -> None:
        super().__init__(ProcedureType.ANAESTHESIA, procedure_length)
