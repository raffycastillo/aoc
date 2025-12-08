
import copy

input = open('6.in', 'r')
data = input.read()
input.close()
lines = data.strip().split('\n')

lines = [list(line) for line in lines]

start = tuple()
for i,iVal in enumerate(lines):
    for j,jVal in enumerate(iVal):
        if jVal == '^':
            start = (i,j)
            lines[i][j] = '.'
            break

# determine the face by doing some mod 0,1,2,3
# iterate using the face until roadblock
# rotate the face and iterate again
# only stops until you hit the edge of the matrix
# return how many total steps/iterations you made

# edge validation
# returns -1,-1 if invalid
# given input is 130x130 ill just hardcode it
def returnAhead(point, dir): 
    finalDir = dir % 4
    # 0 is up
    # 1 is right
    # 2 is down
    # 3 is left

    # move next point according to dir
    if finalDir == 0:
        i,j = point[0]-1, point[1] # go up 1 unit
    elif finalDir == 1:
        i,j = point[0], point[1]+1 # go right 1 unit
    elif finalDir == 2:
        i,j = point[0]+1, point[1] # go down 1 unit
    else: # finalDir == 3:
        i,j = point[0], point[1]-1 # go left 1 unit

    # validate the point and return accordingly
    if i >= 0 and i <= 129 and j >= 0 and j <= 129:
        return (i,j)
    return (-1,-1)

visited = set()
dir = 0
p1start = start
next = returnAhead(p1start,dir)
while next != (-1,-1):
    if lines[next[0]][next[1]] == '.':
        p1start = next
        next = returnAhead(p1start, dir)
    else: # lines[next[0]][next[1]] == '#'
        dir += 1
        next = returnAhead(p1start, dir)
    visited.add(p1start)
p1 = len(visited)
print(p1)

# how the do i do p2...
p2 = 0
# print(visited)
# for point in visited:
#     revisited = set() 
#     newLines = copy.deepcopy(lines)
#     newLines[point[0]][point[1]] = '#'
#     p2start = start
#     dir = 0
#     next = returnAhead(p2start, dir)
    # while next != (-1,-1):
    #     if newLines[next[0]][next[1]] == '.':
    #         p2start = next
    #         next = returnAhead(p2start, dir)
    #     else: # lines[next[0]][next[1]] == '#'
    #         dir += 1
    #         next = returnAhead(p2start, dir)
    #     revisited.add(p2start)
print(p2)
