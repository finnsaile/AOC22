import numpy as np

def get_sum(list):
    sum = 0
    for c in list:
        num = ord(c)
        if c.isupper():
            sum += num - 38
        else:
            sum += num - 96
    return sum

inp = open('input.txt').read().strip().split('\n')

backpacks = [(l[:len(l) // 2], l[len(l) // 2:]) for l in inp]
backpacks2 = [inp[n:n+3] for n in range(0, len(inp), 3)]
c_list = []
c_list2 = []

for b in backpacks:
    c_list.append(np.unique([c for c in b[0] if c in b[1]]).item())

for b in backpacks2:
    c_list2.append(np.unique([c for c in b[0] if c in b[1] and c in b[2]]).item())

print(f"1. {get_sum(c_list)}")
print(f"2. {get_sum(c_list2)}")
