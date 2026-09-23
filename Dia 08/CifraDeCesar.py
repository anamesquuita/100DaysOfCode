import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decodificar":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Após {encode_or_decode}, esse é seu resultado: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?
choice="sim"

while choice == "sim":
    direction = input("Digite 'codificar' para criptografar ou digite 'decodificar' para descriptografar:\n").lower()
    text = input("Digite sua mensagem:\n").lower()
    shift = int(input("Digite a quantidade de posições a serem deslocadas:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    choice=input("Você gostaria de continuar criptografando e descriptografando mensagens? (sim ou não)\n").lower()


