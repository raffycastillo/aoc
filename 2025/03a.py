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

for line in lines:
    print('---')
    print('for line:')
    print(line)

    left, right = 0, 1
    line = [int(char) for char in line]
    
    max_jolt = line[left]*10 + line[right]
    while right < len(line)-1:
        if line[left] < line[right]:
            left = right
            right = left+1
        else:
            right = right+1
        
        curr = line[left]*10 + line[right]
        max_jolt = max(max_jolt, curr)
    
    res += max_jolt
    print('added: ', max_jolt)

print('---')
print('out:')
print(res)

