from producto import Producto
from almacen import Almacen
from empresa import Empresa

#Durante las siguientes semanas agregaremos una clase por encima para permitir transacciones entre Empresas, una clase historial y entrada/salida de los datos

def menu():
    print("\n--- Gestión de Inventarios ---")
    print("1. Agregar almacén")
    print("2. Eliminar almacén")
    print("3. Mostrar almacenes")
    print("4. Agregar producto a un almacén")
    print("5. Eliminar producto de un almacén")
    print("6. Actualizar stock de un producto en un almacén")
    print("7. Mostrar inventario de un almacén")
    print("8. Transferir producto entre almacenes")
    print("0. Salir")

def main():
    empresa = Empresa("Mi Empresa")

    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del almacén: ")
            nuevo = Almacen(nombre)
            empresa.agregar_almacen(nuevo)

        elif opcion == "2":
            nombre = input("Nombre del almacén a eliminar: ")
            empresa.eliminar_almacenes(nombre)

        elif opcion == "3":
            empresa.mostrar_almacenes()

        elif opcion == "4":
            nombre = input("Nombre del almacén: ")
            almacen = empresa.get_almacen(nombre)
            if almacen:
                codigo = input("Código del producto: ")
                nombre_p = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(codigo, nombre_p, cantidad, precio)
                almacen.agregar_producto(producto)
            else:
                print("El almacén no existe.")

        elif opcion == "5":
            nombre = input("Nombre del almacén: ")
            almacen = empresa.get_almacen(nombre)
            if almacen:
                codigo = input("Código del producto a eliminar: ")
                almacen.eliminar_producto(codigo)
            else:
                print("El almacén no existe.")

        elif opcion == "6":
            nombre = input("Nombre del almacén: ")
            almacen = empresa.get_almacen(nombre)
            if almacen:
                codigo = input("Código del producto: ")
                cantidad = int(input("Cantidad a añadir (puede ser negativa): "))
                almacen.actualizar_stock(codigo, cantidad)
            else:
                print("El almacén no existe.")

        elif opcion == "7":
            nombre = input("Nombre del almacén: ")
            almacen = empresa.get_almacen(nombre)
            if almacen:
                almacen.mostrar_inventario()
            else:
                print("El almacén no existe.")

        elif opcion == "8":
            origen = input("Almacén origen: ")
            destino = input("Almacén destino: ")
            codigo = input("Código del producto: ")
            cantidad = int(input("Cantidad a transferir: "))
            empresa.transferir_producto(codigo, cantidad, origen, destino)

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
