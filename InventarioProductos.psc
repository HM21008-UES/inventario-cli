Algoritmo modulo_productos_inventario
	
    //definición de variables
    definir nombres como texto
    definir codigos como entero
    definir precios como texto
    definir stocks como entero
	
    // arreglos de almacenamiento de información
    Dimension nombres[100]
    dimension codigos[100]
    dimension precios[100]
    dimension stocks[100]
    
    // i - en que posición guardaremos el siguiente producto
    // j - recorrer los productos cuando busquemos 
    // codigo buscar - codigo del proudcto que queremos modificar
    Definir i, opcion, j, codigoBuscar como Entero
    i <- 1
	
    Repetir
        Escribir ""
        Escribir "======= MENU PRODUCTOS ======="
        Escribir "1. Agregar producto"
        Escribir "2. Modificar producto"
        Escribir "3. Listar productos"
        Escribir "4. Salir"
        Leer opcion
        
        Segun opcion Hacer
            
            1:
                // registro de nuevo producto
                Escribir "Ingrese nombre del producto:"
                Leer nombres[i]
                
                Escribir "Ingrese codigo del producto:"
                Leer codigos[i]
                
                Escribir "Ingrese precio del producto:"
                Leer precios[i]
                
                Escribir "Ingrese stock del producto:"
                Leer stocks[i]
                
                // validación del stock --- no puede ser negativo
                Si stocks[i] < 0 Entonces
                    Escribir "ERROR: El stock no puede ser negativo"
                SiNo
                    Escribir "Producto registrado correctamente"
                    i <- i + 1      //siguiente posición libre
                FinSi
                
            2:
                // modificación d eocdigo existente
                Escribir "Ingrese el codigo del producto a modificar:"
                Leer codigoBuscar
                
				// busqueda de producto dentro de la lista
                Para j <- 1 Hasta i-1 Hacer
                    Si codigos[j] = codigoBuscar Entonces
                        
                        Escribir "Ingrese el nuevo nombre:"
                        Leer nombres[j]
                        
                        Escribir "Ingrese el nuevo precio:"
                        Leer precios[j]
                        
                        Escribir "Ingrese el nuevo stock:"
                        Leer stocks[j]
                        
                        // validación del stock nuevamente -- no puede ser negativo
                        Si stocks[j] < 0 Entonces
                            Escribir "ERROR: El stock no puede ser negativo"
                            stocks[j] <- 0
                        FinSi
                        
                        Escribir "Producto modificado correctamente"
                        
                    FinSi
                FinPara
                
            3:
                // lista de todos los productos guardados
                Si i = 1 Entonces
                    Escribir "No existen productos registrados"
                SiNo
                    Para j <- 1 Hasta i-1 Hacer
                        Escribir "--------------------------------"
                        Escribir "Nombre : ", nombres[j]
                        Escribir "Codigo : ", codigos[j]
                        Escribir "Precio : ", precios[j]
                        Escribir "Stock  : ", stocks[j]
                        Escribir "--------------------------------"
                    FinPara
                FinSi
			4:
				Escribir "Saliendo del programa..."
                
        FinSegun
        
    Hasta Que opcion = 4
	
FinAlgoritmo