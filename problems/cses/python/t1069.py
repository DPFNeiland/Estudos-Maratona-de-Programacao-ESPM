
dna = input()

resp = 1
maior = 1
for i in range(1, len(dna)):

    if dna[i] != dna[i-1]:
        if maior > resp:
            resp = maior
        maior = 1

    if dna[i] == dna[i-1]:
        maior += 1

if maior > resp:
    resp = maior

print(resp)