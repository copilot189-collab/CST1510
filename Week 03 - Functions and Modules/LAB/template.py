"""Record Check mini-project | Week 3 | IT lane.

Enter a hostname, GB used and GB total. Type quit to finish.
"""

def status_of(percent):
    """Return the status based on the percentage used."""
    if percent >= 100:
        return "OVER LIMIT"
    if percent >= 90:
        return "WARNING"
    return "OK"


def check(value, limit):
    """Return the difference and percentage for a record."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Display a bordered report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used        : {value:>10.2f}")
    print(f"  Total       : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Of limit    : {percent:>9.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)
    print()


def main():
    """Check records until quit and report how many exceeded the limit."""
    over_count = 0
    while True:
        label = input("Hostname (or 'quit'): ").strip()
        if label.lower() == "quit":
            break
        value = float(input("GB used: "))
        limit = float(input("GB total: "))
        difference, percent = check(value, limit)
        status = status_of(percent)
        if status == "OVER LIMIT":
            over_count += 1
        print_report(label, value, limit, difference, percent, status)
    print(f"Records OVER LIMIT: {over_count}")


if __name__ == "__main__":
    main()