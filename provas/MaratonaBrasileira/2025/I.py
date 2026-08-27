
def dist(a: list, b: list):
    if a[0] == b[0]:
        return abs(b[1] - a[1])
    return abs(b[0] - a[0])



def solver(lista, n):
    men, mai = 1, max(lista[1][1] - lista[0][1] -1 , lista[1][0] - lista[0][0] - 1)
    ans = -1

    def consegue(tentativa):

        orbita = tentativa

        for i in range(0, n - 1):

            if orbita >= dist(lista[i], lista[i+1]) :
                return False
            orbita = dist(lista[i], lista[i+1]) - orbita

        return True

    while men <= mai:
        mid = (men + mai) // 2

        if consegue(mid):
            ans = mid
            men = mid + 1

        else:
            mai = mid - 1

    return ans

n = int(input())

r = list()

for i in range(n):
    x, y = map(int, input().split())
    r.append([x, y])

print(solver(r, n))