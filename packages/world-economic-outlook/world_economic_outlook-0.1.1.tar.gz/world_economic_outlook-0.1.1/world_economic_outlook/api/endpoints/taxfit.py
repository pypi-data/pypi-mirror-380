from ..base import BaseAPI
from ...models.taxfit_options import TAXFITOptions


class TAXFITAPI(BaseAPI):
    def build_endpoint(self, options: TAXFITOptions) -> str:
        def join_or_star(val):
            if isinstance(val, list):
                return "+".join(val)
            return val or "*"

        endpoint = f"TAXFIT/{join_or_star(options.country)}.{join_or_star(options.indicator)}.{join_or_star(options.legal_spouse_presence)}.{join_or_star(options.number_of_children)}.{join_or_star(options.principal_employment_earnings)}.{join_or_star(options.spouse_employment_earnings)}.{join_or_star(options.frequency)}"
        return endpoint

    def get_data(self, options: TAXFITOptions):
        endpoint = self.build_endpoint(options)
        params = {}
        if hasattr(options, "start_date") and options.start_date not in (None, "*"):
            params["startPeriod"] = options.start_date
        if hasattr(options, "end_date") and options.end_date not in (None, "*"):
            params["endPeriod"] = options.end_date
        return self.request(endpoint, params, parse_xml=True)
