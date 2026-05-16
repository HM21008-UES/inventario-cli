Algoritmo Modulo_Proveedores_y_Movimientos
	// Definicion de variables globales simuladas
	Definir nombreProv, contactoProv Como Cadena
	Definir nombreProd, fechaEntrada Como Cadena
	Definir stockActual, cantidadEntrada, nuevoStock Como Entero
	Definir opcion Como Entero
	
	// Inicializacion de datos de ejemplo
	nombreProv <- "Sin asignar"
	contactoProv <- "Sin asignar"
	nombreProd <- "Producto Ejemplo"
	stockActual <- 10 // Stock inicial para la prueba
	
	Repetir
		Escribir ""
		Escribir "========================================="
		Escribir "   SISTEMA DE INVENTARIO "
		Escribir "========================================="
		Escribir "1. Agregar Proveedor"
		Escribir "2. Registrar Entrada de Stock"
		Escribir "3. Consultar Historial de Entradas (ultima)"
		Escribir "4. Salir"
		Escribir "Seleccione una opcion:"
		Leer opcion
		
		Segun opcion Hacer
			1:
				Escribir "--- AGREGAR PROVEEDOR ---"
				Escribir "Ingrese el nombre del proveedor:"
				Leer nombreProv
				Escribir "Ingrese el contacto (Tel/Email):"
				Leer contactoProv
				Escribir "Proveedor guardado con exito."
				
			2:
				Escribir "--- REGISTRAR ENTRADA DE STOCK ---"
				Escribir "Producto actual: ", nombreProd
				Escribir "Stock actual: ", stockActual
				
				Escribir "Ingrese la cantidad que entra:"
				Leer cantidadEntrada
				
				// VALIDACION: Que la entrada no sea negativa o cero
				Si cantidadEntrada <= 0 Entonces
					Escribir "Error: La cantidad de entrada debe ser mayor a cero."
				SiNo
					Escribir "Ingrese la fecha de entrada (DD/MM/AAAA):"
					Leer fechaEntrada
					
					nuevoStock <- stockActual + cantidadEntrada
					stockActual <- nuevoStock // Actualizamos el stock
					
					Escribir "Entrada registrada."
					Escribir "Nuevo stock disponible: ", stockActual
				FinSi
				
			3:
				Escribir "--- HISTORIAL DE ENTRADAS ---"
				Si cantidadEntrada = 0 Entonces
					Escribir "No hay movimientos registrados aun."
				SiNo
					Escribir "Ultimo movimiento registrado:"
					Escribir "Fecha: ", fechaEntrada
					Escribir "Producto: ", nombreProd
					Escribir "Cantidad ingresada: ", cantidadEntrada
					Escribir "Proveedor: ", nombreProv
					Escribir "Stock resultante: ", stockActual
				FinSi
				
			4:
				Escribir "Saliendo del sistema..."
				
			De Otro Modo:
				Escribir "Opcion no valida."
		FinSegun
		
	Hasta Que opcion = 4
	
FinAlgoritmo
//fin	

