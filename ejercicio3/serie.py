#Ejercicio que pide un número de elementos ( números reales ) que se van a introducir y va comprobando que cada número es mayor al anterior
#si en algún momento no se cumple esa condición pedirá que se vuelva a introducir 

#Para este ejericico nos valdremos de una variable auxiliar para guardar el anterior y con eso será suficiente 

#primero pedimos un número al usuario de los números que se van a introducir (Entendemos que será un número mayor que 0)
num=-1
while num <= 0:
    num = int(input("Introduce un número mayor que 0 que será la longitud de la lista: "))

#Ahora comenzamos a pedir los números 
ant=0
for i in range(num):
    x = int(input())
    if(x < ant):
        while(x < ant):
            x = int(input("Vuelve a introducir el número, actualmente es menor que el anterior: "))
    ant = x        