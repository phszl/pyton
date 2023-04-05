salarioFixo=float(input("Digite o salário fixo:"))
vendas=float(input("Digite o valor das vendas: "))

comissão = vendas*0.04
salarioFinal = salarioFixo + comissão

print("A comissão é de R${:.2f}".format(comissão))
print("O salario final é de R${:.2f}".format(salarioFinal))