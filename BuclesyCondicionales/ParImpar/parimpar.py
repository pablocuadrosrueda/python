#Programa que pide un número de lementos que se van a introducir y cuenta cuantos pares o impares

#Suponemos que el numero de la lista debe ser > 0 
num=-1
while(num <= 0):
    num = int(input("Introduce la longitud de la lista de números: "))

par=0
impar=0

for i in range(num):
    #hacemos valor absoluto a todos los numeros
    x = int(input())
    if(abs(x)%2==0):
        par+=1
    else: 
        impar+=1

print("--------------------------------------------RESULTADOS--------------------------------------------")
print(f"Numeros pares: {par}")
print(f"Numeros impares: {impar}")
