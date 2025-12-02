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
lines = data.strip().split(',')
# FILE READ setup END

res = 0

for r in lines:
    left, right = map(lambda x: int(x), r.split('-'))
    print('---')
    print('processing range: ', left, '-', right)

    curr = left
    while curr <= right:
        currStr = str(curr)
        halfLen = (len(currStr) // 2) + 1

        for i in range(1, halfLen):
            base, remaining = currStr[:i], currStr[i:]

            if len(remaining) % i != 0:
                continue

            flag = True
            for r in range(0, len(remaining), i):
                chunk = remaining[r:r+i]
                if base != chunk:
                    flag = False
                    break

            if flag:
                print('adding: ', curr)
                print('compared: ', base, '-', remaining)
                res += curr
                break

        curr += 1

print('---')
print('out:')
print(res)

