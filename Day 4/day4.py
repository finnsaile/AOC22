import re

pattern = re.compile('\d+')

quadruplets = [pattern.findall(line) for line in open("input.txt").read().strip().split("\n")]
sum1 = sum2 = 0
for q in quadruplets:
    q = [int(x) for x in q]
    if (q[0] >= q[2] and q[1] <= q[3]) or (q[2] >= q[0] and q[3] <= q[1]):
        sum1 += 1
    
    if (q[1] >= q[2]) and (q[3] >= q[0]):
        sum2 += 1

print(f"1. {sum1}")
print(f"2. {sum2}")
