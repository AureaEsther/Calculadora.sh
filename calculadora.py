# Mensagem de boas vindas

print("Olá! Seja bem vindo(a) à calculadora EBAC!")

# Entrada do nome do usuário para constar na mensagem de saudação

usuario_nome = input("Digite seu nome:")
print("Ótimo! Vamos dar início aos cálculos,", usuario_nome,".")

# Entrada dos valores que serão utilizados na operação

num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))

# Exibição das operações disponíveis para o usuário

print("OPERAÇÕES DISPONÍVEIS:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão inteira")
print("5 - Divisão decimal")
print("6 - Resto da divisão")
print("7 - Exponenciação")

# Entrada do número que representa a operação desejada

opcao = int(input("Digite o número da operação desejada:"))

# Operações a serem realizadas a partir da opção escolhida

if opcao == 1:
  print("Você escolheu a operação: ADIÇÃO")
  print("Resultado = ", num1 + num2)

if opcao == 2:
  print("Você escolheu a operação: SUBTRAÇÃO")
  print("Resultado = ", num1 - num2)

if opcao == 3:
  print("Você escolheu a operação: MULTIPLICAÇÃO")
  print("Resultado = ", num1 * num2)

if opcao == 4:
  print("Você escolheu a operação: DIVISÃO INTEIRA")
  print("Resultado = ", num1 // num2)

if opcao == 5:
  print("Você escolheu a operação: DIVISÃO DECIMAL")
  print("Resultado = ", num1 / num2)

if opcao == 6:
  print("Você escolheu a operação: RESTO DA DIVISÃO")
  print("Resultado = ", num1 % num2)

if opcao == 7:
  print("Você escolheu a operação: EXPONENCIAÇÃO")
  print("Resultado = ", num1 ** num2)



#Fim do código


