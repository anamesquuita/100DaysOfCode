print(r'''
                    _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                 '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
print("Seja bem-vindo a ilha do tesouro!")
print("Sua missão é encontrar o tesouro escondido.\n\n")

print("Após um naufrágio você se encontra no meio de uma ilha deserta.\nVocê acredita ter chegado a ilha do tesoura, mas seu mapa está ensopado...\n")
print("\n Sem mais escolhas, você entra na mata densa da ilha.")

p1=input("\na) Seguir à direita\nb) Seguir à esquerda\n")

if p1 == "a":
    print("Você caiu direto no ninho de uma Píton gigante e foi devorado!\nGame Over!")

elif p1 == "b":
    print("Você avança e chega em um grande rochedo")
    p2 = input("\na) Ignorar o grande rochedo\nb) Tentar subir no rochedo para ver algo\n")

    if p2 == "a":
        print(
            "Você segue na mata densa e acaba andando em círculos. Eventualmente você tropeça em um galho e cai no ninho de uma grande Píton. Você foi devorado!\n Game Over!")
    elif p2 == "b":
        print(
            "De cima da grande rocha você consegue ver um círculo de pequenas pedras não muito longe de onde você está.")
        p3 = input("\na) Seguir no rumo do círculo de pedras\nb) Seguir em outra direção.\n")

        if p3 == "a":
            print(
                "Você segue rumo ao círculo de pequenas pedras. Ao chegar nele você percebe que é o jardim de uma fada moradora daquela ilha.\nEla te lança um feitiço por invadir propriedade privada e te transforma numa pequena cobrinha.\n Game Over!")
        elif p3 == "b":
            print(
                "Você anda por kilometros sem saber onde está. Eventualmente você chega a outra ponta da ilha\n Nela você vê um grande baú, já aberto, com jóias e ouro dentro.\nAo lado dela tem um esqueleto.\nParabéns! Você achou o tesouro!\nEspero que consiga sair da ilha para aproveitá-lo hehe :)")
        else:
            print("Escolha invalida, escolha entre a ou b.")
    else:
        print("Escolha invalida, escolha entre a ou b.")
else:
    print("Escolha invalida, escolha entre a ou b.")

