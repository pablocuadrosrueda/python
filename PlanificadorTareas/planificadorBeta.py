import sys

#Tengo que definir la lista de tareas
tareas = []

def main():
    print("Iniciando aplicacion...")
    print("############## MENÚ ##############")
    print("1. Añadir tarea \n2. Mostrar todas las tareas \n3. Marcar tarea como completada \n4. Eliminar tarea \n5. Salir")
    while True:
        try: 
            opcion = int(input("Opción: "))
            #Tratamiento de la opción
            a = seleccion_opcion(opcion)
            if a != 0: 
                #NUEVA TAREA
                if a == 1:
                    t = input("Ha seleccionado introducir una tarea, introduzca el titulo de la misma: ")
                    nuevaTarea(t)
                #LISTAR TAREAS    
                elif a == 2: 
                    print("Ha seleccionado listar tareas, mostrando ...")
                    lsTareas()
                #COMPLETAR TAREA    
                elif a == 3:
                    s = input("Ha seleccionado marcar tarea como completada, introduzca el nombre de la misma: ")
                    completaTarea(s)
                #ELIMINAR TAREA
                elif a == 4: 
                    s = input("Ha seleccionado eliminar tarea, introduzca el nombre de la misma: ")
                    eliminaTarea(s)
                else:
                    salir()    
        except ValueError:
            print("Error, tipo de dato erróneo")

def seleccion_opcion(a):
    if isinstance(a,int):
        if a < 1 or a > 5:
            print("Error, opción en el rango inváldio ( 1- 5 )")
        else:
            return a
    else:
        print("La operacion debe ser un numero")
        return 0                               


#Añade una nueva tarea, usamos isinstance para verificar si es un string, devuelve 0 si ha habido un error y 1 si se ha añadido con éxito  
def nuevaTarea(tarea):
    if not isinstance(tarea,str):
        return 0
    else:
        tareas.append({"titulo": tarea, "hecha": False})
        return 1
    
#Muestra un listado completo con todas las tareas     
def lsTareas():
    if not tareas:
        print("No hay tareas pendientes.")
        return

    for i, t in enumerate(tareas, 1):
        estado = "✔️" if t["hecha"] else "❌"
        print(f"{i}. [{estado}] {t['titulo']}")

#Marca una tarea como completada si el formato es el válido y si esta existe 
def completaTarea(tarea):
    if not isinstance(tarea,str):
        return 0
    else:
        for t in tareas: 
            if t["titulo"] == tarea: 
                t["hecha"] = True
                return 1
    print("No se ha encontrado la tarea")            
    return -1        

#Marca una tarea como completada si el formato es el válido y si esta existe 
def eliminaTarea(tarea):
    if not isinstance(tarea,str):
        return 0
    else:
        for t in tareas: 
            if t["titulo"] == tarea: 
                tareas.remove(t)
                return 1
    return -1    

        
def salir():
    sys.exit("Final del programa, apagando aplicacion...")       




#MAIN:
main()