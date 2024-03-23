salario = float(input("Informe seu salário: "))
if salario < 3000:
    print("pobre miseravel")
elif salario > 3000 and salario <= 6000:
    print("da pro gasto")
elif salario > 6000 and salario <= 15000:
    imposto = salario * 0.20
    salarioFinal = salario - imposto
    print("seu salario final foi reduzido para:", salarioFinal, ",o valor descontado foi de:", imposto)