# librerías necesarias
import json
import os

# archivo donde se guardará el inventario
archivo_json = 'productos.json'


# guardar y cargar productos

# esta función carga los productos guardados
def cargar_productos():

    # verifica si el archivo existe
    if not os.path.exists(archivo_json):
        return []

    try:
        # abre el archivo para leer datos
        with open(archivo_json, 'r', encoding='utf-8') as archivo:

            # convierte el json en lista
            return json.load(archivo)

    # error si el archivo tiene problemas
    except json.JSONDecodeError:
        print("Hubo un error al cargar los productos.")
        return []


# esta función guarda productos en el archivo
def guardar_productos(productos):

    # abre el archivo en modo escritura
    with open(archivo_json, 'w', encoding='utf-8') as archivo:

        # guarda la información en formato json
        json.dump(productos, archivo, indent=4)


# buscar productos

# busca un producto usando el código
def buscar_producto_por_codigo(productos, codigo):

    # recorre todos los productos
    for index, producto in enumerate(productos):

        # compara los códigos
        if producto['codigo'].upper() == codigo.upper():

            # devuelve la posición encontrada
            return index

    # retorna none si no existe
    return None


# funciones del inventario

# agregar un producto nuevo
def agregar_producto(productos):

    # título
    print("\n--- AGREGAR PRODUCTO ---")

    # solicita el código
    codigo = input("Ingrese el código del producto: ").strip().upper()

    # verifica si el código ya existe
    if buscar_producto_por_codigo(productos, codigo) is not None:
        print("Ya existe un producto con ese código.")
        return

    # solicita el nombre
    nombre = input("Ingrese el nombre del producto: ").strip()

    # validación del precio
    while True:
        try:
            # solicita el precio
            precio = float(input("Ingrese el precio del producto: $"))

            # verifica que sea válido
            if precio <= 0:
                print("El precio debe ser mayor a 0.")
                continue

            break

        # error si escribe letras
        except ValueError:
            print("Ingrese un número válido.")

    # validación del stock
    while True:
        try:
            # solicita cantidad disponible
            stock = int(input("Ingrese el stock disponible: "))

            # verifica que no sea negativo
            if stock < 0:
                print("El stock no puede ser negativo.")
                continue

            break

        # error si escribe texto
        except ValueError:
            print("Ingrese un número entero.")

    # crear producto
    nuevo_producto = {

        # código del producto
        "codigo": codigo,

        # nombre del producto
        "nombre": nombre,

        # precio del producto
        "precio": precio,

        # cantidad disponible
        "stock": stock
    }

    # agrega producto a la lista
    productos.append(nuevo_producto)

    # guarda cambios
    guardar_productos(productos)

    # mensaje final
    print("Producto agregado correctamente.")


# mostrar productos registrados
def listar_productos(productos):

    # título
    print("\n--- LISTA DE PRODUCTOS ---")

    # verifica si hay productos
    if not productos:
        print("No hay productos registrados.")
        return

    # recorre la lista
    for prod in productos:

        # línea decorativa
        print("-" * 30)

        # mostrar información
        print(f"Código : {prod['codigo']}")
        print(f"Nombre : {prod['nombre']}")
        print(f"Precio : ${prod['precio']:.2f}")
        print(f"Stock  : {prod['stock']}")

    # línea final
    print("-" * 30)


# modificar un producto
def modificar_producto(productos):

    # título
    print("\n--- MODIFICAR PRODUCTO ---")

    # solicita el código
    codigo = input("Ingrese el código del producto: ").strip().upper()

    # busca el producto
    indice = buscar_producto_por_codigo(productos, codigo)

    # verifica si existe
    if indice is None:
        print("No se encontró el producto.")
        return

    # muestra producto encontrado
    print(f"Producto encontrado: {productos[indice]['nombre']}")

    # solicita nuevo nombre
    nuevo_nombre = input("Ingrese el nuevo nombre (Enter para dejar igual): ").strip()

    # cambia el nombre si escribió algo
    if nuevo_nombre:
        productos[indice]['nombre'] = nuevo_nombre

    # solicita nuevo precio
    nuevo_precio = input("Ingrese el nuevo precio (Enter para dejar igual): ").strip()

    # verifica si escribió un dato
    if nuevo_precio:
        try:
            # convierte el dato a decimal
            precio_float = float(nuevo_precio)

            # verifica si es válido
            if precio_float > 0:
                productos[indice]['precio'] = precio_float
            else:
                print("El precio ingresado no es válido.")

        # error si escribe letras
        except ValueError:
            print("Debe ingresar un número.")

    # solicita nuevo stock
    nuevo_stock = input("Ingrese el nuevo stock (Enter para dejar igual): ").strip()

    # verifica si escribió un dato
    if nuevo_stock:
        try:
            # convierte el dato a entero
            stock_int = int(nuevo_stock)

            # verifica si es válido
            if stock_int >= 0:
                productos[indice]['stock'] = stock_int
            else:
                print("El stock no puede ser negativo.")

        # error si escribe texto
        except ValueError:
            print("Debe ingresar un número entero.")

    # guarda los cambios
    guardar_productos(productos)

    # mensaje final
    print("Producto actualizado correctamente.")


# eliminar un producto
def eliminar_producto(productos):

    # título
    print("\n--- ELIMINAR PRODUCTO ---")

    # solicita el código
    codigo = input("Ingrese el código del producto: ").strip().upper()

    # busca el producto
    indice = buscar_producto_por_codigo(productos, codigo)

    # verifica si existe
    if indice is None:
        print("No se encontró el producto.")
        return

    # elimina el producto
    producto_eliminado = productos.pop(indice)

    # guarda los cambios
    guardar_productos(productos)

    # mensaje de confirmación
    print(f"El producto '{producto_eliminado['nombre']}' fue eliminado.")


# menú principal

# menú del sistema
def menu_productos():

    # carga productos guardados
    lista_productos = cargar_productos()

    # mantiene el menú activo
    while True:

        # mostrar opciones
        print("\n======= MENÚ PRODUCTOS =======")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        # solicita opción
        opcion = input("Seleccione una opción: ").strip()

        # ejecuta opción elegida
        if opcion == '1':
            agregar_producto(lista_productos)

        elif opcion == '2':
            listar_productos(lista_productos)

        elif opcion == '3':
            modificar_producto(lista_productos)

        elif opcion == '4':
            eliminar_producto(lista_productos)

        # salir del programa
        elif opcion == '5':
            print("Saliendo del sistema...")
            break

        # opción inválida
        else:
            print("Opción no válida. Intente nuevamente.")


# iniciar programa
if __name__ == "__main__":

    # ejecuta el menú
    menu_productos()
