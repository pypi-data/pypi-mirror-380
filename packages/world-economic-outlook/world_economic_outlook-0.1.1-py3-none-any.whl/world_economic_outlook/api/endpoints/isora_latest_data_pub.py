from ..base import BaseAPI
from ...models.isora_latest_data_pub_options import ISORA_LATEST_DATA_PUBOptions


class ISORA_LATEST_DATA_PUBAPI(BaseAPI):
    def build_endpoint(self, options: ISORA_LATEST_DATA_PUBOptions) -> str:
        def join_or_star(val):
            if isinstance(val, list):
                return "+".join(val)
            return val or "*"

        endpoint = f"ISORA_LATEST_DATA_PUB/{join_or_star(options.jurisdiction)}.{join_or_star(options.indicator)}.{join_or_star(options.frequency)}"
        return endpoint

    def get_data(self, options: ISORA_LATEST_DATA_PUBOptions):
        endpoint = self.build_endpoint(options)
        params = {}
        if hasattr(options, "start_date") and options.start_date not in (None, "*"):
            params["startPeriod"] = options.start_date
        if hasattr(options, "end_date") and options.end_date not in (None, "*"):
            params["endPeriod"] = options.end_date
        return self.request(endpoint, params, parse_xml=True)
