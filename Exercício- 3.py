valorInicial = int(input("Digite o valor inicial: "))
valorFinal = int(input("Digite o valor final: "))

if valorInicial < valorFinal:
    print("O valor inicial deve ser maior que o valor final!!!")
else:
    for valor in range(valorInicial, valorFinal - 1, -1):
       print(valor)