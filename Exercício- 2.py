valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))
resultado = 0;
operacao = input("Digite o tipo da operação: ")

if operacao == "soma":
    resultado = valor1 + valor2
    print("O resultado é: ", resultado)

if operacao == "multiplicação":
    resultado = valor1 * valor2
    print("O resultado é: ", resultado)

if operacao == "divisão":
    resultado = valor1 / valor2
    print("O resultado é: ", resultado)

if operacao == "subtração":
    resultado = valor1 - valor2
    print("O resultado é: ", resultado)
    