import random

numeros = tuple(random.sample(range(0,9), 4))
print(f'Os números sorteados foram {numeros}')

maior = 0
menor = numeros[-1]

for n in numeros:
    if n > maior:
        maior = n
    elif n < menor:
        menor = n

print(f"O maior número sorteado foi o {maior}")
print(f"O menor número sorteado foi o {menor}")
