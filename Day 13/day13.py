import functools

div = [[[2]], [[6]]]
pairs = [[eval(p[0]), eval(p[1])] for p in [p.split('\n') for p in open('input.txt').read().split('\n\n')]]
pairs2 = [eval(p) for p in '\n'.join(open('input.txt').read().split('\n\n')).split('\n')]
pairs2.extend(div)


def compare(a, b):
    if type(a) != type(b):
        if type(a) is int:
            return compare([a], b)
        return compare(a, [b])

    if type(a) is int:
        if a < b:
            return -1
        if a > b:
            return 1      
        return 0
    
    for i in range(min(len(a), len(b))):
        ret = compare(a[i], b[i])
        if ret == 0:
            continue
        return ret

    return compare(len(a), len(b))

sum = 0
for i, p in enumerate(pairs):
    ret = compare(p[0], p[1])
    if ret == -1:
        sum += i + 1

pairs2.sort(key=functools.cmp_to_key(compare))
res = (pairs2.index(div[0]) + 1) * (pairs2.index(div[1]) + 1)

print(f'1. {sum}')
print(f'2. {res}')
