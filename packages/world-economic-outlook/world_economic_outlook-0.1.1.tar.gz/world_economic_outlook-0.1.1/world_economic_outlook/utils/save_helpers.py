"""Helpers for saving records to file in various formats."""

import json
import csv


def save_records(records: list[dict], save_path: str, file_format: str = "json"):
    """
    Save records to file in json, csv, or txt (tab-delimited) format.
    """
    if file_format == "json":
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
    elif file_format == "csv":
        if records:
            with open(save_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=records[0].keys())
                writer.writeheader()
                writer.writerows(records)
    elif file_format == "txt":
        if records:
            with open(save_path, "w", encoding="utf-8") as f:
                header = "\t".join(records[0].keys())
                f.write(header + "\n")
                for rec in records:
                    row = "\t".join(str(rec[k]) for k in records[0].keys())
                    f.write(row + "\n")
    else:
        raise ValueError(f"Unsupported file format: {file_format}")
