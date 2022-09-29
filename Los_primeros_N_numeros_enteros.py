# Sumar los primeros n numeros enteros

from re import I


print("---------------------------------------------")
print("----SUMAR LOS PRIMERO N NUMEROS ENTEROS------")
print("---------------------------------------------")

#input
n = int(input("Digite el ultimo numero de la suma: "))
i = 1
sum = 0

#process
while i<=n:
    sum = sum + i 
    i = i + 1

print("La suma de los primeros",n,"es",sum)