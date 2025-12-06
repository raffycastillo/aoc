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
lines = data.strip()
# FILE READ setup END

[intervals, _] = lines.split('\n\n')
intervals = sorted(list(map(lambda i: list(map(lambda n: int(n),i.split('-'))), intervals.split('\n'))))

merged_intervals = []
curr = intervals[0]
for i in range(1, len(intervals)):
    next = intervals[i]
    if curr[1] >= next[0]:
        curr[0] = min(curr[0], next[0])
        curr[1] = max(curr[1], next[1])
    else:
        merged_intervals.append(curr)
        curr = intervals[i]

if curr[1] == intervals[-1][1]:
    merged_intervals.append(curr)

res = 0

for interval in merged_intervals:
    res += interval[1] - interval[0] + 1

print('---')
print('out:')
print(res)

