import numpy as np
line = list(open('input.txt').read().strip())

quadrupel = []

for i in range(0, len(line) - 3):
    quadrupel = line[i:i+4]
    if len(np.unique(quadrupel)) == 4:
        print(f"1. {i + 4}")
        break

for i in range(0, len(line) - 13):
    quadrupel = line[i:i+14]
    if len(np.unique(quadrupel)) == 14:
        print(f"1. {i + 14}")
        break