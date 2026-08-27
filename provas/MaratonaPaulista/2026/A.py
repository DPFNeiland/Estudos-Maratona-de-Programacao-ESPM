
baladas = []
grupos = []
n, q = map(int, input().split())

# Preco, musica e i
auxiliar = []


# baladas
for _ in range(n):
    baladas.append(list(map(int, input().split())))

for _ in range(q):
    grupos.append(list(map(int, input().split())))

# preencher o auxiliar
aux = 1
auxiliar.append([baladas[0][0], baladas[0][1],0])
for i in range(1, n):
    print(f"{baladas[i][0]} == {auxiliar[-1][0]}" )
    if baladas[i][0] == auxiliar[-1][0] and aux == 1:
        aux = 0
        auxiliar.append([baladas[i][0], baladas[i][1], i])

    elif baladas[i][0] < auxiliar[-1][0]:
        auxiliar.append([baladas[i][0], baladas[i][1], i])
        aux = 1

# busca binária
maiorFesta = n - 1
menorFesta = 0
meio = -1
for i in range(q):


    while True:
        meio = (maiorFesta + menorFesta)//2

        if grupos[i][0] > auxiliar[meio][0]:
            menorFesta = (maiorFesta + menorFesta)//2 + 1

        elif grupos[i][0] < auxiliar[meio][0]:
            maiorFesta = (maiorFesta + menorFesta)//2 - 1

        else:
            # achei sua respectiva festa
            print(auxiliar[meio][2])
            break

print(auxiliar)