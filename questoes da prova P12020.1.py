print("Nome: Thamires Lemes Leal")
print("Matricula: 201921140")
print("")
print("")

print("Questão 1 da prova:")
print("")
num1=int(input("Digite o primeiro número:"))
num2=int(input("Digite o segundo número:"))
num3=int(input("Digite o terceiro número:"))
menor = num1
if (num2 < menor):
 menor = num2
elif (num3 < menor):
 menor = num3
print("Menor:" ,menor)
print("")

print("Questão 2 da prova:")
print("")

nome=input("Digite seu nome completo:")
x= nome.split(" ")
print("Nome inserido na lista:",x)
print("Terceira letra do nome:", nome[2])
print(f"\033[7;31;40m Thamires Lemes Leal\033[0m")
print("")
print("")

print("Questão 3 da prova:")
print("")

class Pai:
    def __init__(self):
        self.nome="Nome do Pai"
        self.sobrenome="Sobrenome da familia"
        self.idade=42
        self.cor_olhos="Verdes"
        self.cor_cabelos="Castanhos"

class Mae:
    def __init__(self):
        self.nome="Nome da Mae"
        self.sobrenome="Sobrenome da familia"
        self.idade=30
        self.cor_olhos="Azuis"
        self.cor_cabelos="Preto"

class Filho(Pai):
    def __init__(self):
        Pai.__init__(self)
        self.nome="Nome do filho"
        self.idade=22
        self.cor_cabelos="Loiro"


class Filha(Mae):
    def __init__(self):
        Mae.__init__(self)
        self.nome="Nome da filha"
        self.idade=20
        self.cor_olhos="Castanhos"

p= Pai()
m= Mae()
fo= Filho()
fa= Filha()

x=input ("Digite Pai:")
print(f"\033[1mOlhos {p.cor_olhos}\033[0m")

x= input ("Digite Mae:")
print(f"\033[1mCabelos {m.cor_cabelos}\033[0m")

y= input("Digite qual membro da familia (filho ou filha):")

if y == ("Filha"):
    print(f"\033[1mCabelos", fa.cor_cabelos,"herdados da Mãe\033[0m")

elif y == ("Filho"):
    print(f"\033[1mOlhos", fo.cor_olhos,"herdados do Pai!\033[0m")

