from pydantic import BaseModel


class COFEROptions(BaseModel):
    country: str = "*"
    indicator: str = "*"
    fxr_currency: str = "*"
    type_of_transformation: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
