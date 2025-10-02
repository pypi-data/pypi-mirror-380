from pydantic import BaseModel


class PIPOptions(BaseModel):
    country: str = "*"
    accounting_entry: str = "*"
    indicator: str = "*"
    sector: str = "*"
    counterpart_sector: str = "*"
    counterpart_country: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
