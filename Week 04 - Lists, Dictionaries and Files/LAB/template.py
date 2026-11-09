"""RECORD CHECK - Week 4 mini-project (Excellent level).

Reads label,value,limit rows from records.txt, prints a report for each,
and writes label,status rows to results.txt.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def check_record(value, limit):
    """Return the difference, percentage, and status of a record."""
    difference = value - limit
    percent = (value / limit) * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print a formatted report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Value       : {value:>10.2f}")
    print(f"  Limit       : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Of limit    : {percent:>9.1f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


def load_records(path):
    """Read label,value,limit lines and return a list of dictionaries."""
    records = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue
            label, value, limit = line.strip().split(",")
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit),
            })
    return records


def main():
    """Process records, print reports, and save statuses."""
    records = load_records(BASE_DIR / "records.txt")
    over_limit_count = 0

    with open(BASE_DIR / "results.txt", "w", encoding="utf-8") as output_file:
        for record in records:
            difference, percent, status = check_record(
                record["value"], record["limit"]
            )
            print_report(
                record["label"], record["value"], record["limit"],
                difference, percent, status
            )
            output_file.write(f'{record["label"]},{status}\n')
            if status == "OVER LIMIT":
                over_limit_count += 1

    print(f"Checked {len(records)} records. {over_limit_count} were over limit.")
    print("Results saved to results.txt")


if __name__ == "__main__":
    main()
