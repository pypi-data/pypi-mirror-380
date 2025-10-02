"""Helper functions for IMF API wrapper."""

import re


def parse_imf_date(date_str : str) -> str | None:
    """
    Parse IMF date strings to ISO format (YYYY-MM-DD).
    Handles monthly (YYYY-MMM), quarterly (YYYY-QN), annual (YYYY).
    Returns ISO date string or None if format is unknown.
    """
    if re.match(r"^\d{4}-M\d{2}$", date_str):  # Monthly
        year, month = date_str.split("-M")
        return f"{year}-{month}-01"
    elif re.match(r"^\d{4}-Q[1-4]$", date_str):  # Quarterly
        year, quarter = date_str.split("-Q")
        month = str((int(quarter) - 1) * 3 + 1).zfill(2)
        return f"{year}-{month}-01"
    elif re.match(r"^\d{4}$", date_str):  # Annual
        return f"{date_str}-01-01"
    else:
        return None


def infer_file_format(save_path: str) -> str:
    if save_path.endswith(".json"):
        return "json"
    elif save_path.endswith(".csv"):
        return "csv"
    elif save_path.endswith(".txt"):
        return "txt"
    else:
        raise ValueError(
            f"Unknown file format for '{save_path}'. Please use .json, .csv, or .txt."
        )
