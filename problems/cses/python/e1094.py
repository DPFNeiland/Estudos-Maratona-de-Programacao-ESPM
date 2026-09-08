
n = int(input())
x = list(map(int, input().split()))

resp = 0
for i in range(1, n):

    if x[i] < x[i-1]:
        resp += x[i-1] - x[i]
        x[i]+= (x[i-1] - x[i])

print(resp)