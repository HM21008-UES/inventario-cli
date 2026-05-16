# ==========================================
# MODULO PROVEEDORES Y MOVIMIENTOS
# ==========================================

import json

# ==========================================
# LISTAS PRINCIPALES
# ==========================================

proveedores = []
movimientos = []

# Productos simulados
productos = [
    {"nombre": "Coca Cola", "stock": 20},
    {"nombre": "Pepsi", "stock": 15},
    {"nombre": "Galletas", "stock": 30}
]

# ==========================================
# GUARDAR JSON
# ==========================================

def guardar_datos():

    with open("proveedores.json", "w") as archivo:
        json.dump(proveedores, archivo, indent=4)

    with open("movimientos.json", "w") as archivo:
        json.dump(movimientos, archivo, indent=4)

# ==========================================
# CARGAR JSON
# ==========================================

def cargar_datos():

    global proveedores
    global movimientos

    try:
        with open("proveedores.json", "r") as archivo:
            proveedores = json.load(archivo)

    except:
        proveedores = []

    try:
        with open("movimientos.json", "r") as archivo:
            movimientos = json.load(archivo)

    except:
        movimientos = []

# ==========================================
# REGISTRAR PROVEEDOR
# ==========================================

def registrar_proveedor():

    print("\n===== REGISTRAR PROVEEDOR =====")

    nombre = input("Ingrese nombre: ")
    telefono = input("Ingrese telefono: ")

    proveedor = {
        "nombre": nombre,
        "telefono": telefono
    }

    proveedores.append(proveedor)

    guardar_datos()

    print("Proveedor registrado correctamente")

# ==========================================
# LISTAR PROVEEDORES
# ==========================================

def listar_proveedores():

    print("\n===== LISTA DE PROVEEDORES =====")

    if len(proveedores) == 0:

        print("No existen proveedores")

    else:

        for i in range(len(proveedores)):

            print(f"\nProveedor #{i+1}")
            print(f"Nombre   : {proveedores[i]['nombre']}")
            print(f"Telefono : {proveedores[i]['telefono']}")

# ==========================================
# MODIFICAR PROVEEDOR
# ==========================================

def modificar_proveedor():

    listar_proveedores()

    if len(proveedores) > 0:

        try:

            posicion = int(input("\nSeleccione proveedor: ")) - 1

            if posicion >= 0 and posicion < len(proveedores):

                nuevo_nombre = input("Nuevo nombre: ")
                nuevo_telefono = input("Nuevo telefono: ")

                proveedores[posicion]["nombre"] = nuevo_nombre
                proveedores[posicion]["telefono"] = nuevo_telefono

                guardar_datos()

                print("Proveedor modificado correctamente")

            else:
                print("ERROR: Proveedor invalido")

        except:
            print("ERROR: Dato invalido")

# ==========================================
# ELIMINAR PROVEEDOR
# ==========================================

def eliminar_proveedor():

    listar_proveedores()

    if len(proveedores) > 0:

        try:

            posicion = int(input("\nSeleccione proveedor: ")) - 1

            if posicion >= 0 and posicion < len(proveedores):

                proveedores.pop(posicion)

                guardar_datos()

                print("Proveedor eliminado correctamente")

            else:
                print("ERROR: Proveedor invalido")

        except:
            print("ERROR: Dato invalido")

# ==========================================
# REGISTRAR MOVIMIENTO
# ==========================================

def registrar_movimiento():

    print("\n===== MOVIMIENTOS INVENTARIO =====")

    for i in range(len(productos)):

        print(f"{i+1}. {productos[i]['nombre']} | Stock: {productos[i]['stock']}")

    try:

        producto = int(input("Seleccione producto: ")) - 1

        if producto >= 0 and producto < len(productos):

            tipo = input("Tipo de movimiento (entrada/salida): ").lower()

            cantidad = int(input("Ingrese cantidad: "))

            fecha = input("Ingrese fecha: ")

            # ==================================
            # ENTRADA
            # ==================================

            if tipo == "entrada":

                productos[producto]["stock"] += cantidad

            # ==================================
            # SALIDA
            # ==================================

            elif tipo == "salida":

                if cantidad > productos[producto]["stock"]:

                    print("ERROR: Stock insuficiente")
                    return

                productos[producto]["stock"] -= cantidad

            else:

                print("ERROR: Tipo invalido")
                return

            # ==================================
            # GUARDAR MOVIMIENTO
            # ==================================

            movimiento = {
                "producto": productos[producto]["nombre"],
                "tipo": tipo,
                "cantidad": cantidad,
                "fecha": fecha,
                "stock_actual": productos[producto]["stock"]
            }

            movimientos.append(movimiento)

            guardar_datos()

            print("Movimiento registrado correctamente")
            print(f"Stock actual: {productos[producto]['stock']}")

        else:
            print("ERROR: Producto invalido")

    except:
        print("ERROR: Datos invalidos")

# ==========================================
# HISTORIAL MOVIMIENTOS
# ==========================================

def historial_movimientos():

    print("\n===== HISTORIAL MOVIMIENTOS =====")

    if len(movimientos) == 0:

        print("No existen movimientos")

    else:

        for i in range(len(movimientos)):

            print(f"\nMovimiento #{i+1}")
            print(f"Producto     : {movimientos[i]['producto']}")
            print(f"Tipo         : {movimientos[i]['tipo']}")
            print(f"Cantidad     : {movimientos[i]['cantidad']}")
            print(f"Fecha        : {movimientos[i]['fecha']}")
            print(f"Stock actual : {movimientos[i]['stock_actual']}")

# ==========================================
# MENU PRINCIPAL
# ==========================================

def menu():

    cargar_datos()

    while True:

        print("\n===================================")
        print(" MODULO PROVEEDORES Y MOVIMIENTOS")
        print("===================================")

        print("1. Registrar proveedor")
        print("2. Listar proveedores")
        print("3. Modificar proveedor")
        print("4. Eliminar proveedor")
        print("5. Registrar movimiento")
        print("6. Historial movimientos")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_proveedor()

        elif opcion == "2":
            listar_proveedores()

        elif opcion == "3":
            modificar_proveedor()

        elif opcion == "4":
            eliminar_proveedor()

        elif opcion == "5":
            registrar_movimiento()

        elif opcion == "6":
            historial_movimientos()

        elif opcion == "7":

            print("Saliendo del sistema...")
            break

        else:
            print("Opcion invalida")

# ==========================================
# INICIO
# ==========================================

menu()