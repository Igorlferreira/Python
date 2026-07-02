def extrair_dominio(email):
    # Divide o email usando "@" como delimitador e retorna a segunda parte
    return email.split('@')[-1]

def main():
    # Solicita o e-mail do usuário
    email = input("Entre com seu e-mail: ")

    # Extrai o domínio do e-mail fornecido
    dominio = extrair_dominio(email)

    # Imprime o domínio
    print("O domínio do seu e-mail é:", dominio)

if __name__ == "__main__":
    main()