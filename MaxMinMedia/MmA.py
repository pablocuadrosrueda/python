#Ejercicio que dada una lista de números introducidad por pantalla devuelva el menor el mayor y la media aritmética

num = -1
while num <= 0: 
    num = int(input("Introduce un numero positivo ( longitud de la lista ): "))

#Definimos variables  
max = float('-inf')
min = float('inf')
sum = 0.0
for i in range(num): 
    x = float(input())
    if x > max:
        max = x
    if x < min:
        min =x
    sum += x       

print(f"Maximo: {max}")
print(f"Minimo: {min}") 
print(f"Media:{sum/num}")

