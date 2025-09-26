"""
Almacen  clase con composicion:
nombre (string)
inventario (diccionario donde clave = codigo del producto, valor = objeto Producto)
Metodos sugeridos:
agregar_producto(producto)
eliminar_producto(codigo)
actualizar_stock(codigo, cantidad)
mostrar_inventario()
"""
from producto import Producto

class Almacen:
    #Constructor
    def __init__(self, nombre):
        self.__nombre = nombre           
        self.__inventario = {} 
    
    #Agregar producto
    #Especificaciones: 
    """
    Primero comprobamos si lo pasado por la cabecera es un producto, luego hay dos casos, que ya exista o que no 
    """
    def agregar_producto(self,nuevo):
            if not isinstance(nuevo,Producto):
                 raise ValueError("Se espera recibir un producto")
            else:
                 cod = nuevo.get_codigo()
                 #Si es un produto nuevo 
                 if cod not in self.__inventario:
                    self.__inventario[cod]=nuevo
                 else: 
                    self.__inventario[cod].actualizar_cantidad(nuevo.get_cantidad())

    def eliminar_producto(self,cod):
        if cod not in self.__inventario:
            print(f"El producto con codigo: {cod} no se encuentra en el inventario")
            return False
        else:
            del self.__inventario[cod]     
            return True
        
    def actualizar_stock(self,codigo,cantidad):
        if self.__inventario:
             if codigo in self.__inventario:
                  self.__inventario[codigo].actualizar_cantidad(cantidad)
             else:
                  print(f"El producto con codigo: {codigo} no se encuentra en el inventario")   
        else:
            print("Sin existencias de ningún tipo")          

    def mostrar_inventario(self):
         if self.__inventario:
              for p in self.__inventario.values():
                   print(p)
         else:
              print("Sin existencias de ningún tipo")