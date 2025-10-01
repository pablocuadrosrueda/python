import uuid
from datetime import datetime
#uuid nos ayuda a generar identificadores únicos universales 
class Transaccion:
    def __init__(self, empresa_origen, empresa_destino, articulo, cantidad, precio_unitario):
        self.__id = str(uuid.uuid4())   
        self.__fecha = datetime.now()
        self.__empresa_origen = empresa_origen
        self.__empresa_destino = empresa_destino
        self.__articulo = articulo
        self.__cantidad = cantidad
        self.__desembolso = cantidad * precio_unitario

    def __str__(self):
        return f"[{self.__fecha}] {self.__empresa_origen} → {self.__empresa_destino}: {self.__cantidad}x {self.__articulo} = {self.__desembolso}€"

    # getters básicos
    def get_id(self): return self.__id
    def get_fecha(self): return self.__fecha
    def get_empresa_origen(self): return self.__empresa_origen
    def get_empresa_destino(self): return self.__empresa_destino
    def get_articulo(self): return self.__articulo
    def get_cantidad(self): return self.__cantidad
    def get_desembolso(self): return self.__desembolso


class GestorHistorial:
    def __init__(self):
        self.__transacciones = []

    def agregar_transaccion(self, transaccion):
        self.__transacciones.append(transaccion)

    def buscar_por_articulo(self, nombre):
        return [t for t in self.__transacciones if nombre.lower() in t.get_articulo().lower()]

    def buscar_por_empresa(self, empresa):
        return [t for t in self.__transacciones if t.get_empresa_origen() == empresa or t.get_empresa_destino() == empresa]

    def buscar_por_fecha(self, fecha):
        return [t for t in self.__transacciones if t.get_fecha().date() == fecha]
