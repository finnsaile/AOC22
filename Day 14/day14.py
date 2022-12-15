import re
import math
from copy import deepcopy
paths = [p for l in open('input.txt').read().strip().split('\n') for n in [[int(num) for num in re.findall('\d+', l)]] for t in [list(zip(n[0::2], n[1::2]))] for p in list(zip(t[0::1], t[1::1]))]
max_depth = 0
filled = set()

for p in paths:
    for x in range(min(p[0][0], p[1][0]), max(p[0][0], p[1][0]) + 1):
        for y in range(min(p[0][1], p[1][1]), max(p[0][1], p[1][1]) + 1):
            filled.add((x, y))
    if max(p[0][1], p[1][1]) > max_depth:
        max_depth = max(p[0][1], p[1][1])
    

def sim(part2=False):
    loc_filled = deepcopy(filled)

    count = 0
    pos = (500, 0)

    while True:
        if not part2 and pos[1] > max_depth:
            break

        down = (pos[0], pos[1] + 1)
        left = (pos[0] - 1, pos[1] + 1)
        right = (pos[0] + 1, pos[1] + 1)

        if down[1] > (max_depth + 1):
            loc_filled.add(pos)
            count += 1
            pos = (500, 0)
            continue
        if down not in loc_filled:
            pos = down
        elif left not in loc_filled:
            pos = left
        elif right not in loc_filled:
            pos = right
        else:
            loc_filled.add(pos)
            count += 1
            if pos == (500, 0):
                break
            pos = (500, 0)
    
    return count

print(f'1. {sim()}')
print(f'2. {sim(True)}')
