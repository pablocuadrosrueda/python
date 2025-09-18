#Un numero es perfecto si es la suma de todos sus divisores sin contar el mismo 

num=-1
while num <= 0: 
    num = int(input("Introduce un número mayor que 0: "))

sum=0
for i in range(1,(num//2)+1):
    if num % i == 0: 
        sum += i

if(sum == num):
    print("El numero es perfecto")
else: 
    print("El numero no es perfecto")    
