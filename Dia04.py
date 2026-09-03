import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lista= [pedra,papel,tesoura]
computador = random.randint(0,2)

escolha=input("Faça sua escolha: Digite '1' para PEDRA, '2' para PAPEL e '3' para TESOURA ")
print(lista[computador])

if escolha=='1' and computador==0:
    print(pedra)
    print("Empate")
elif escolha=='1' and computador==1:
    print(pedra)
    print("Papel vence Pedra. Você perdeu!")
elif escolha=='1' and computador==2:
    print(pedra)
    print("Pedra vence Tesoura. Você venceu!")

elif escolha=='2' and computador==0:
    print(papel)
    print("Papel vence Pedra. Você venceu!")
elif escolha == '2' and computador == 1:
    print(papel)
    print("Empate")
elif escolha=='2' and computador==2:
    print(papel)
    print("Tesoura vence papel. Você perdeu!")

elif escolha=='3' and computador==0:
    print(tesoura)
    print("Pedra vence Tesoura. Você perdeu!")
elif escolha == '3' and computador == 1:
    print(tesoura)
    print("Tesoura vence Papel. Você venceu!")
elif escolha=='2' and computador==2:
    print(tesoura)
    print("Empate")