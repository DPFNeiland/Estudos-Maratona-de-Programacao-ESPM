import random as r

res = r.randint(1, 1000)

while True:

    chute = int(input("Chute o número: "))

    if chute > res:
        print("o número é <")

    if chute < res:
        print("o número é >")

    if chute == res:
        print("acertou miseravi")
        break

