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

from functools import reduce

res = 0

# getting length of each column
op_buckets = []
length = 1
for [i, op] in enumerate(lines[-1][1:]):
    # print(i, op)
    if op == ' ':
        length += 1
    else:
        op_buckets.append(length-1)
        length = 1

op_buckets.append(4) # LMAOOO hardcode 3 for test input 4 for actual
print(f'len of all lines besides last: {len(list(lines[0].split()))}')
print(f'len of last line: {len(list(lines[-1].split()))}')

buckets = [['' for _ in range(op_buckets[i])] for [i, _] in enumerate(lines[0].split())]
# buckets, excluding the end
for line in lines[:-1]:
    line_ptr = 0
    n = 0
    while line_ptr < len(line):
        curr = line[line_ptr:line_ptr+op_buckets[n]]
        for [i, char] in enumerate(curr):
            # print(buckets[n][i])
            buckets[n][i] += char
            # print(n,i)
            # print(buckets[n])

        line_ptr += op_buckets[n]+1
        n += 1

# print(buckets)
# print(op_buckets)

def process(int_str: str, op: str) -> int:
    stripped_str = int_str.strip()

    if len(stripped_str) == 0:
        if op == '*':
            return 1
        else:
            return 0
    
    return int(stripped_str)

for [i, op] in enumerate(lines[-1].split()):
    if op == '*':
        res += reduce(lambda acc, curr: acc*process(curr, '*'), buckets[i], 1)
    else:
        res += reduce(lambda acc, curr: acc+process(curr, '+'), buckets[i], 0)

print('---')
print('out:')
print(res)

