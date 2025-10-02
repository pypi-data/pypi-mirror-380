from pydantic import BaseModel


class TAXFITOptions(BaseModel):
    country: str = "*"
    indicator: str = "*"
    legal_spouse_presence: str = "*"
    number_of_children: str = "*"
    principal_employment_earnings: str = "*"
    spouse_employment_earnings: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
