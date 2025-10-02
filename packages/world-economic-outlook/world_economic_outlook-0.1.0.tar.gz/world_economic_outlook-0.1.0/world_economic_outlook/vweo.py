"""
Vintage World Economic Outlook (WEO) data from the IMF.
Works slightly differently from other wrappers, as WEO data are provided
as a *complete* dataset for each vintage (e.g., "April 2025").
"""

import requests
import re
import io
import csv
from simple_sqlite3 import Database
from typing import Optional, List, Dict
from .utils.iso_mappings import iso_alpha3_to_alpha2
from .utils.save_helpers import save_records


def download_weo_data(year: int, month: str) -> bytes:
    """
    Downloads the IMF WEO data file for a given year and month.
    Args:
        year (int): The year of the WEO vintage.
        month (str): The month of the WEO vintage (e.g., 'April', 'October').
    Returns:
        bytes: The downloaded WEO data file as bytes.
    Raises:
        ValueError: If the WEO data link is not found on the IMF page.
        Exception: For network or download errors.
    """
    url = f"https://www.imf.org/en/Publications/WEO/weo-database/{year}/{month}/download-entire-database"
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        html = response.text
    except Exception as e:
        raise Exception(f"Failed to fetch WEO page: {e}")
    match = re.search(
        r'href="(/-/media/Files/Publications/WEO/WEO-Database[^"]+)"', html
    )
    if not match:
        raise ValueError("WEO data link not found on the IMF page.")
    file_url = "https://www.imf.org" + match.group(1)
    try:
        file_response = requests.get(file_url, timeout=60)
        file_response.raise_for_status()
        data = file_response.content
    except Exception as e:
        raise Exception(f"Failed to download WEO data file: {e}")
    return data


def push_weo_data(
    data: bytes,
    database: str,
    vintage: str,
    table: str = "weo",
) -> None:
    """
    Parses and pushes WEO data into a SQLite database table.
    Args:
        data (bytes): The WEO data file as bytes.
        database (str): Path to the SQLite database file.
        table (str): Name of the table to insert data into.
        vintage (str): The vintage string (e.g., '2025 April').
    Raises:
        RuntimeError: If the data cannot be read with any of the tried encodings.
    """
    encodings_to_try = ["utf-16-le", "utf-8", "windows-1250", "latin-1"]
    last_exception = None
    for encoding in encodings_to_try:
        try:
            file = io.TextIOWrapper(
                io.BytesIO(data), encoding=encoding, errors="replace"
            )
            reader = csv.reader(file, delimiter="\t")
            headers = next(reader)
            # Remove null bytes and strip whitespace from all headers
            headers = [
                h.replace("\x00", "")
                .replace("\u0000", "")
                .replace("\0", "")
                .replace(chr(0), "")
                .strip()
                for h in headers
            ]
            break
        except Exception as e:
            last_exception = e
            continue
    else:
        raise RuntimeError(
            f"Failed to read WEO data with tried encodings {encodings_to_try}: {last_exception}"
        )
    try:
        estimates_start_after_idx = headers.index("Estimates Start After")
    except ValueError:
        raise RuntimeError(
            "'Estimates Start After' column not found in WEO data headers. Headers found: "
            + str(headers)
        )
    rows = []
    for row in reader:
        try:
            iso = iso_alpha3_to_alpha2.get(row[1], row[1])
            iso_alpha3 = row[1]
            weo_subject_code = row[2]
            country = row[3]
            subject_descriptor = row[4]
            units = row[6]
            scale = row[7] if len(row) > 7 else None
            estimates_start_after = (
                int(row[estimates_start_after_idx])
                if row[estimates_start_after_idx].isdigit()
                else None
            )
            for col_idx in range(9, estimates_start_after_idx):
                year_col = "".join(filter(str.isdigit, headers[col_idx]))
                try:
                    value = float(row[col_idx])
                except (ValueError, TypeError):
                    value = None
                if year_col:
                    rows.append(
                        (
                            iso,
                            iso_alpha3,
                            weo_subject_code,
                            country,
                            subject_descriptor,
                            units,
                            scale,
                            int(year_col),
                            value,
                            estimates_start_after,
                            int(
                                estimates_start_after is not None
                                and int(year_col) > estimates_start_after
                            ),
                            vintage,
                        )
                    )
        except IndexError:
            continue
    schema = """
        iso TEXT,
        iso_alpha3 TEXT,
        weo_subject_code TEXT,
        country TEXT,
        subject_descriptor TEXT,
        units TEXT,
        scale TEXT,
        year INTEGER,
        value REAL,
        estimates_start_after INTEGER,
        estimate INTEGER,
        vintage TEXT
    """
    columns = tuple(col.strip().split()[0] for col in schema.strip().split(",\n"))
    try:
        with Database(database) as db:
            table = db.table(table)
            table.insert_many(rows=rows, columns=columns, schema=schema)
    except Exception as e:
        raise Exception(f"Database error: {e}")


