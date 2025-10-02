"""Base API logic for IMF data requests."""

import requests
import xml.etree.ElementTree as ET


class BaseAPI:
    BASE_URL = "https://api.imf.org/external/sdmx/2.1/data/"

    def request(self, endpoint: str, params: dict = None, parse_xml: bool = False):
        url = self.BASE_URL + endpoint
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            content_type = response.headers.get("Content-Type", "")
            if "application/json" in content_type:
                return response.json()
            elif parse_xml:
                root = ET.fromstring(response.text)
                obs_list = []
                for series in root.findall(".//Series"):
                    series_attrs = series.attrib.copy()
                    for obs in series.findall(".//Obs"):
                        record = series_attrs.copy()
                        record.update(obs.attrib)
                        obs_list.append(record)
                return obs_list
            else:
                return response.text
        except requests.RequestException as e:
            raise RuntimeError(f"API request failed: {e}")
