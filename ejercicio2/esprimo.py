#Ejercicio que dado un número devuelve si este es primo o no 
num = -1
while num < 0:
    num = int(input("Introduce un número entero positivo: "))

#primer caso (si es menor o igual a 2 no es primo)
if num < 2: print("No es primo")
elif num == 2: print("Es primo")

#segundo caso (si el numero es par tampoco será primo)
elif num%2 == 0: print("No es primo")

#ahora recorremos los numeros en el rango 3 hasta su raiz cuadrada buscando si existe algún divisor, si es así no será primo 
else:
    for i in range(3,int(num**(1/2))+1,2):
        if num%i == 0: 
            print("No es primo")
            break

    else: 
        print("Es primo")
