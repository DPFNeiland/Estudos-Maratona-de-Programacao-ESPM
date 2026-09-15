mod = 1000000007

def fatorial(n: int):

    resp = 1
    for i in range(2, n + 1):
        resp *= i


    return resp

n, k = map(int, input().split())

print((fatorial(n) % mod * pow(fatorial(k),mod - 2, mod) % mod * pow(fatorial(n-k),mod -2, mod) % mod) % mod)