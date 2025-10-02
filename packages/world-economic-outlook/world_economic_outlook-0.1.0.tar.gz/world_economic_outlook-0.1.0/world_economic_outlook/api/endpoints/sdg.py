from ..base import BaseAPI
from ...models.sdg_options import SDGOptions


class SDGAPI(BaseAPI):
    def build_endpoint(self, options: SDGOptions) -> str:
        def join_or_star(val):
            if isinstance(val, list):
                return "+".join(val)
            return val or "*"

        endpoint = f"SDG/{join_or_star(options.freq)}.{join_or_star(options.reporting_type)}.{join_or_star(options.series)}.{join_or_star(options.ref_area)}.{join_or_star(options.sex)}.{join_or_star(options.age)}.{join_or_star(options.urbanisation)}.{join_or_star(options.income_wealth_quantile)}.{join_or_star(options.education_lev)}.{join_or_star(options.occupation)}.{join_or_star(options.cust_breakdown)}.{join_or_star(options.composite_breakdown)}.{join_or_star(options.disability_status)}.{join_or_star(options.activity)}.{join_or_star(options.product)}"
        return endpoint

    def get_data(self, options: SDGOptions):
        endpoint = self.build_endpoint(options)
        params = {}
        if hasattr(options, "start_date") and options.start_date not in (None, "*"):
            params["startPeriod"] = options.start_date
        if hasattr(options, "end_date") and options.end_date not in (None, "*"):
            params["endPeriod"] = options.end_date
        return self.request(endpoint, params, parse_xml=True)
