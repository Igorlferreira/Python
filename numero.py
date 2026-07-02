def calcular_inverso(numero):
    # Converte o número em uma string e reverte
    numero_invertido = str(numero)[::-1]
    # Converte o número invertido de volta para inteiro
    return int(numero_invertido)

def main():
    # Solicita um número inteiro de três algarismos ao usuário
    numero = int(input("Digite um número inteiro com três algarismos: "))

    # Calcula o inverso do número
    inverso = calcular_inverso(numero)

    # Calcula a soma do número com seu inverso
    soma = numero + inverso

    # Imprime o inverso do número
    print("O inverso do número é:", inverso)

    # Imprime a soma
    print("A soma é:", numero, "+", inverso, "=", soma)

if __name__ == "__main__":
    main()