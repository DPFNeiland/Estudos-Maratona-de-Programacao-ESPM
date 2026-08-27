

def solve(n, m, a):
    

    for i in range(1, n):
        for j in range(m-1):

            if not (a[i][j] != a[i - 1][j] and a[i][j] != a[i][j+1]):
                return "N"
            
            if j == m-2:
                if not (a[i][j+1] != a[i-1][j+1]):
                    return "N"
    return "S" 

            

n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(str, input())))

print(solve(n, m, a))