#Ejercicio que muestra el siguiente menú
#1. Sumar
#2. Restar
#3. Multiplicar
#4. Dividir
#5. Salir
import sys
#Siendo operacion el tipo de operacion permitida, n1 el primer argumento, n2 el segundo
def calculadora(op,a,b):
    n1 = a
    n2 = b 
    if(op == 1):
      return n1+n2
    elif(op == 2):
      return n1-n2
    elif(op == 3):
        return n1*n2
    elif(op==4):
        if n2 == 0:
            print("No es posible dividir por 0")
            return -1
        else:
            return n1/n2
    elif(op==5):
        sys.exit()  
    
def pedir_numero(mensaje):
    while True:
        a = (input(mensaje))
        try: 
           return float(a)
        except:
            print("ERROR. Uso: introducir un numero válido") 

def operacion():
    while True:
        entrada = input("Elige una opción (1-5): ")
        try:
            op = int(entrada)
            if 1 <= op <= 5:
                return (op)
            else:
                print("ERROR. Uso:introducir una opción en el rango permitido ")
        except ValueError:
            print("Error: tipo de dato introduciro erróneo.")
    
def main():
    #Iniciando calculadora... 
    print("###############################################################################################################")
    print("##########################################CALCULADORA EN MARCHA################################################")
    print("###############################################################################################################")
    while True:
        a = pedir_numero("Introduce el primer operando: ")
        b = pedir_numero("Introduce el segundo operando: ")
        op = operacion()
        if op != 5:
            print(f"{calculadora(op,a,b):.2f}")
        else: 
            print("Saliendo de la calculadora...")
            print("Fin del programa...")  
            break
              





main()