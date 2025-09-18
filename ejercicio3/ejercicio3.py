#El factorial de un numero es el productorio de todos los números en el rango 1 hasta el numero 

num=-1
while num <= 0: 
    num = int(input("Introduce un numero mayor que 0: "))

prod=1
for i in range(1,num+1):
    prod *= i
print(f"El factorial del numero {num} es : {prod}")