tabela = (
    "Flamengo",
    "Palmeiras",
    "Athletico-PR",
    "Fluminense",
    "Bahia",
    "Cruzeiro",
    "Atlético-MG",
    "Santos",
    "Coritiba",
    "Red Bull Bragantino",
    "São Paulo",
    "Botafogo",
    "Vitória",
    "Corinthians",
    "Mirassol",
    "Vasco da Gama",
    "Grêmio",
    "Internacional",
    "Remo",
    "Chapecoense"
)

print("=-"*50)
print(f"Lista de times do Brasileirão {tabela}")
print("=-"*50)
print(f"Os 5 primeiros são {tabela[:5]}")
print("=-"*50)
print(f"Os 4 últimos são {tabela[-4:]}")
print("=-"*50)
print(f"Times em ordem alfabética {sorted(tabela)}")
print("=-"*50)
print(f"Chapecoense está na {tabela.index("Chapecoense")+1}° posição")