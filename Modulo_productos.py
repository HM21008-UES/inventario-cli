import json
import os

archivo_json = 'productos.json' # archivo donde se guardan los productos

def cargar_productos(): # cargar productos del archivo
    # si no existe el archivo devuelve lista vacía
    if not os.path.exists(archivo_json):
        return []
    try:
        # abre y lee el archivo json
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)

    except json.JSONDecodeError: #si el archivo dañado
        print("Error al cargar datos")
        return []
    except OSError:
        print("Error al abrir el archivo")
        return []

# guardar productos en el archivo
def guardar_productos(productos_lista):
    with open(archivo_json, 'w', encoding='utf-8') as archivo:
        json.dump(productos_lista, archivo, indent=4)

# buscar producto por código
def buscar_producto(productos_lista, codigo):
    for i, prod in enumerate(productos_lista):
        if prod['codigo'].upper() == codigo.upper():
            return i
    return None

# validar nombre duplicado
def nombre_duplicado(productos_lista, nombre):
    for producto in productos_lista:
        if producto['nombre'].upper() == nombre.upper():
            return True
    return False

# agregar producto
def agregar_producto(productos_lista): # CREATE
    print("\n--- Agregar producto ---")
    codigo = input("Código: ").strip().upper()
    if codigo == "":
        print("Código vacío")
        return
    if buscar_producto(productos_lista, codigo) is not None:
        print("El código ya existe")
        return
    nombre = input("Nombre:").strip()
    if nombre == "":
        print("Nombre vacío")
        return
    if nombre_duplicado(productos_lista, nombre):
        print("El nombre ya existe")
        return
    try:
        precio = float(input("Precio: $"))
        if precio <= 0:
            print("Precio inválido")
            return
        stock = int(input("Stock:"))
        if stock < 0:
            print("Stock inválido")
            return
    except ValueError:
        print("Datos inválidos")
        return

    producto = { # estructura del producto
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    productos_lista.append(producto) # agregar a lista
    guardar_productos(productos_lista) # guardar en JSON
    print("Producto agregado correctamente")

# listar productos
def listar_productos(productos_lista): # READ
    print("\n--- Lista de productos ---")
    if len(productos_lista) == 0:
        print("No hay productos registrados")
        return

    for p in productos_lista:
        print("----------------")
        print("Código:", p['codigo'])
        print("Nombre:", p['nombre'])
        print("Precio: $", p['precio'])
        print("Stock:", p['stock'])

# modificar producto
def modificar_producto(productos_lista): # UPDATE
    print("\n--- Modificar producto ---")
    codigo = input("Código: ").strip().upper()
    i = buscar_producto(productos_lista, codigo)
    if i is None:
        print("El producto no existe")
        return

    nombre = input("Nuevo nombre:").strip()
    if nombre != "":
        if nombre_duplicado(productos_lista, nombre):
            print("El nombre ya está en uso")
            return
        productos_lista[i]['nombre'] = nombre

    try:
        precio = input("Nuevo precio: $").strip()
        if precio != "":
            precio = float(precio)
            if precio > 0:
                productos_lista[i]['precio'] = precio

        stock = input("Nuevo stock:").strip()
        if stock != "":
            stock = int(stock)
            if stock >= 0:
                productos_lista[i]['stock'] = stock
    except ValueError:
        print("Dato inválido")

    guardar_productos(productos_lista)
    print("Producto actualizado correctamente")

# eliminar producto
def eliminar_producto(productos_lista): # DELETE CRUD
    print("\n--- Eliminar producto ---")
    codigo = input("Código: ").strip().upper()
    i = buscar_producto(productos_lista, codigo)
    if i is None:
        print("El producto no existe")
        return
    productos_lista.pop(i)
    guardar_productos(productos_lista)
    print("Producto eliminado correctamente")

# total de productos
def total_productos(productos_lista):
    print("\n--- Total de productos ---")
    if len(productos_lista) == 0:
        print("No hay productos registrados")
        return

    contador = 1
    for producto in productos_lista:
        print(str(contador) + ".", producto["nombre"], "- Stock:", producto["stock"])
        contador += 1

    print("--------------------------------------")
    print("Cantidad de productos registrados:", len(productos_lista)) # conteo

# valor total inventario
def valor_inventario(productos_lista):
    print("\n--- Valor total del inventario ---")
    if len(productos_lista) == 0:
        print("No hay productos registrados")
        return

    total_inventario = 0
    contador = 1

    for producto in productos_lista:
        valor_producto = producto["precio"] * producto["stock"]
        print(str(contador) + ".", producto["nombre"], "$", valor_producto)
        total_inventario += valor_producto
        contador += 1

    print("--------------------------------------")
    print("Valor total del inventario: $", total_inventario) # acumulador

# productos bajo stock y agotados
def productos_bajo_stock(productos_lista):
    print("\n-------------------------------")
    print("    Productos con bajo stock   ")
    print("-------------------------------")

    encontrados_bajo = False
    encontrados_agotados = False
    contador_bajo = 1
    contador_agotados = 1

    print("A punto de agotarse -----------") # <10
    for producto in productos_lista:
        if 0 < producto["stock"] < 10:
            encontrados_bajo = True
            print(str(contador_bajo) + ".", producto["nombre"], "=> Stock:", producto["stock"])
            contador_bajo += 1

    if not encontrados_bajo:
        print("No hay productos a punto de agotarse")

    print("\nAgotados ---------------------") # stock 0
    for producto in productos_lista:
        if producto["stock"] == 0:
            encontrados_agotados = True
            print(str(contador_agotados) + ".", producto["nombre"], "=> Stock:", producto["stock"])
            contador_agotados += 1

    if not encontrados_agotados:
        print("No hay productos agotados")

# menú principal productos
def menu_productos():
    while True:
        productos_lista = cargar_productos()
        print("\n------ Menú productos -----")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Total productos")
        print("6. Valor inventario")
        print("7. Bajo stock / agotados")
        print("8. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":
            agregar_producto(productos_lista)
        elif opcion == "2":
            listar_productos(productos_lista)
        elif opcion == "3":
            modificar_producto(productos_lista)
        elif opcion == "4":
            eliminar_producto(productos_lista)
        elif opcion == "5":
            total_productos(productos_lista)
        elif opcion == "6":
            valor_inventario(productos_lista)
        elif opcion == "7":
            productos_bajo_stock(productos_lista)
        elif opcion == "8":
            break
        else:
            print("Opción inválida")