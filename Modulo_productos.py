import json
import os

# archivo donde se guardan los productos
archivo_json = 'productos.json'

# cargar productos del archivo
def cargar_productos():
    # si no existe el archivo devuelve lista vacía
    if not os.path.exists(archivo_json):
        return []
    try:
        # abre y lee el archivo json
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    # si el archivo está dañado
    except json.JSONDecodeError:
        print("Error al cargar datos.")
        return []

# guardar productos en el archivo
def guardar_productos(productos_lista):
    # escribe en el archivo json
    with open(archivo_json, 'w', encoding='utf-8') as archivo:
        json.dump(productos_lista, archivo, indent=4)

# buscar producto por código
def buscar_producto(productos_lista, codigo):
    # recorre lista de productos
    for i, prod in enumerate(productos_lista):
        # compara código
        if prod['codigo'].upper() == codigo.upper():
            return i
    return None

# validar nombre duplicado
def nombre_duplicado(productos_lista, nombre):
    # revisa si ya existe el nombre
    for prod in productos_lista:
        if prod['nombre'].upper() == nombre.upper():
            return True
    return False

# agregar producto
def agregar_producto(productos_lista):
    print("\n--- Agregar producto ---")
    # pedir código
    codigo = input("Código: ").strip().upper()
    # validar código vacío
    if codigo == "":
        print("Código vacío.")
        return
    # validar duplicado
    if buscar_producto(productos_lista, codigo) is not None:
        print("El código ya existe.")
        return
    # pedir nombre
    nombre = input("Nombre: ").strip()
    # validar nombre
    if nombre == "":
        print("Nombre vacío.")
        return
    # validar duplicado nombre
    if nombre_duplicado(productos_lista, nombre):
        print("El nombre ya existe.")
        return
    try:
        # pedir precio
        precio = float(input("Precio: "))
        # validar precio
        if precio <= 0:
            print("Precio inválido.")
            return
        # pedir stock
        stock = int(input("Stock: "))
        # validar stock
        if stock < 0:
            print("Stock inválido.")
            return
    except ValueError:
        print("Datos inválidos.")
        return
    # crear producto
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    # guardar en lista
    productos_lista.append(producto)
    # guardar archivo
    guardar_productos(productos_lista)
    print("Producto agregado correctamente.")

# listar productos
def listar_productos(productos_lista):
    print("\n--- Lista de productos ---")
    # si no hay productos
    if len(productos_lista) == 0:
        print("No hay productos registrados.")
        return
    # mostrar cada producto
    for p in productos_lista:
        print("----------------")
        print("Código:", p['codigo'])
        print("Nombre:", p['nombre'])
        print("Precio:", p['precio'])
        print("Stock:", p['stock'])

# modificar producto
def modificar_producto(productos_lista):
    print("\n--- Modificar producto ---")
    codigo = input("Código: ").strip().upper()
    # buscar producto
    i = buscar_producto(productos_lista, codigo)
    if i is None:
        print("El producto no existe.")
        return
    # cambiar nombre
    nombre = input("Nuevo nombre: ").strip()
    if nombre != "":
        if nombre_duplicado(productos_lista, nombre):
            print("El nombre ya está en uso.")
            return
        productos_lista[i]['nombre'] = nombre
    try:
        # cambiar precio
        precio = input("Nuevo precio: ").strip()
        if precio != "":
            precio = float(precio)
            if precio > 0:
                productos_lista[i]['precio'] = precio
        # cambiar stock
        stock = input("Nuevo stock: ").strip()
        if stock != "":
            stock = int(stock)
            if stock >= 0:
                productos_lista[i]['stock'] = stock
    except ValueError:
        print("Dato inválido.")
    # guardar cambios
    guardar_productos(productos_lista)
    print("Producto actualizado correctamente.")

# eliminar producto
def eliminar_producto(productos_lista):
    print("\n--- Eliminar producto ---")
    codigo = input("Código: ").strip().upper()
    # buscar producto
    i = buscar_producto(productos_lista, codigo)
    if i is None:
        print("El producto no existe.")
        return
    # eliminar
    productos_lista.pop(i)
    guardar_productos(productos_lista)
    print("Producto eliminado correctamente.")

# submenú de productos
def menu_productos():
    while True:
        productos_lista = cargar_productos()
        print("\n======= MENÚ PRODUCTOS =======")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto(productos_lista)
        elif opcion == "2":
            listar_productos(productos_lista)
        elif opcion == "3":
            modificar_producto(productos_lista)
        elif opcion == "4":
            eliminar_producto(productos_lista)
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")