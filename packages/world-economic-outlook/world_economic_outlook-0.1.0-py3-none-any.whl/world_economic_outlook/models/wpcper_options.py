from pydantic import BaseModel


class WPCPEROptions(BaseModel):
    currency: str = "*"
    country: str = "*"
    indicator: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
