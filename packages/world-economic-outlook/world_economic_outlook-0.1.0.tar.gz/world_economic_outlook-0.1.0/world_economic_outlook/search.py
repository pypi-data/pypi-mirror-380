"""Search functionality for IMF datasets."""

import re
import json
from pprint import pprint
import importlib.resources


def load_datasets():
    with importlib.resources.open_text("world_economic_outlook.structures", "DATASETS.json", encoding="utf-8") as f:
        return json.load(f)


def search(query: str) -> list[dict]:
    """Search for a database by id or name, or by keyword in id, name, or description."""
    datasets = load_datasets()
    query_lc = query.lower()
    # First, try exact match by id or name
    for db_id, info in datasets.items():
        if db_id.lower() == query_lc or info.get("name", "").lower() == query_lc:
            return [
                {
                    "database": db_id,
                    "name": info.get("name", ""),
                    "description": info.get("description", ""),
                    "wrapper": db_id.lower(),
                }
            ]
    # If no exact match, do general keyword search
    tokens = re.findall(r"\w+", query_lc)
    results = []
    for db_id, info in datasets.items():
        text = f"{db_id} {info.get('name', '')} {info.get('description', '')}".lower()
        if query_lc in text or all(token in text for token in tokens):
            results.append(
                {
                    "database": db_id,
                    "name": info.get("name", ""),
                    "description": info.get("description", ""),
                    "wrapper": db_id.lower(),
                }
            )
    return results


if __name__ == "__main__":
    # Print CPI dataset info for example
    pprint(search("CPI"))

    # Or search by keyword (e.g., "interest rates")
    pprint(search("interest rates"))
