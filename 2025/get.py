# make my own ? that would be a fun little homework
# https://pypi.org/project/advent-of-code-data/
from aocd import get_data

data = get_data(day=1, year=2025)
input = open('1.in', 'a')
input.write(data)
input.close()

