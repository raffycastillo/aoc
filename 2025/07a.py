# TEST FLAG setup
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--test', action='store_true', help='Use test input')
args = parser.parse_args()

problem_num = sys.argv[0].split('/')[-1][:2]
input_file = f'{problem_num}-test.in' if args.test else f'{problem_num}.in'
# TEST FLAG setup END

# FILE READ setup
input = open(input_file, 'r')
data = input.read()
input.close()
lines = data.strip().split('\n')
# FILE READ setup END

from typing import Optional
from collections import deque

res = 0

def fall(i: int, j: int, grid: list[list[str]]) -> Optional[list[int]]:
    while i < len(grid):
        if grid[i][j] == '^':
            return [i, j]
        i += 1
    return None

def list_int_to_str(list: list[int]) -> str:
    return ','.join([str(item) for item in list])

lines = list(map(lambda line: list(line), lines))
start = next((i for i, x in enumerate(lines[0]) if x == 'S'))
dq = deque([[0, start]])
split_points = set()


while len(dq) > 0:
    i, j = dq.popleft()
    next_point = fall(i, j, lines)
    if next_point is not None and list_int_to_str(next_point) not in split_points:
        res += 1
        split_points.add(list_int_to_str(next_point))
        next_i, next_j = next_point
        dq.append([next_i, next_j-1])
        dq.append([next_i, next_j+1])


print('---')
print('out:')
print(res)

