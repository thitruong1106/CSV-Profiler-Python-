import csv
from collections import Counter
from typing import List, Dict, Any, Optional, Tuple


DEFAULT_MISSING_TOKENS = {"", "na", "n/a", "null", "none"} 


def load_csv(path: str) -> List[Dict[str, str]]:
    """
    Load a CSV file into a list of dictionaries.

    Returns:
        List[Dict[str, str]]: rows (empty list if file is empty or can't be read)
    """
    try:
        with open(path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            if not rows:
                print("Empty file (no data rows).")
            return rows
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []


def is_missing(value: Any, missing_tokens: set) -> bool: #function returns true or false. Simply saying, True if value is missing, False if not 
    """
    Check if a value should be considered missing based on None status or predefined missing tokens.

    This function determines whether a given value represents missing data by checking:
    1. If the value is None
    2. If the value is a string that, when cleaned (stripped and lowercased),
    matches any token in the provided set of missing tokens.

    Parameters
    ----------
    value : Any
        The value to check for missing status. Can be any Python object.
    missing_tokens : set
        A set of string tokens that represent missing values when encountered.
        String values are case-insensitively compared after stripping whitespace.

    Returns
    -------
    bool
        True if the value is considered missing (either None or a string matching
        a missing token), False otherwise.

    Examples
    --------
    >>> missing_tokens = {'na', 'n/a', 'null', ''}
    >>> is_missing(None, missing_tokens)
    True
    >>> is_missing('NA', missing_tokens)
    True
    >>> is_missing('valid data', missing_tokens)
    False
    """
    if value is None:
        return True
    if isinstance(value, str):
        cleaned = value.strip().lower()
        return cleaned in missing_tokens #is the cleaned value, one of the known missing values
    return False #safe default for any value that doesnt match known missing case, since value is not none and not a missing string token, treated as valid data. 


def profile_columns(rows: List[Dict[str, Any]],missing_tokens: Optional[set] = None) -> List[Dict[str, Any]]:
    """
    Build a profiling report per column.

    Returns:
        List of dicts, one per column, containing summary stats.
    """
    if not rows:
        return []

    if missing_tokens is None:
        missing_tokens = DEFAULT_MISSING_TOKENS

    columns = list(rows[0].keys())
    total_rows = len(rows)

    report = []

    for col in columns:
        values = []
        missing_count = 0

        for row in rows:
            v = row.get(col)
            if is_missing(v, missing_tokens): #true, + missing 
                missing_count += 1
            else:
                values.append(v.strip() if isinstance(v, str) else v)

        counter = Counter(values)
        top_values: List[Tuple[Any, int]] = counter.most_common(3)

        non_missing_count = total_rows - missing_count
        missing_percent = (missing_count / total_rows) * 100

        report.append({
            "column": col,
            "total_rows": total_rows,
            "missing_count": missing_count,
            "non_missing_count": non_missing_count,
            "missing_percent": round(missing_percent, 1),
            "unique_count": len(counter),
            "top_values": top_values,
        })

    return report


def print_profile(report: List[Dict[str, Any]]) -> None:
    """
    Docstring for print_profile
    
    :param report: Description
    :type report: List[Dict[str, Any]]
    """
    if not report:
        print("No rows found (nothing to profile).")
        return

    for col_report in report:
        print("-" * 40)
        print(f"Column: {col_report['column']}")
        print(f"Total rows: {col_report['total_rows']}")
        print(f"Missing count: {col_report['missing_count']}")
        print(f"Non-missing count: {col_report['non_missing_count']}")
        print(f"Missing %: {col_report['missing_percent']}%")
        print(f"Unique values (non-missing): {col_report['unique_count']}")

        if col_report["top_values"]:
            print("Top values:")
            for i, (value, count) in enumerate(col_report["top_values"], start=1):
                print(f"  {i}. '{value}' — {count}")
        else:
            print("Top values: (none)")


if __name__ == "__main__":
    path = input("Enter path: ")
    rows = load_csv(path)
    report = profile_columns(rows)
    print_profile(report)
