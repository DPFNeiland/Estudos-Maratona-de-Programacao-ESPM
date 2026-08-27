

n, m, p, s = map(int, input().split())

rest = []
for i in range(m):
    rest.append(map(int, input().split()))

for mask in range(1 << n):
    validos = []
    for i in range(n):
        if mask & (1 << i):
            validos.append(n[i])

    if soma <= limite:
        validos.append(mask)

print(validos)