def save_weo_data(
    year: int, month: str, data: bytes, path: Optional[str] = None
) -> None:
    """
    Saves the WEO data as an .xls file to the specified path.
    Args:
        year (int): The year of the WEO data.
        month (str): The month of the WEO data.
        data (bytes): The WEO data to save.
        path (str, optional): The file path to save the data. Defaults to '{year}_{month}.xls'.
    Raises:
        ValueError: If no data is provided.
        Exception: If file writing fails.
    """
    if not data:
        raise ValueError("No data to save. Please download the data first.")
    if path is None:
        path = f"{year}_{month}.xls"
    try:
        with open(path, "wb") as file:
            file.write(data)
        print(f"WEO data saved to '{path}' successfully.")
    except Exception as e:
        print(f"Failed to save WEO data: {e}")
        raise


def parse_weo_data(
    data: bytes,
    vintage: str,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
    indicator: str | list[str] = None,
    isos: str | list[str] = "*",
    start_year: int = None,
    end_year: int = None,
) -> List[Dict]:
    """
    Parses the WEO data bytes into a list of records (dicts).
    Args:
        data (bytes): The WEO data file as bytes.
        vintage (str): The vintage string (e.g., '2025 April').
    Returns:
        List[Dict]: List of parsed records.
    """
    encodings_to_try = ["utf-16-le", "utf-8", "windows-1250", "latin-1"]
    last_exception = None
    for encoding in encodings_to_try:
        try:
            file = io.TextIOWrapper(
                io.BytesIO(data), encoding=encoding, errors="replace"
            )
            reader = csv.reader(file, delimiter="\t")
            headers = next(reader)
            headers = [
                h.replace("\x00", "")
                .replace("\u0000", "")
                .replace("\0", "")
                .replace(chr(0), "")
                .strip()
                for h in headers
            ]
            break
        except Exception as e:
            last_exception = e
            continue
    else:
        raise RuntimeError(
            f"Failed to read WEO data with tried encodings {encodings_to_try}: {last_exception}"
        )
    try:
        estimates_start_after_idx = headers.index("Estimates Start After")
    except ValueError:
        raise RuntimeError(
            "'Estimates Start After' column not found in WEO data headers. Headers found: "
            + str(headers)
        )
    records = []
    # Normalise indicator and isos to lists for easier checking
    indicator_list = None
    if indicator is not None:
        indicator_list = [indicator] if isinstance(indicator, str) else indicator
    isos_list = None
    if isos is not None and isos != "*":
        isos_list = [isos] if isinstance(isos, str) else isos
    # Handle year constraints
    year_min = start_year if start_year is not None else None
    year_max = end_year if end_year is not None else None
    if full_output:
        for row in reader:
            try:
                iso = (
                    iso_alpha3_to_alpha2.get(row[1], row[1])
                    if use_iso_alpha2
                    else row[1]
                )
                indicator_val = row[2]
                country = row[3]
                description = row[4]
                units = row[6]
                scale = row[7] if len(row) > 7 else None
                estimates_start_after = (
                    int(row[estimates_start_after_idx])
                    if row[estimates_start_after_idx].isdigit()
                    else None
                )
                # Filtering by indicator and isos
                if indicator_list is not None and indicator_val not in indicator_list:
                    continue
                if isos_list is not None and iso not in isos_list:
                    continue
                for col_idx in range(9, estimates_start_after_idx):
                    year_col = "".join(filter(str.isdigit, headers[col_idx]))
                    if year_col:
                        year_val = int(year_col)
                        # Filtering by year range
                        if year_min is not None and year_val < year_min:
                            continue
                        if year_max is not None and year_val > year_max:
                            continue
                        try:
                            value = float(row[col_idx])
                        except (ValueError, TypeError):
                            value = None
                        if value is None:
                            continue
                        records.append(
                            {
                                "iso": iso,
                                "indicator": indicator_val,
                                "country": country,
                                "description": description,
                                "units": units,
                                "scale": scale,
                                "year": year_val,
                                "value": value,
                                "estimates_start_after": estimates_start_after,
                                "estimate": int(
                                    estimates_start_after is not None
                                    and year_val > estimates_start_after
                                ),
                                "vintage": vintage,
                            }
                        )
            except IndexError:
                continue
    else:
        for row in reader:
            try:
                iso = (
                    iso_alpha3_to_alpha2.get(row[1], row[1])
                    if use_iso_alpha2
                    else row[1]
                )
                indicator_val = row[2]
                scale = row[7] if len(row) > 7 else None
                estimates_start_after = (
                    int(row[estimates_start_after_idx])
                    if row[estimates_start_after_idx].isdigit()
                    else None
                )
                # Filtering by indicator and isos
                if indicator_list is not None and indicator_val not in indicator_list:
                    continue
                if isos_list is not None and iso not in isos_list:
                    continue
                for col_idx in range(9, estimates_start_after_idx):
                    year_col = "".join(filter(str.isdigit, headers[col_idx]))
                    if year_col:
                        year_val = int(year_col)
                        # Filtering by year range
                        if year_min is not None and year_val < year_min:
                            continue
                        if year_max is not None and year_val > year_max:
                            continue
                        try:
                            value = float(row[col_idx])
                        except (ValueError, TypeError):
                            value = None
                        if value is None:
                            continue
                        records.append(
                            {
                                "iso": iso,
                                "indicator": indicator_val,
                                "year": year_val,
                                "value": value,
                                "estimate": int(
                                    estimates_start_after is not None
                                    and year_val > estimates_start_after
                                ),
                                "vintage": vintage,
                            }
                        )
            except IndexError:
                continue

    return records


