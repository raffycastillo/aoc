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
lines: list[str] = data.strip().split('\n')
# FILE READ setup END

from functools import reduce

res = 0

buckets: list[list[int]] = [[] for _ in lines[0].split()]

# buckets, excluding the end
for line in lines[:-1]:
    for [i, val] in enumerate(line.split()):
        buckets[i].append(int(val))

for [i, op] in enumerate(lines[-1].split()):
    if op == '*':
        res += reduce(lambda acc, curr: acc*curr, buckets[i], 1)
    else:
        res += reduce(lambda acc, curr: acc+curr, buckets[i], 0)

print('---')
print('out:')
print(res)

