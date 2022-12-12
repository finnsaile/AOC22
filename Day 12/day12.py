import heapq
import numpy as np
from copy import deepcopy

field = np.array([list(l) for l in open('input.txt').read().strip().split('\n')])

class node:
    def __init__(self, pos, dist, height):
        self.pos = pos
        self.dist = dist
        self.height = height
    
    def __repr__(self):
        return f'Node value: {self.pos}, {self.dist}'

    def __lt__(self, other):
        return self.dist < other.dist
    
    def __eq__(self, other):
        return self.pos == other.pos


def get_dist(start, end, field):
    field = deepcopy(field)
    field[end] = 'z'

    heap = [node(s, 0, 'a') for s in start]
    heapq.heapify(heap)

    visited = []
    
    while True:
        try:
            cur = heapq.heappop(heap)
        except IndexError:
            break

        for i in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_pos = (cur.pos[0] + i[0], cur.pos[1] + i[1])
            if new_pos[0] not in range(0, len(field)) or new_pos[1] not in range(0, len(field[0])):
                continue

            new_node = node(new_pos, cur.dist + 1, field[new_pos[0], new_pos[1]])

            if (ord(new_node.height) - ord(cur.height) < 2) and new_node not in visited:
                visited.append(new_node)
                heapq.heappush(heap, new_node)
    
    return [v.dist for v in visited if v.pos == end][0]


start = list(zip(*np.where((field == 'S'))))
end = list(zip(*np.where(field == 'E')))[0]
print(f'1. {get_dist(start, end, field)}')

starts = list(zip(*np.where((field == 'a') | (field == 'S'))))
print(f'2. {get_dist(starts, end, field)}')