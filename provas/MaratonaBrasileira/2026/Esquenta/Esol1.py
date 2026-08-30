
def divisores(n):

    divisor = [1]

    for i in range(2, n//2 + 1):
        if n%i == 0:
            divisor.append(i)

    if n > 1:
        divisor.append(n)
    return divisor[::-1]

def teste(strings: list):
    n = len(strings)

    for i in range(n - 1):
        if strings[i] != strings[i + 1]:
            return False

    return True

def solve(s: str):

    n = len(s)

    divisor = divisores(n)

    for d in divisor:
        r = n//d

        left = 0
        right = r

        strings = [s[left:right]]

        for _ in range(d - 1):
            left = right 
            right = left + r
            strings.append(s[left:right])

        if teste(strings):
            return f"{d}\n{strings[0]}"

        strings = []

s = input()


print(solve(s))