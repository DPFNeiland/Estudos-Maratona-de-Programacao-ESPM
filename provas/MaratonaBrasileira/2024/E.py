

n = int(input())
k = []

for i in range(n):
    k.append(list(map(int, input().split())))


if k[0][0] < k[0][1] and k[0][0] < k[1][0]:
    print("0") 

elif k[0][0] > k[0][1] and k[0][0] < k[1][0]:
    print("1")

elif k[0][0] > k[0][1] and k[0][0] > k[1][0]:
    print("2")

else:
    print("3")