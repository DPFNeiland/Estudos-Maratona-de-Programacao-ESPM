

n = int(input())

resp = []

auxC = 0
auxV = 0
for i in range(n):
    c, v = map(int, input().split())
    # preencher o resposta:
    auxC += c
    auxV += v

    In = (auxC - auxV)/(auxC + auxV)
    if In > 0:
        resp.append("COMPRA")
    elif In < 0:
        resp.append("VENDA")
    else:
        resp.append("NEUTRO")

q = int(input())
for i in range(q):
    qi = int(input()) - 1
    print(resp[qi])