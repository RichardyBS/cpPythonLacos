##Escreva um programa que solicite números inteiros para o usuário. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética. 

numUser = int(input("Escreva um numero inteiro e irei somalo infinitamente. Digite 0 para Finalizar o Programa: "))
resposta = 0
soma = resposta + numUser
media = soma / 2
resposta += numUser;

while numUser > 0:
    if numUser > 0:
        print(f"A soma dos numeros digitados foi: {resposta}")
        numUser = int(input("Escreva um numero inteiro e irei somalo infinitamente. Digite 0 para Finalizar o Programa: "))
    
    if numUser == 0:
        print("+", end=" ")
        print(f" = {numUser + soma}\n", end="")
        print(f" = {media}", end="")


















##fiz um usando o random (aprendi por fora agr so queria deixar pra mostrar kkkk)

""" import random

numIntUser = int(input("Digite um Numero Inteiro:      "))

random = random.randint(0,10)

while numIntUser != random:
    numIntUser = int(input("Digite um Numero Inteiro:      "))

    if numIntUser == random:
        print(f"A quantidade de numeros digitados foi:{numIntUser} VOCE ACERTOU")   """