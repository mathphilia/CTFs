with open('case(N=1000).txt') as f:
    A = [*map(int, f.read().split())]

count = [1] + [0] * 1023
for a in A:
    if a<=500:
        count_new = [count[i ^ a] for i in range(1024)]
    else:
        count_new = [count[i ^ a] + count[i ^ (1000 - a)] for i in range(1024)]
    count = [c % (10 ** 9 + 7) for c in count_new]

for c in count:
    if c:
        print('FLAG{' + str(c) + '}')
        break