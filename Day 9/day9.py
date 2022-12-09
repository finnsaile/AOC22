commands = [l.split(' ') for l in open('input.txt').read().strip().split('\n')]

def are_adj(a, b):
    if abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1:
        return True
    return False

def get_move(head, tail):
    out = [0, 0]
    if head[0] > tail[0]:
        out[0] = 1
    if head[0] < tail[0]:
        out[0] = -1
        
    if head[1] > tail[1]:
        out[1] = 1
    if head[1] < tail[1]:
        out[1] = -1

    return tuple(out)


def get_visited(knots):
    dir_dict = {'U' : (0, 1), 'D' : (0, -1), 'L' : (-1, 0), 'R' : (1, 0)}
    visited = set()
    for c in commands:
        for i in range(int(c[1])):
            knots[0] = tuple(map(sum, zip(knots[0], dir_dict[c[0]])))
            for i in range(len(knots) - 1):
                if not are_adj(knots[i], knots[i + 1]):
                    knots[i + 1] = tuple(map(sum, zip(knots[i + 1], get_move(knots[i], knots[i + 1]))))

            visited.add(knots[-1])
    
    return len(visited)


print(f'1. {get_visited([(0,0)] * 2)}')
print(f'2. {get_visited([(0,0)] * 10)}')
