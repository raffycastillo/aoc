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
lines_raw = data.strip().split('\n')
# FILE READ setup END

# convert to 2d arr
lines = [list(line) for line in lines_raw]

dirs = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
]

def check(row: int, col: int, max_row: int, max_col: int, arr: list[list[str]]) -> bool:
    count = 0
    for [dr, dc] in dirs:
        new_row = row+dr
        new_col = col+dc

        valid_row = True if new_row >= 0 and new_row <= max_row else False
        valid_col = True if new_col >= 0 and new_col <= max_col else False

        if valid_row and valid_col and arr[new_row][new_col] == '@':
            count += 1
    
    return count < 4

res = 0
while True:
    local_res = res
    removes: list[list[int]] = []

    for [r, line] in enumerate(lines):
        for [c, char] in enumerate(line):
            if char == '.':
                continue

            if check(r, c, len(lines)-1, len(line)-1, lines):
                removes.append([r, c])
                res += 1

    for [r, c] in removes:
        lines[r][c] = '.'

    if local_res == res:
        break
    

print('---')
print('out:')
print(res)

