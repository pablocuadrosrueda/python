#Escribe un programa que introduzca un número entero ( cantidad de números a introducir ) y calcule la sumatoria de estos y además la muestre 
num=-1
while num <= 0: 
    num = int(input("Introduce la longitud de la lista: "))

cadena = ""  # aquí construiremos la sumatoria
sum=0
for i in range(1, num+1):
    x = int(input(f"Número {i}: "))
    sum += x
    if i == 1:
        cadena = str(x)  # el primer número no lleva '+'
    else:
        cadena += f"+{x}"  # los siguientes sí


print(f"{cadena}={sum}")