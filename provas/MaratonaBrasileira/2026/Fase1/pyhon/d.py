def ele_mesmo(mapa: list[list], inverso: list[list], n, m):
    for i in range(n):
        for j in range(m):
            if mapa[i][j] != inverso[i][j]:
                return False

    return True

def cabeca_pra_baixo(mapa: list[list], inverso: list[list], n, m):
    inversa = inverso[::-1]

    for i in range(n):
        for j in range(m):
            if mapa[i][j] != inversa[i][j]:
                return False

    return True

def cabeca_gira_90(mapa: list[list], inverso: list[list], n, m):
    for i in range(n):
        for j in range(m):
            if mapa[i][j] != inverso[n-j-1][i]:
                return False
            
    return True
        
def cabeca_gira_menos_90(mapa: list[list], inverso: list[list], n, m):
    for i in range(n):
        for j in range(m):
            if mapa[i][j] != inverso[j][n-i-1]:
                return False

    return True

def inversor(mapa: list[list], n, m):
    inversa = []
    for i in range(n):
            inversa.append(mapa[i][::-1])

    return inversa

def solve(mapa: list[list], n, m):
    resp = 1
    inversa = inversor(mapa, n, m)

    if ele_mesmo(mapa, inversa, n, m):
        resp += 1


    if cabeca_pra_baixo(mapa, mapa, n, m):
        resp += 1

    if cabeca_pra_baixo(mapa, inversa, n, m):
        resp += 1


    if n == m:
        if cabeca_gira_90(mapa, mapa, n, m):
            resp += 1

        if cabeca_gira_90(mapa, inversa, n, m):
            resp += 1

        if cabeca_gira_menos_90(mapa, mapa, n, m):
            resp += 1

        if cabeca_gira_menos_90(mapa, inversa, n, m):
            resp += 1


    return resp

n, m = map(int, input().split())

mapa = []
for _ in range(n):
    mapa.append(list(input()))

print(solve(mapa, n, m))