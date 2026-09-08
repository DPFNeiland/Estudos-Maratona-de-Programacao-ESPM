
n = int(input())

l = list(map(int, input().split()))

soma = (1 + n) * n // 2

print(soma - sum(l))