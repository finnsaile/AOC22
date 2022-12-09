forest = [[i for i in list(map(int, list(row)))] for row in open('input.txt').read().strip().split('\n')]

def get_scenic_score(x, y):
    global forest
    top = bot = right = left = 0
    height = forest[y][x]

    for i in range(y - 1, -1, -1):
        top += 1
        if forest[i][x] >= height:
            break

    for i in range(y + 1, len(forest)):
        bot += 1
        if forest[i][x] >= height:
            break
        
    for i in range(x - 1, -1, -1):
        left += 1
        if forest[y][i] >= height:
            break

    for i in range(x + 1, len(forest[0])):
        right += 1
        if forest[y][i] >= height:
            break

    return top * bot * right * left

def is_visible(x, y):
    global forest
    top = bot = left = right = True
    height = forest[y][x]

    for i in range(0, y):
        if forest[i][x] >= height:
            top = False
    
    for i in range(len(forest) - 1, y, -1):
        if forest[i][x] >= height:
            bot = False

    for i in range(0, x):
        if forest[y][i] >= height:
            left = False
    
    for i in range(len(forest[0]) - 1, x, -1):
        if forest[y][i] >= height:
            right = False
    
    return top | bot | left | right

counter = 0
max_s = 0

for i in range(0, len(forest)):
    for j in range(0, len(forest[0])):
        if is_visible(j, i):
            counter += 1
        if get_scenic_score(j, i) > max_s:
            max_s = get_scenic_score(j, i)

print(f'1. {counter}')
print(f'2. {max_s}')
