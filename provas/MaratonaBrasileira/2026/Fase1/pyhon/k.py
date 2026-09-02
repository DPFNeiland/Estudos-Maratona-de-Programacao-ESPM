
def solve(c, k):
    resp = -1
    soma =  0
    for i in range(n):
        soma += c[i]


    for i in range(n):
        if k[i] > c[i]:
            return -1

        resp = max(resp, soma - c[i] +k[i] )
    return resp

n = int(input())

soma = 0
c = list(map(int, input().split()))
k = list(map(int, input().split()))


print(solve(c, k))