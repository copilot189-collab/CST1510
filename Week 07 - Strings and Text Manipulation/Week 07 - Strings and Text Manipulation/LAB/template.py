
# RECORD CHECK - Week 7
# Name: Enter your name
# Lane: IT
# Date: 09/11/2026


# SECTION 1: FUNCTIONS

def parse_line(raw_line):
    """Clean a messy server record into a dictionary."""
    parts = raw_line.strip().split(",")

    record = {"hostname": parts[0].strip().lower()}

    for part in parts[1:]:
        key, value = part.split("=", 1)
        record[key.strip().lower()] = float(value.strip())

    return record


def status_of(record):
    """Return a status based on server storage usage."""
    used = record["used"]
    total = record["total"]

    if total <= 0:
        return "INVALID"

    percentage = used / total * 100

    if percentage >= 100:
        return "OVER LIMIT"
    elif percentage >= 90:
        return "WARNING"
    else:
        return "OK"


# SECTION 2: INPUT RECORDS

raw_records = [
    "  Srv-01 , used=87 , total=100  ",
    "SRV-02,USED=120,TOTAL=100",
    " srv-03 , Used=45 , Total=100 ",
    "Srv-04, used=95,total=100",
    "  SRV-05 , USED=105 , TOTAL=100 ",
    "SRV-06,used=unknown,total=100"
]


# SECTION 3: PROCESS AND OUTPUT

total_records = 0
flagged_records = 0

for raw_record in raw_records:
    try:
        record = parse_line(raw_record)
        status = status_of(record)

        print(record)
        print("Status:", status)
        print()

        total_records += 1

        if status != "OK":
            flagged_records += 1

    except ValueError as error:
        print("Invalid record:", raw_record)
        print("Error:", error)
        print()


# SECTION 4: SUMMARY

print("RECORD CHECK SUMMARY")
print("Checked", total_records, "records.")
print(flagged_records, "records were flagged.")
