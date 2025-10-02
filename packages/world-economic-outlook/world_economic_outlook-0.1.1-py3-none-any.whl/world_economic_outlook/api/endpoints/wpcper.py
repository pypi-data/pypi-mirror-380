from ..base import BaseAPI
from ...models.wpcper_options import WPCPEROptions


class WPCPERAPI(BaseAPI):
    def build_endpoint(self, options: WPCPEROptions) -> str:
        def join_or_star(val):
            if isinstance(val, list):
                return "+".join(val)
            return val or "*"

        endpoint = f"WPCPER/{join_or_star(options.currency)}.{join_or_star(options.country)}.{join_or_star(options.indicator)}.{join_or_star(options.frequency)}"
        return endpoint

    def get_data(self, options: WPCPEROptions):
        endpoint = self.build_endpoint(options)
        params = {}
        if hasattr(options, "start_date") and options.start_date not in (None, "*"):
            params["startPeriod"] = options.start_date
        if hasattr(options, "end_date") and options.end_date not in (None, "*"):
            params["endPeriod"] = options.end_date
        return self.request(endpoint, params, parse_xml=True)
