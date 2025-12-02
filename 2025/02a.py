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

    i = left
    while i <= right:
        strI = str(i)
        leftS, rightS = strI[:len(strI) // 2], strI[len(strI) // 2:]

        if (leftS == rightS):
            res += int(i)
            print('adding to res: ', int(i))

        i += 1

print('---')
print('out:')
print(res)

