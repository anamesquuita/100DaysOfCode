print("Bem-vindo ao calculador de gorjeta!")
conta=float(input("Insira o valor total da conta:\n"))
porcentagem=float(input("Insira a porcentagem desejada da gorjeta:\n"))
pessoas=int(input("Insira a quantidade de pessoas que irão dividir a conta:\n"))

total= (conta + (conta*porcentagem)/100)
dividirconta= total/pessoas
round(dividirconta,2)

print(f"O total da conta com {porcentagem}% de gorjeta será {total}\n")
print(f"Dividido por {pessoas} pessoas, cada uma pagará {dividirconta}")

input("\nPressione ENTER para sair...")