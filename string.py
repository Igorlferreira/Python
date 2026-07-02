def contar_caracteres(string):
    # Converte a string para caixa alta
    string = string.upper()

    # Cria um dicionário para contar a frequência de cada caractere
    frequencia = {}

    # Percorre cada caractere na string
    for caractere in string:
        # Verifica se o caractere já está no dicionário
        if caractere in frequencia:
            # Se sim, incrementa o contador
            frequencia[caractere] += 1
        else:
            # Se não, adiciona o caractere ao dicionário com o valor 1
            frequencia[caractere] = 1

    # Imprime a frequência de cada caractere
    for caractere, contagem in frequencia.items():
        print(f"O caractere {caractere} aparece {contagem} vez{'es' if contagem > 1 else ''}")

def main():
    # Solicita ao usuário que entre com uma string
    string = input("Entre com uma string: ")

    # Chama a função para contar os caracteres
    contar_caracteres(string)

if __name__ == "__main__":
    main()