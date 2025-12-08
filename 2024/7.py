input = open('7a.in', 'r')
data = input.read()
input.close()
lines = data.strip().split('\n')


# P1 algo or something
# for each line:
#   apply + to all spots
#   if result is greater than, invalid so just skip
#   if result is equal, valid so add to sum
#   if result is less than:
#     // this is the challenge, how do u generate all possible mult spots?
#     // m^2 where n refers to each spot? so if a line has n numbers, there's m "spots"
#     // easier said thatn done!
#     for each +, try all possible combinations of * replacement:
#       same criteria applies as above

# so 2^m permutations of operators
# where m is n-1 and n is number of ints in array

# for m = 3 => 8
# 0 0 0
# 1 0 0
# 0 1 0
# 0 0 1
# 1 1 0
# 1 0 1
# 0 1 1
# 1 1 1

# for m = 5 => 26
# 0 0 0 0 0
# 1 0 0 0 0
# 0 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 0
# 0 0 0 0 1
# 1 1 0 0 0
# 1 0 1 0 0
# 1 0 0 1 0
# 1 0 0 0 1
# 0 1 1 0 0
# 0 1 0 1 0
# 0 1 0 0 1
# 0 0 1 1 0
# 0 0 1 0 1
# 0 0 0 1 1
# 1 1 1 0 0
# 1 1 0 1 0
# 1 1 0 0 1
# 1 0 1 1 0
# 1 0 1 0 1
# 1 0 0 1 1
# 0 1 1 1 0
# 0 1 1 0 1
# 0 1 0 1 1
# 0 0 1 1 1


def calc(operations, values, target):
    # print()
    print(operations)
    final = int(values[0])
    # print(f'current target is {target}')
    # while we don't match final val and we haven't tried all combinations... the last of which should be that if all operations are mults???
    for i in range(len(operations)):
        if operations[i] == 0:
            # print(f'adding {final} to {int(values[i+1])}')
            final += int(values[i+1])
        else:
            # print(f'multing {final} to {int(values[i+1])}')
            final *= int(values[i+1])
    # print(f'final: {final}, target: {target}')
    if final < target:
        return [1, final] # move to next permutation
    if final > target:
        return [-1, final] # exceeded target, invalid line
    return [0, final] # found

    # this returns -1, 0, 1
    # -1 if final val < target
    #  0 if final val == target
    #  1 if final val > target

def rec(operations, values, target):
    if len(operations) <= 0:
        return -1
    res1 = calc(operations, values, target)
    operations[0] = 1
    res2 = calc(operations, values, target)
    # print(res1,res2)
    if res1[0] == 0 or res2[0] == 0:
        return 0
    final1, final2 = 2,2
    if res1[0] == 1:
        # print(f'+ recursion: {target-int(values[0])}')
        final1 = rec(operations[1:], values[1:], target-int(values[0]))
    if res2[0] == 1:
        # print(f'* recursion: {target/int(values[0])}')
        # so sometimes you want to process two at a time for mult but then how do you retain the previous value for the next recursive step?
        values[1] = values[0] * values[1]
        final2 = rec(operations[1:], values[1:], target-int(values[0]))
    return min(abs(final1), abs(final2))


p1 = 0
count = 0
for line in lines:
    print()
    # count += 1
    # if count >= 2:
    #     break
    # extract final res, and get array of nums
    values = line.split(' ')
    # separate the final val and the accumulators
    final = int(values[0][:-1])
    # print(final)
    values = values[1:]
    # print(values)
    # now applying + to all spots. how do i do it?
    # what if we setup an array that indicates whether we + or mult?
    # operation[i] determines the operation between values[i] and values[i+1]
    operations = [0 for _ in range(len(values)-1)]
    # make a recursive call here somehow?
    print(f'starts with {operations}')
    res = rec(operations, values, final)

    if res == 0:
        print(line.split(' '))
        print('added to p1 sum')
        p1 += final

print(p1)
