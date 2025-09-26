""""
Empresa → clase con composición:
nombre (string)
almacenes (diccionario donde clave = nombre del almacén, valor = objeto Almacén)
Métodos sugeridos:
agregar_almacen(nombre)
eliminar_almacen(nombre)
mostrar_almacenes()
transferir_producto(codigo, cantidad, origen, destino)
Operaciones que debes implementar
Agregar, eliminar y modificar productos dentro de cada almacén.
Mostrar el inventario completo de un almacén.
Agregar y eliminar almacenes.
Transferir productos entre almacenes (disminuir stock en origen y aumentar en destino).
Opcional: calcular valor total de inventario por almacén o por empresa.
Ideas de estructura de archivos
"""

from almacen import Almacen
from producto import Producto

def __init__(self,nombre):
    self.__nombre = nombre
    self.__almacenes = {}

#Para agregar un almacén primero debo comprobar si dicho almacén no existe ya previamente (su nombre está disponible)
def agregar_almacen(self,almacen):
    if not isinstance(almacen,Almacen):
        raise ValueError("Se espera recibir un almacen")
    else:
        #Necesito extraer el nombre del almacen 
        nombre = almacen.get_nombre()
        #Si el almacén no existe lo creamos
        if nombre not in self.__almacenes:
            self.__almacenes[nombre] = almacen
            return True
        else:
            print(f"El almacen con nombre: {nombre} ya existe")
            return False

#Es preferible que pasemos el nombre del almacén a la hora de eliminarlo 
def elimina_almacen(self,nombre):
    if not isinstance(nombre,str):
        raise ValueError("Se espera recibir una cadena (el nombre del almacen)")
    else:
        #Si el almacén no existe no lo podemos borrar
        if nombre not in self.__almacenes:
            print(f"El almacen con nombre: {nombre} no existe")
            return False
        else:
            del self.__almacenes[nombre]
            return True

def mostrar_almacenes(self):
    #Primero comprobamos que tengamos almacenes que mostrar
    if not self.__almacenes:
        print("Actualmente la empresa no tiene ningún almacen")
    else:
        for almacen in self.__almacenes.values():
            print(f"Nombre: {almacen.get_nombre()}")    


def transferir_producto(self,codigo, cantidad, origen, destino):
    #Primero compruebo que ambos almacenes existen (recordamos que oirgen y destino son cadenas de caracteres)
    if origen in self.__almacenes and destino in self.__almacenes:
        almacen_origen = self.__almacenes[origen]
        almacen_destino = self.__almacenes[destino]
        #Posteriormente compruebo que el producto existe en el almacen de origen
        c = almacen_origen.esta_producto(codigo)
        if c != 0:
            #Vale, ahora comprobamos que tengo cantidad suficiente como para satisfaces la transferencia
            if c >= cantidad:
                #Una vez hemos comprobado todo podemos realizar la transferencia (la cantidad para el almacen de origen es negativa)
                almacen_origen.actualizar_stock(codigo,(-cantidad))
                almacen_destino.actualizar_stock(codigo,cantidad)
                return True
            else:
                print("La cantidad seleccionada no es compatible con la cantidad en stock que hay actualmente en el almacen de origen")   
                return False
        else:
            print(f"El producto con código: {codigo} no esta en stock ")             
            return False
    else:
        print("Al menos uno de los almacenes introducidos no existen")            
        return False