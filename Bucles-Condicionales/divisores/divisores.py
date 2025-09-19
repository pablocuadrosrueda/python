#Escribe un programa que pida al usuario un número entero positivo y muestre por pantalla sus divisores
num=-1
while num <= 0:
    num = int(input("Introduce un numero entero positivo: "))

#Mostramos todos sus divisores, que teniendo en cuenta que el máximo divisor posible de un numero es su mitad o menos de la mitad para impares (sin contar el mismo) ... 
print(f"Mostrando divisores del número {num}:")   
for i in range(1,num+1):
    if num%i == 0: 
        print(i, ",",end="")

print(num)

#Detalles interesantes:
# División entera -> // 
# end="" para que no se haga salto de línea automáticamente 
