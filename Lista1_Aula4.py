# Lista 1 - Aula 4
# 1. Desenvolva um programa que leia dois números e informe o maior deles.
numero1 = input("Digite o primeiro numero")
numero2 = input("Digite o segundo numero")
if numero1 > numero2:
    print("O primeiro numero é o maior")
else:
    print("O segundo numero é o maior")


# 2. Faça um código que leia um número informado pelo usuário e que ao final informe se o número é par ou ímpar.

valor = int(input("Digite um  numero"))
if valor % 2 == 0:
    print("O valor é par")
else:
    print("O valor é impar")

# 3. Partindo da solução da questão anterior. Crie um programa que calcule o quadrado de um número quando ele for par e que calcule o cubo do número caso ele seja ímpar.

valor = int(input("Digite um  numero"))
if valor % 2 == 0:
    valorFinal = valor**2
    print(valorFinal)
else:
    valorFinal = valor**3
    print(valorFinal)


# 4. Faça um programa que receba 3 notas de prova de um aluno, calcule a média e diga se ele foi aprovado ou reprovado. A média para aprovação é de pelo menos 6 (aprovado se média maior ou igual a 6).
nota1 = float(input("Digite a primeira nota"))
nota2 = float(input("Digite seguna nota"))
nota3 = float(input("Digite a terceira nota"))
notaFinal = (nota1 + nota2 + nota3) / 3
print(notaFinal)
if notaFinal >= 6:
    print("Voce foi aprovado")
else:
    print("Voce foi reprovado")


# 5. Escreva um program que leia dois números e que pergunte qual operação o usuário deseja realizar.
# Esse programa deve aceitar como respostas a soma(+), a subtração(-), a multiplicação (*) e a divisão (/).
# Ao final, o programa deve exibir o resultado da operação escolhida.
# num1 = float(input('Insira o primeiro número: '))
# num2 = float(input('Insira o segundo número: '))
# op = input('Insira o sinal da operação desejada: ')
# if (op == '+'):
#     soma = num1 + num2
#     print(soma)
# elif (op == '-'):
#     subt = num1 - num2
#     print(subt)
# elif (op == '*'):
#     mult = num1*num2
#     print(mult)
# elif (op == '/'):
#     div = num1/num2
#     print(div)

# 6. Escreva um programa que pergunte a distância que determinado passageiro deseja percorrer em km.
# A partir disso calcule o preço da passagem. É cobrado 0,50 centavos por km para viagens de até 300 km.
# E 0,45 centavos para viagens mais longas.
# distancia = float(input('Insira quantos km deseja percorrer na viagem: '))
# if (distancia <= 300):
#     preco = distancia*0.50
#     print(preco)
# elif (distancia > 300):
#     preco = 300*0.5 + (distancia - 300)*0.45
#     print(preco)


# 7. Suponha que determinado usuário possua 2 logins em uma rede corporativa.
# Login 1
# usuario: jardim
# senha: flores1206
# Login 2
# usuario: cordeiro
# senha la1506
# Escreva um programa que valide o acesso do usuário na rede. Caso o par usuário e senha estejam corretos, o programa deve imprimir a mensagem: "Seja bem vindo!". Caso contrário, "Usuário e senha não conferem".

OBS.: Não consegui Fazer

# 8. Uma empresa concederá aumento de salário aos seus funcionários de acordo com o cargo.
# Cargo - Aumento(%)
# Gerente Geral - 30
# Gerente de Relacionamento - 30
# Analista - 25
# Assistente de Atendimento - 20
# Crie um programa que solicite o salário e o cargo do funcionário. O programa deve calcular e imprimir o novo salário. Caso o cargo informado não esteja na tabela, o programa deve imprimir "Cargo inválido".

OBS.: Não consegui Fazer