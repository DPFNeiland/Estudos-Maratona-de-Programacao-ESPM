

n = int(input())

grafo = [[] for _ in range(n)]

for i in range(n):

    u, v = map(int, input().split())
    u -= 1
    v -= 1

    grafo[u].append(v)
    grafo[v].append(u)

resp = 1

for i in range(n):

    if len(grafo[i]) > 2:

        for j in range(len(grafo[i])):

            if len(grafo[j]) > 2:
                resp = grafo[i][j] + 1
                break

print(resp)