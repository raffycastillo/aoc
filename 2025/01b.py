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

res = 0
pos = 50

for r in lines:
    dir, val = r[:1], r[1:]
    print('---')
    print(f'pos: {pos}, rot: {r}')

    if dir == 'L':
        if pos == 0:
            res += int(val) // 100
        elif int(val) >= pos:
            res += 1 + (int(val) - pos) // 100
        pos = (pos - int(val)) % 100
    else:
        if int(val) >= 100 - pos:
            res += 1 + (int(val) - (100 - pos)) // 100
        pos = (pos + int(val)) % 100

    print('this iter:', res, pos)

print('---')
print('finally: ', res,pos)

