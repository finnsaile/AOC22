import numpy as np
import re


pattern = re.compile('\d+')

with open('input.txt') as f:
    stacks = []
    stacks2 = []
    cargo = np.zeros((9, 36), dtype=object)
    for i in range(0, 9):
        s = f.readline()
        cargo[i] = list(s)
    
    for (i, x) in enumerate(cargo[-1]):
        if x[-1] != ' ' and x[-1] != '\n':
            c = np.flip(cargo[: , i])
            c = c[(c != ' ') & (c != '\n')]
            stacks.append(list(c))
            stacks2.append(list(c))

    f.readline()

    lines = f.readlines()

    for l in lines:
        nums = pattern.findall(l)

        for i in range(0, int(nums[0])):
            stacks[int(nums[2]) - 1].append(stacks[int(nums[1]) - 1].pop())

        stacks2[int(nums[2]) - 1].extend(stacks2[int(nums[1]) - 1][-int(nums[0]):])
        del stacks2[int(nums[1]) - 1][-int(nums[0]):]

    out = []
    out2 = []
    for s in stacks:
        out.append(s[-1])
    for s in stacks2:
        out2.append(s[-1])
    
    print(f"1. {''.join(out)}")
    print(f"2. {''.join(out2)}")

    

        

 