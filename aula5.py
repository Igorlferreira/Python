def calcular_peso_ideal(altura, sexo):
    if sexo.lower() == 'masculino':
        peso_ideal = (72.7 * altura) - 58
    elif sexo.lower() == 'feminino':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        peso_ideal = None
        print("Sexo inválido. Por favor, insira 'masculino' ou 'feminino'.")
    return peso_ideal

altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (masculino/feminino): ")

peso_ideal = calcular_peso_ideal(altura, sexo)

if peso_ideal:
    print("Seu peso ideal é:", peso_ideal, "kg")