def menu_general():
    while True:
        print("\n-----------------------------------")
        print("    Sistema general de inventario      ")
        print("-----------------------------------")
        print("1. Módulo gestión de productos")
        print("2. Módulo proveedores y movimientos")
        print("3. Salir del sistema")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_proveedores()
        elif opcion == "3":
            print("Saliendo del sistema. Hasta luego!!!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu_general()