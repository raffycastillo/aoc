import sys
# see: https://pypi.org/project/advent-of-code-data/
from aocd import get_data

if len(sys.argv) != 3:
    print("Usage: python get.py <year> <day>")
    print("Example: python get.py 2025 1")
    sys.exit(1)

year = int(sys.argv[1])
day = int(sys.argv[2])

data = get_data(day=day, year=year)
filename = f'{day:02d}.in'
with open(filename, 'w') as f:
    f.write(data)
print(f"Downloaded day {day} data to {filename}")

