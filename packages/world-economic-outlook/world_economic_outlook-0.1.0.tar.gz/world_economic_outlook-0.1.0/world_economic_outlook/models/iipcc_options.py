from pydantic import BaseModel


class IIPCCOptions(BaseModel):
    country: str = "*"
    bop_accounting_entry: str = "*"
    indicator: str = "*"
    currency: str = "*"
    unit: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
