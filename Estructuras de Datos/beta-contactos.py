"""
1. Agenda de contactos
Usa listas de diccionarios para almacenar contactos (nombre, teléfono, email).
Funciones a implementar:
agregarContacto()
buscarContacto(nombre) → devuelve los datos del contacto
eliminarContacto(nombre)
modificarContacto(nombre, campo, nuevo_valor)
💡 Práctica: recorrer listas, acceder a diccionarios, validar tipos y campos.
"""


# Lo primero es escoger bien la estructura de datos. Normalmente, cuando agregamos un contacto, no solemos borrarlo con frecuencia, 
# por lo que no es algo muy importante a tener en cuenta el optimizar operaciones de eliminación.
# 
# Una lista podría funcionar, pero con un gran número de contactos la búsqueda secuencial tiene complejidad O(n) y puede volverse lenta.
# 
# Por eso, un diccionario es más adecuado: permite acceder a un contacto por su nombre (clave) en tiempo O(1) promedio, 
# ya que Python implementa los diccionarios internamente como tablas hash.
# 
# Podríamos considerar implementar una tabla hash manualmente, pero para una agenda de contactos pequeña o mediana,
# el diccionario de Python es suficiente y consume menos memoria que una implementación manual de hash.

#Definicion del diccionario

agenda = {}

#Agrega un contacto dado un nombre, número de telefono y email, en caso de error devuelve False en caso de éxito True
def agregarContacto(nombre,num,email):
    #Comprobamos que el formato sea correcto
    if not isinstance(nombre,str) or not isinstance(num,str) or not isinstance(email,str):
        print("ERROR, debes introducir en todos los casos una cadena")
        return False
    else:
        #En python usamos un valor como clave y un diccionario a su vez como valor en caso de meter varios datos como es el caso
        agenda[num] = {"nombre": nombre,"email": email}
        return True

#Busca un contacto dado su número
def buscarContacto(num):
    if isinstance(num,str):
    #en python podemos comprobar si un elemento está en la estructura de datos de esta manera
        if num in agenda:
            print("##################################################################")
            print(f"Informacion del contacto con número {num}")
            print(f"Nombre: {agenda[num]['nombre']} \nEmail: {agenda[num]['email']}")
            print("##################################################################")
            return True
        else:
            print(f"Usuario con numero: {num} no encontrado")
            return False
    else:
        print("ERROR, debes introducir una cadena (el número)")

def eliminarContacto(num):
    if isinstance(num,str): 
        if num in agenda: 
            s=""
            while s != 'y' and s != 'n':       
                s = input(f"¿Estás seguro de que quieres eliminar el número {num} ? :  [y/n]")
            if s == 'n':
                return False
            else:
                del agenda[num]
                print(f"Borrado del numero {num} realizado con éxito")
                return True
        else: 
            print("Usuario no encontrado")
            return False        
    else:
        print("ERROR, debes introducir una cadena (el número)")

#Modifica un contacto dado su número
def modicicaContacto(num):
    if isinstance(num,str):
    #primero buscamos si existe el contacto, también tenemos que tener cuidado con que no coincida con un número ya existente
        if num in agenda:
            print("Procediendo a la modificación del contacto, si hay algún campo que quiera mantener igual, introduzca un 0")
            new_nombre = input("Introduce el nuevo nombre del contacto")
            new_email = input("Introduce el nuevo email del contacto")
            if(new_nombre != '0'):
                agenda[num]["nombre"] = new_nombre
            if(new_email != '0'):
                agenda[num]["email"] = new_email
            print("Modificación realizada con exito")    
            return True    
        else:
            print(f"Usuario con número: {num} no encontrado")
            return False
    else:
        print("ERROR, debes introducir una cadena (el número)")
        

def main():
    while True:
        print("\n")
        print("################---AGENDA DE CONTACTOS---################")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Modificar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos los contactos")
        print("0. Salir")
        print("#########################################################")
        print("\n")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            num = input("Número de teléfono: ")
            email = input("Email: ")
            if agregarContacto(nombre, num, email):
                print("Contacto agregado correctamente.")
            else:
                print("No se pudo agregar el contacto.")
        
        elif opcion == "2":
            num = input("Número de teléfono a buscar: ")
            buscarContacto(num)
        
        elif opcion == "3":
            num = input("Número de teléfono del contacto a modificar: ")
            modicicaContacto(num)
        
        elif opcion == "4":
            num = input("Número de teléfono del contacto a eliminar: ")
            eliminarContacto(num)
        
        elif opcion == "5":
            if not agenda:
                print("No hay contactos en la agenda.")
            else:
                print("\n--- CONTACTOS EN LA AGENDA ---")
                for n, datos in agenda.items():
                    print(f"Número: {n}, Nombre: {datos['nombre']}, Email: {datos['email']}")
        
        elif opcion == "0":
            print("Saliendo de la agenda...")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el main si el script se ejecuta directamente
if __name__ == "__main__":
    main()
