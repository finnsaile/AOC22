import numpy as np


lines = open("input.txt").read()
sums = []
for elf in lines.split("\n\n"):
    sum = 0
    for num in elf.split("-"):
        sum += int(num)

    sums.append(sum)
    
sums.sort()
print(f"1. {sums[-1]}")
print(f"2. {np.array(sums[-3:]).sum()}")
