#Escribe un programa que introduzca un número entero ( cantidad de números a introducir ) y calcule la sumatoria de estos 
num=-1
while num <= 0: 
    num = int(input("Introduce la longitud de la lista: "))

sum=0
for i in range(num):
    sum += int(input())

print(f"Resultado de la sumatoria: {sum}")