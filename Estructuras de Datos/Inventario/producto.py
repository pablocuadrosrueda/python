"""
Producto clase con atributos:
codigo (string, clave unica del producto)
nombre (string)
cantidad (int)
precio (float)
"""

# __ privado
# _ protegido
#   publico

class Producto:
    #Constructor
    def __init__(self,codigo,nombre,cantidad,precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    @classmethod
    def copiar(cls, otro):
        if not isinstance(otro, Producto):
            raise ValueError("Se esperaba un objeto Producto")
        return cls(
            otro.get_codigo(),
            otro.get_nombre(),
            otro.get_cantidad(),
            otro.get_precio()
        )    


    #Métodos get y set     
    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_cantidad(self):
        return self.__cantidad

    def actualizar_cantidad(self, cantidad):
        if cantidad + self.__cantidad >= 0:
            self.__cantidad += cantidad
            return True
        else:
            print(f"No se admite stock negativo de un producto, cantidad actual: {self.__cantidad}")  
            return False  

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    def __str__(self):
        return f"{self.__nombre} (Código: {self.__codigo}) - Cantidad: {self.__cantidad}, Precio: ${self.__precio:.2f}"