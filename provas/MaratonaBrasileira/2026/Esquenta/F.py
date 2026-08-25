


n, p = map(int, (input().split()))

b = []
t = []

for i in range(n):
    bi, ti = map(int, (input().split()))
    b.append(bi)
    t.append(ti)


# pegar os candidatos com maior número de balões
baloes = -1
topB = []
topT = []

for i in range(n):
    if b[i] > baloes:
        baloes = b[i]
        topB = []
        topT = []
        topB.append(b[i])
        topT.append(t[i])

    elif b[i] == baloes:
        topB.append(b[i])
        topT.append(t[i])


# acho o menor tempo
menor = topT[0]
for i in range(1, len(topT)):
    if menor > topT[i]:
        menor = topT[i]

if baloes < p:
    print(f"{baloes + 1} {menor}")

else:
    print(f"{baloes} {menor - 1}")


