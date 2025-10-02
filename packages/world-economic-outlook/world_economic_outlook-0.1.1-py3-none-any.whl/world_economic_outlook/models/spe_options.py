from pydantic import BaseModel


class SPEOptions(BaseModel):
    country: str = "*"
    bop_accounting_entry: str = "*"
    indicator: str = "*"
    unit: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
