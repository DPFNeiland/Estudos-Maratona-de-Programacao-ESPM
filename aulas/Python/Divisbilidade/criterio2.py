
def resto_decimal(s, d):
    resto = 0

    for c in s:
        resto = (resto * 10 + int(c)) % d

    if resto == 0:
        return True
    return False


n = input()

print('S' if resto_decimal(n, 4) else 'N')
print('S' if resto_decimal(n, 9) else 'N')
print('S' if resto_decimal(n, 25) else 'N')