# 1. Construa um programa  em que o usuário informe a estatura em metros e o programa converta para centímetros.
# Em aula


# 2. Construa um programa que receba do usuário a variação do deslocamento de um objeto (em metros) e a variação do tempo percorrido(em segundos). Ao fim, calcule a velocidade média.
# Obs.: velocidade_media = variação_do_deslocamento/tempo_percorrido

deslocamento = float(input("Informe quantos metros voce deslocou"))
tempo = float(input("Informe seu tempo de deslocamento"))
velociadeMedia = deslocamento / tempo

print("velociade media é :", velociadeMedia, "metros por segundo")


# 3. Construa um programa que calcule a área de um triângulo.
# Area_Triangulo = (Base*Altura)/2

base = int(input("Digite o valor da base do triangulo"))
altura = int(input("Digite o valor da altura do triangulo"))
areaTriangulo = (base * altura) / 2
print(areaTriangulo)

# 4. Construa um programa que leia 2 números reais que seja informados pelo usuário. Esse programa deve realizar soma e
# a multiplicação desses valores e exibir o resultado de ambos.
# Em aula

# 5. Escreva um programa que calcule um aumento de salário. No programa o usuário deve ser capaz de inserir o valor atual do salário, a porcentagem de aumento que receberá e o programa deverá informar ao final o novo valor do salário e qual o valor do acréscimo do salário.

salario = float(input("Digite o valor do seu salario atual"))
porc = float(input("Digite a porcetangem de aumento"))
aumento = (porc / 100) * salario
salarioFinal = salario + aumento
print(salarioFinal)


# 6. Faça um programa que peça o nome e a idade do usuário e que ao final informe o ano de nascimento da pessoa.

nome = input("Insira seu nome")
idade = int(input("Digite sua idade"))
nascimento = 2023 - idade
print(nascimento)

# 7. Escreva um script que receba um número e que ao final informe o dobro do número, o número ao quadrado e o número ao cubo.
# Em aula

# 8. Uma mobiliária paga aos seus corretores um salário base de 1500 Reais. Além disso, uma comissão de 200,00 Reias por cada imóvel vendido e 5% do valor de cada venda. Construa um programa que solicite o nome do corretor, a quantidade de imóveis vendidos e o valor total de suas vendas. Ao fim, o programa deve calcular e escrever o salário final do corretor de imóveis.
OBS.: Não consegui fazer