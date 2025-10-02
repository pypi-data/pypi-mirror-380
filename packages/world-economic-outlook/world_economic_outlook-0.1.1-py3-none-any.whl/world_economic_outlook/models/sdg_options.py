from pydantic import BaseModel


class SDGOptions(BaseModel):
    freq: str = "*"
    reporting_type: str = "*"
    series: str = "*"
    ref_area: str = "*"
    sex: str = "*"
    age: str = "*"
    urbanisation: str = "*"
    income_wealth_quantile: str = "*"
    education_lev: str = "*"
    occupation: str = "*"
    cust_breakdown: str = "*"
    composite_breakdown: str = "*"
    disability_status: str = "*"
    activity: str = "*"
    product: str = "*"
    start_date: str = None
    end_date: str = None
