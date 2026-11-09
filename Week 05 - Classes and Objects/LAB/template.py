"""Week 5 Record Check mini-project: IT lane, Excellent level."""
from pathlib import Path

class Record:
    """Store a server record and calculate its status."""

    def __init__(self, label, value, limit):
        """Store this record's label, value and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on percentage of the limit used."""
        percent = self.value / self.limit * 100
        if percent >= 100:
            return "OVER LIMIT"
        if percent >= 90:
            return "WARNING"
        return "OK"


def load_records(path):
    """Load comma-separated records into a list of Record objects."""
    records = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records


def main():
    """Print reports for all records and count over-limit results."""
    records = load_records(Path(__file__).resolve().parent / "records.txt")
    over_limit_count = 0
    for record in records:
        status = record.status()  # Call status() exactly once per record.
        print()
        print("=" * 34)
        print(f"  RECORD CHECK  -  {record.label}")
        print("=" * 34)
        print(f"  Value       : {record.value:>10.2f}")
        print(f"  Limit       : {record.limit:>10.2f}")
        print(f"  Status      : {status:>10}")
        print("=" * 34)
        if status == "OVER LIMIT":
            over_limit_count += 1
    print(f"Checked {len(records)} records. {over_limit_count} were over limit.")


if __name__ == "__main__":
    main()
