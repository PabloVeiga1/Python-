numeros = (
    int(input("Digite o primeiro número: ")),
    int(input("Digite outro número: ")),
    int(input("Digite mais um número: ")),
    int(input("Digite o último número: "))
)

print(f"Você digitou os valores {numeros}")

cont9 = 0
pos3 = 0
pares = []

for n in numeros:
    if n == 9:
        cont9 +=1
    elif n == 3:
        pos3 = numeros.index(3)+1
    elif n%2==0:
        pares.append(n)
print(f"O número 9 apareceu {cont9} vezes.")

if pos3 > 0:
    print(f"O número 3 apareceu na {pos3}° posição.")
else:
    print(f"O número 3 não apareceu em nenhuma posição")

print(f"Os valores pares digitados foram {tuple(pares)}")
