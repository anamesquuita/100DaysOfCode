logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
continuar=True
bids= {}

def achar_maior_lance(bids):
    maior_lance = 0
    vencedor = ""
    for pessoa in bids:
        valor=bids[pessoa]
        if valor>maior_lance:
            maior_lance=valor
            vencedor=pessoa
    print(f"O vencedor do leilão é {vencedor} com um lance de R${maior_lance}")



while continuar==True:
    nome= input("Qual seu nome? ")
    lance= int(input("Dê seu lance: R$"))
    pessoas=(input("Há outros licitantes? Digite 'sim' ou 'não'")).lower()
    print("\n"*100)
    bids[nome]=lance
    if pessoas=='não':
        continuar=False
        achar_maior_lance(bids)

input("Pressione ENTER para sair")