def vweo(
    vintage: str | list[str] = None,
    isos: str | list[str] = "*",
    indicator: str = None,
    start_year: int = None,
    end_year: int = None,
    database: Optional[str] = None,
    table: Optional[str] = None,
    save_path: Optional[str] = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> List[Dict]:
    """
    Downloads IMF WEO data for one or more vintages and optionally saves to file or database.
    Args:
        vintage (str or list[str]): The vintage string (e.g., 'April 2025') or list of such strings.
        save_path (str, optional): Path to save the WEO data as a file (by extension).
        database (str, optional): Path to the SQLite database file.
        table (str, optional): Name of the table to insert data into.
    Returns:
        List[Dict]: WEO records.
    Raises:
        Exception: If download or save/push fails.
    """
    if (database and not table) or (table and not database):
        raise ValueError("Both 'database' and 'table' must be provided together.")
    vintages = [vintage] if isinstance(vintage, str) else vintage
    all_records = []
    for v in vintages:
        a, b = v.split()
        if len(a) == 4:
            year, month = a, b
        elif len(b) == 4:
            year, month = b, a
        year = int(year)
        data = download_weo_data(year, month)
        records = parse_weo_data(
            data,
            f"{month} {year}",
            full_output=full_output,
            use_iso_alpha2=use_iso_alpha2,
            indicator=indicator,
            isos=isos,
            start_year=start_year,
            end_year=end_year,
        )
        all_records.extend(records)
    if database and table and all_records:
        with Database(database) as db:
            db.table(table).insert_many(
                rows=[tuple(r.values()) for r in all_records],
                columns=tuple(all_records[0].keys()),
                schema=None,
            )
    if save_path and all_records:
        # Check file format (.json, .csv, or .txt)
        file_format = save_path.lower().rsplit(".", 1)[-1]
        save_records(all_records, save_path, file_format)
    return all_records
