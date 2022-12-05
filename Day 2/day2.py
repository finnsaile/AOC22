import numpy as np

rounds = [line.split(" ") for line in open("input.txt").read().strip().split("\n")]

sum1 = 0
sum2 = 0

# calc shape value using offset
def shape_val(x):
    return ord(x) - ord('A') + 1

# dirs showing what to chose if you want to win/lose
win_dict = {'A' : 'B', 'B' : 'C', 'C' : 'A'}
lose_dict = {v : k for k, v in win_dict.items()}

for r in rounds:
    # transpose X, Y, z to A, B, C
    r[1] = chr(ord(r[1]) - (ord('X') - ord('A')))
    # add shape val
    sum1 += shape_val(r[1])
    # if draw add 3
    if r[0] == r[1]:
        sum1 += 3
    # if win add 6
    elif win_dict[r[0]] == r[1]:
        sum1 += 6

    # if win get win shape
    if r[1] == 'C':
        sum2 += shape_val(win_dict[r[0]]) + 6
    elif r[1] == 'B':
        sum2 += shape_val(r[0]) + 3
    # if lose get lose shape
    else:
        sum2 += shape_val(lose_dict[r[0]])


print(f"1. {sum1}")
print(f"2. {sum2}")
