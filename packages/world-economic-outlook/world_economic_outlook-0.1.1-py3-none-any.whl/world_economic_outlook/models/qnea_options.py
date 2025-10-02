from pydantic import BaseModel


class QNEAOptions(BaseModel):
    country: str = "*"
    indicator: str = "*"
    price_type: str = "*"
    s_adjustment: str = "*"
    type_of_transformation: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
