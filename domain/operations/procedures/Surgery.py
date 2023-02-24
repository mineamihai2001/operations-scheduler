from .Procedure import Procedure, ProcedureType


class Surgery(Procedure):
    def __init__(self, procedure_length: float) -> None:
        super().__init__(ProcedureType.SURGICAL, procedure_length)
