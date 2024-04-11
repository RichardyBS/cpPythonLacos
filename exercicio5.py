##Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles.                                                                                                                                                                                                                                                                                                                                                                        Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4. 

i = int(input("Digite o Primeiro Numero: "))
j = int(input("Digite o Segundo Numero: "))
print(f"{i} X {j} = " , end="")

n = 1

while n <= j:
    print(f"{i}", end=" ")
    if n < j:
        print("+", end=" ")
    n += 1
print(f" = {i * j}", end="")
while n <= i:
    print(f"{j}", end="" )
    if n < i:
        print(f"+ ", end="")
        n += 1
        print("\n Fim do Laco")