logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operacoes= { "+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}

# print(operacoes["*"](4,8))

continuar=True
cont_result=True
while continuar==True:
    print(logo)
    n1=int(input("Digite o primeiro número da operação: "))
    cont_result=True
    while cont_result==True:
        operador=input("Digite qual operação deseja realizar: (+, -, * ou /)\n")
        n2=int(input("Digite o segundo número da operação: "))
        if operador=="+":
            resultado=(operacoes["+"](n1,n2))
            print(resultado)
        if operador=="-":
            resultado=(operacoes["-"](n1,n2))
            print(resultado)
        if operador=="*":
            resultado=(operacoes["*"](n1,n2))
            print(resultado)
        if operador=="/":
            resultado=(operacoes["/"](n1,n2))
            print(resultado)

        escolha=input(f"Pressione 'c' se deseja continuar calculando com {resultado}, digite 'n' se deseja continuar com uma nova operação.\n")
        if escolha=="c":
            n1= resultado
            cont_result=True
        else:
            cont_result=False
            print("\n"*100)
