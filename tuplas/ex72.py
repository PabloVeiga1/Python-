nums = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")

numDig = int(input("Digite um número entre 0 e 20: "))

while True:
    if numDig < 0 or numDig > 20:
        numDig = int(input("Tente novamente. Digite um número entre 0 e 20: "))
    else:
        print(f"Você digitou o número {nums[numDig]}.")
        break
