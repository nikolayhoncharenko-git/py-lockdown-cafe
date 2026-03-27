import datetime

from typing import Any
from app import errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

    def visit_cafe(self, visitor: dict) -> Any:
        vaccine = visitor.get("vaccine")

        if vaccine is None:
            raise errors.NotVaccinatedError("NotWearingMaskError")
        else:
            expiration_date = vaccine["expiration_date"]
            if expiration_date < datetime.date.today():
                raise errors.OutdatedVaccineError("NotVaccinatedError")

        wearing_a_mask = visitor.get("wearing_a_mask")

        if wearing_a_mask is None or wearing_a_mask is False:
            raise errors.NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
