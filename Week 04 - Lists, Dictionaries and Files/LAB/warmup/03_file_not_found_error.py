
from pathlib import Path

file_path = Path(__file__).resolve().parent.parent.parent / "DEMO" / "records.txt"

with open(file_path) as f:
    print(f.read())
