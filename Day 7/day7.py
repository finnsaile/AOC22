import re

lines = [line for line in open("input.txt").read().strip().split("\n")]

dirs = []
total = 0
cl = 0

def get_size(cl):
    global dirs, total
    sum = 0

    while cl < len(lines):
        if re.search('\d+', lines[cl]) != None:
            sum += int(lines[cl].split(' ')[0])
            
        elif lines[cl] == '$ cd ..':
            break
        
        elif re.search('\$\scd', lines[cl]) != None:
            cl, new_s = get_size(cl + 1)
            sum += new_s
        
        cl += 1

    if sum <= 100000:
        total += sum
    dirs.append(sum)
    return cl, sum


needed = -40000000 + get_size(0)[1]
dirs.sort()

print(f'1. {total}')
for x in dirs:
    if x > needed:
        print(f'2. {x}')
        break
