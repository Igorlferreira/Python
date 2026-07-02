def calcular_salario_final(salario_fixo, vendas):
    comissao = vendas * 4
    salario_final = salario_fixo + comissao
    return comissao, salario_final

salario_fixo = float(input("Digite o salário fixo do funcionário: "))
vendas = float(input("Digite o valor das vendas do funcionário: "))

comissao, salario_final = calcular_salario_final(salario_fixo, vendas)

print("Comissão do funcionário: R$", format(comissao, ".2f"))
print("Salário final do funcionário: R$", format(salario_final, ".2f"))