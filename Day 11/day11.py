import re
import numpy as np
from copy import deepcopy

class monkey:
    def __init__(self, string):
        lines = string.split('\n')
        self.num = int(re.findall('\d', lines[0])[0])
        self.items = re.findall('\d+', lines[1])
        self.operation_string = lines[2].split('= ')[1]
        self.div = int(re.findall('\d+', lines[3])[0])
        self.iftrue = int(re.findall('\d+', lines[4])[0])
        self.iffalse = int(re.findall('\d+', lines[5])[0])
        self.items = [int(x) for x in self.items]
        self.count = 0

    def operation(self, index):
        old = self.items[index]
        new = eval(self.operation_string)
        self.items[index] = new
        return new

monkeys = [monkey(par) for par in open('input.txt').read().split('\n\n')]
monkeys2 = deepcopy(monkeys)

def get_business(monkeys, n, part2=False):
    modulus = np.prod([m.div for m in monkeys])
    for _ in range(0, n):
        for m in monkeys:
            for index, _ in enumerate(m.items):
                m.count += 1
                m.operation(index)

                if part2:
                    item = m.items[index] % modulus
                else:
                    item = m.items[index] // 3

                if item % m.div == 0:
                    monkeys[m.iftrue].items.append(item)
                else:
                    monkeys[m.iffalse].items.append(item)
            
            m.items = []
    
    counts = [m.count for m in monkeys]
    counts.sort()
    return counts[-1] * counts[-2]


print(f'1. {get_business(monkeys, 20)}')
print(f'2. {get_business(monkeys2, 10000, True)}')


