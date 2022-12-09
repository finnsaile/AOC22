line = list(open('input.txt').read().strip())

for i in range(0, len(line) - 3):
    quadrupel = line[i:i+4]
    if len(set(quadrupel)) == 4:
        print(f"1. {i + 4}")
        break

for i in range(0, len(line) - 13):
    quadrupel = line[i:i+14]
    if len(set(quadrupel)) == 14:
        print(f"1. {i + 14}")
        break

# oneline solution
[print(f'{x + 1}. {[i + y for i in range(0, len(line) - y - 1) if len(set(line[i:i + y])) == y][0]}') for (x, y) in enumerate([4, 14]) for line in [list(open('input.txt').read().strip())]]
