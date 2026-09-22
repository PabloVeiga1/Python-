produtos = (
    "Lápis",1.75,
    "Borracha",2.00,
    "Caderno",15.90,
    "Estojo",25.00,
    "Transferidor",4.20,
    "Compasso",9.99,
    "Mochila",120.32,
    "Canetas",22.30,
    "Livro",34.90
)

print("_"*50)
print("LISTAGEM DE PREÇOS")
print("_"*50)

for p in produtos:
    indiceAtual = produtos.index(p)
    print(f"{p}....................R${produtos[indiceAtual+1]}")

