# librerías necesarias
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
        print("error al cargar datos")
        return []

# guardar productos en el archivo
def guardar_productos(productos):
    # escribe en el archivo json
    with open(archivo_json, 'w', encoding='utf-8') as archivo:
        json.dump(productos, archivo, indent=4)

# buscar producto por código
def buscar_producto(productos, codigo):
    # recorre lista de productos
    for i, prod in enumerate(productos):
        # compara código
        if prod['codigo'].upper() == codigo.upper():
            return i
    return None

# validar nombre duplicado
def nombre_duplicado(productos, nombre):
    # revisa si ya existe el nombre
    for prod in productos:
        if prod['nombre'].upper() == nombre.upper():
            return True
    return False

# agregar producto
def agregar_producto(productos):
    print("\n--- agregar producto ---")
    # pedir código
    codigo = input("codigo: ").strip().upper()
    # validar código vacío
    if codigo == "":
        print("codigo vacio")
        return
    # validar duplicado
    if buscar_producto(productos, codigo) is not None:
        print("codigo ya existe")
        return
    # pedir nombre
    nombre = input("nombre: ").strip()
    # validar nombre
    if nombre == "":
        print("nombre vacio")
        return
    # validar duplicado nombre
    if nombre_duplicado(productos, nombre):
        print("nombre ya existe")
        return
    try:
        # pedir precio
        precio = float(input("precio: "))
        # validar precio
        if precio <= 0:
            print("precio invalido")
            return
        # pedir stock
        stock = int(input("stock: "))
        # validar stock
        if stock < 0:
            print("stock invalido")
            return
    except ValueError:
        print("datos invalidos")
        return
    # crear producto
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    # guardar en lista
    productos.append(producto)
    # guardar archivo
    guardar_productos(productos)
    print("producto agregado")

# listar productos
def listar_productos(productos):
    print("\n--- lista de productos ---")
    # si no hay productos
    if len(productos) == 0:
        print("no hay productos")
        return
    # mostrar cada producto
    for p in productos:
        print("----------------")
        print("codigo:", p['codigo'])
        print("nombre:", p['nombre'])
        print("precio:", p['precio'])
        print("stock:", p['stock'])

# modificar producto
def modificar_producto(productos):
    print("\n--- modificar producto ---")
    codigo = input("codigo: ").strip().upper()
    # buscar producto
    i = buscar_producto(productos, codigo)
    if i is None:
        print("no existe")
        return
    # cambiar nombre
    nombre = input("nuevo nombre: ").strip()
    if nombre != "":
        if nombre_duplicado(productos, nombre):
            print("nombre en uso")
            return
        productos[i]['nombre'] = nombre
    try:
        # cambiar precio
        precio = input("nuevo precio: ").strip()
        if precio != "":
            precio = float(precio)
            if precio > 0:
                productos[i]['precio'] = precio
        # cambiar stock
        stock = input("nuevo stock: ").strip()
        if stock != "":
            stock = int(stock)
            if stock >= 0:
                productos[i]['stock'] = stock
    except ValueError:
        print("dato invalido")
    # guardar cambios
    guardar_productos(productos)
    print("actualizado")

# eliminar producto
def eliminar_producto(productos):
    print("\n--- eliminar producto ---")
    codigo = input("codigo: ").strip().upper()
    # buscar producto
    i = buscar_producto(productos, codigo)
    if i is None:
        print("no existe")
        return
    # eliminar
    productos.pop(i)
    guardar_productos(productos)
    print("eliminado")

# menú principal
def menu():
    productos = cargar_productos()
    while True:
        print("\n======= MENÚ PRODUCTOS =======")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            listar_productos(productos)
        elif opcion == "3":
            modificar_producto(productos)
        elif opcion == "4":
            eliminar_producto(productos)
        elif opcion == "5":
            print("saliendo")
            break
        else:
            print("opcion invalida")

# ejecutar programa
if __name__ == "__main__":
    menu()