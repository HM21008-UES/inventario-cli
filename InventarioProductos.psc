Algoritmo Sistema_Inventario_Principal
	
    //Variables compartidas - sin tamaño -
    definir nombres como texto
    definir codigos como entero
    definir precios como texto
    definir stocks como entero
    
    // arreglos para el historial de movimientos
    definir historialProducto como texto
    definir historialCantidad como entero
    definir historialFecha como texto
    definir historialTipo como texto  // entrada o salida
    definir historialProveedor como texto
    
    Dimension nombres[100]
    Dimension codigos[100]
    Dimension precios[100]
    Dimension stocks[100]
    
    Dimension historialProducto[500]
    Dimension historialCantidad[500]
    Dimension historialFecha[500]
    Dimension historialTipo[500]
    Dimension historialProveedor[500]
    
    // i - próxima posición libre para guardar un producto
    // h - posición del siguiente movimiento en historial
    Definir i, h Como Entero
    i <- 1
    h <- 1
    
    Definir opcion Como Entero
    
    Repetir
        Escribir ""
        Escribir "================================="
        Escribir "   SISTEMA GENERAL INVENTARIO"
        Escribir "================================="
        Escribir "1. Gestionar Productos"
        Escribir "2. Proveedores y Movimientos"
        Escribir "3. Salir"
        Leer opcion
        
        Segun opcion Hacer
            1:
                modulo_productos_inventario(nombres, codigos, precios, stocks, i)
            2:
                Modulo_Proveedores_y_Movimientos
            3:
                Escribir "Cerrando sistema..."
                
            De Otro Modo:
                Escribir "Opcion invalida"
        FinSegun
        
    Hasta Que opcion = 3
	
FinAlgoritmo

SubProceso modulo_productos_inventario(nombres, codigos, precios, stocks, i Por Referencia)
	
    Definir j , opcion, codigoBuscar Como Entero //j recorre la lista
	
    Repetir
        Escribir ""
        Escribir "======= MENU PRODUCTOS ======="
        Escribir "1. Agregar producto"
        Escribir "2. Modificar producto"
        Escribir "3. Listar productos"
        Escribir "4. Volver a : SISTEMA GENERAL INVENTARIO"
        Leer opcion
        
        Segun opcion Hacer
            
            1:
                Escribir "Ingrese nombre del producto:"
                Leer nombres[i]
                
                Escribir "Ingrese codigo del producto:"
                Leer codigos[i]
                
                Escribir "Ingrese precio del producto:"
                Leer precios[i]
                
                Escribir "Ingrese stock del producto:"
                Leer stocks[i]
                
                Si stocks[i] < 0 Entonces
                    Escribir "ERROR: El stock no puede ser negativo"
                SiNo
                    Escribir "Producto registrado correctamente"
                    i <- i + 1
                FinSi
                
            2:
                Escribir "Ingrese el codigo del producto a modificar:"
                Leer codigoBuscar
				
                Para j <- 1 Hasta i-1 Hacer
                    Si codigos[j] = codigoBuscar Entonces
                        
                        Escribir "Ingrese el nuevo nombre:"
                        Leer nombres[j]
                        
                        Escribir "Ingrese el nuevo precio:"
                        Leer precios[j]
                        
                        Escribir "Ingrese el nuevo stock:"
                        Leer stocks[j]
                        
                        Si stocks[j] < 0 Entonces
                            Escribir "ERROR: El stock no puede ser negativo"
                            stocks[j] <- 0
                        FinSi
                        
                        Escribir "Producto modificado correctamente"
                        
                    FinSi
                FinPara
                
            3:
                Si i = 1 Entonces
                    Escribir "No existen productos registrados"
                SiNo
                    Para j <- 1 Hasta i-1 Hacer
                        Escribir "--------------------------------"
                        Escribir "Nombre: ", nombres[j]
                        Escribir "Codigo: ", codigos[j]
                        Escribir "Precio: ", precios[j]
                        Escribir "Stock : ", stocks[j]
                        Escribir "--------------------------------"
                    FinPara
                FinSi
			4:
				Escribir "Saliendo del modulo productos..."
                
        FinSegun
        
    Hasta Que opcion = 4
	
FinSubProceso

SubProceso Modulo_Proveedores_y_Movimientos

// Definición de variables globales simuladas
	Definir nombreProv, contactoProv Como Cadena
	Definir nombreProd, fechaEntrada Como Cadena
	Definir stockActual, cantidadEntrada, nuevoStock Como Entero
	Definir opcion Como Entero
	
	// Inicialización de datos de ejemplo
	nombreProv <- "Sin asignar"
	contactoProv <- "Sin asignar"
	nombreProd <- "Producto Ejemplo"
	stockActual <- 10 // Stock inicial para la prueba
	
	Repetir
		Escribir ""
		Escribir "========================================="
		Escribir "   SISTEMA DE INVENTARIO - TU MÓDULO"
		Escribir "========================================="
		Escribir "1. Agregar Proveedor"
		Escribir "2. Registrar Entrada de Stock"
		Escribir "3. Consultar Historial de Entradas (Última)"
		Escribir "4. Salir"
		Escribir "Seleccione una opción:"
		Leer opcion
		
		Segun opcion Hacer
			1:
				Escribir "--- AGREGAR PROVEEDOR ---"
				Escribir "Ingrese el nombre del proveedor:"
				Leer nombreProv
				Escribir "Ingrese el contacto (Tel/Email):"
				Leer contactoProv
				Escribir "? Proveedor guardado con éxito."
				
			2:
				Escribir "--- REGISTRAR ENTRADA DE STOCK ---"
				Escribir "Producto actual: ", nombreProd
				Escribir "Stock actual: ", stockActual
				
				Escribir "Ingrese la cantidad que entra:"
				Leer cantidadEntrada
				
				// VALIDACIÓN: Que la entrada no sea negativa o cero
				Si cantidadEntrada <= 0 Entonces
					Escribir "? Error: La cantidad de entrada debe ser mayor a cero."
				SiNo
					Escribir "Ingrese la fecha de entrada (DD/MM/AAAA):"
					Leer fechaEntrada
					
					nuevoStock <- stockActual + cantidadEntrada
					stockActual <- nuevoStock // Actualizamos el stock
					
					Escribir "? Entrada registrada."
					Escribir "Nuevo stock disponible: ", stockActual
				FinSi
				
			3:
				Escribir "--- HISTORIAL DE ENTRADAS ---"
				Si cantidadEntrada = 0 Entonces
					Escribir "No hay movimientos registrados aún."
				SiNo
					Escribir "Último movimiento registrado:"
					Escribir "Fecha: ", fechaEntrada
					Escribir "Producto: ", nombreProd
					Escribir "Cantidad ingresada: ", cantidadEntrada
					Escribir "Proveedor: ", nombreProv
					Escribir "Stock resultante: ", stockActual
				FinSi
				
			4:
				Escribir "Saliendo del sistema..."
				
			De Otro Modo:
				Escribir "Opción no válida."
		FinSegun
		
	Hasta Que opcion = 4
	
FinSubProceso

	

