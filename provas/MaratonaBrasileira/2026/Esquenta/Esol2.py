s = input().strip()

n = len(s)

pi = [0] * n

for i in range(1, n):
    j = pi[i - 1]

    while j > 0 and s[i] != s[j]:
        j = pi[j - 1]

    if s[i] == s[j]:
        j += 1

    pi[i] = j

periodo = n - pi[-1]

if n % periodo == 0:
    r = s[:periodo]
    m = n // periodo
else:
    r = s
    m = 1

print(m)
print(r)