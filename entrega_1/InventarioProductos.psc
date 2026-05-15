algoritmo Sistema_Inventario_Principal
	
    definir opcion Como Entero    
    // arreglos de almacenamiento de información - 100 productos si no inventario lleno
    dimension nombres[100]
    dimension codigos[100]
    dimension precios[100]
    dimension stocks[100]
    
	i <- 1 //variable - 1 (Controlar el espacio total)
    
    repetir
        escribir ""
        escribir "================================="
        escribir "   SISTEMA GENERAL INVENTARIO"
        escribir "================================="
        escribir "1. Gestionar Productos"
        escribir "2. Proveedores y Movimientos"
        escribir "3. Salir"
        leer opcion
        
        segun opcion hacer
            1:
                modulo_productos_inventario(nombres, codigos, precios, stocks, i) //llamará a módulo productos				
            2:
                //Modulo_Proveedores_y_Movimientos(...)                
            3:
                escribir "Cerrando sistema..."                
            de otro modo:
                escribir "Opcion invalida" //imprimir opcion invalida y se repide el menu 
        finsegun        
    hasta que opcion = 3	
finalgoritmo
//------------------------------------------------------------------------------------------------------------------------
subproceso modulo_productos_inventario(nombres, codigos, precios, stocks, i) // (Variables locales)
	//variables....
    definir opcion, j, codigoBuscar Como Entero //j  nueva variables 
    definir encontrado Como Logico //voleano
    encontrado <- falso
	
    repetir
        escribir ""
        escribir "======= MENU PRODUCTOS ======="
        escribir "1. Agregar producto"
        escribir "2. Modificar producto"
        escribir "3. Listar productos"
        escribir "4. Salir"
        leer opcion        
        // VALIDACIÓN DEL MENÚ
        si opcion <= 0 o opcion > 4 entonces
            escribir "Opcion invalida, seleccione una opcion correcta"
        sino			
            segun opcion hacer
                
                1:
                    si i > 100 entonces //Espacios declarados 
                        escribir "Inventario lleno"
                    sino
                        // registro de nuevo producto
                        escribir "Ingrese nombre del producto:"
                        leer nombres[i]                        
                        escribir "Ingrese codigo del producto:"
                        leer codigos[i]                        
                        escribir "Ingrese precio del producto:"
                        leer precios[i]                        
                        escribir "Ingrese stock del producto:"
                        leer stocks[i]                        
                        // validación del stock --- no puede ser negativo
                        si stocks[i] < 0 entonces
                            escribir "ERROR: El stock no puede ser negativo"
                        sino
                            escribir "Producto registrado correctamente"
                            i <- i + 1 //Se guardara en el siguiente espacio
                        finsi
                        
                    finsi                    
                2:
                    escribir "Ingrese el codigo del producto a modificar:"
                    leer codigoBuscar
                    
                    encontrado <- falso
					
                    para j <- 1 hasta i-1 hacer 
                        si codigos[j] = codigoBuscar entonces //compara el codigo del producto para saber si esta o no en lista
                            
                            escribir "Ingrese el nuevo nombre:"
                            leer nombres[j]
                            escribir "Ingrese el nuevo precio:"
                            leer precios[j]
                            escribir "Ingrese el nuevo stock:"
                            leer stocks[j]
							
                            si stocks[j] < 0 entonces
                               escribir "ERROR: El stock no puede ser negativo"
                               stocks[j] <- 0
                            finsi
                            
                            escribir "Producto modificado correctamente"
                            encontrado <- verdadero //se modifico el producto
                            
                        finsi
                    finpara
                    
                    si encontrado = falso entonces // no se encontro el codigo de producto e lista
                        escribir "Producto no encontrado"
                    finsi
                    
                3:
                    si i = 1 entonces //primera casilla vacia 
                        escribir "No existen productos registrados"
                    sino
                        para j <- 1 hasta i-1 hacer // impresion de productos en orden
                            escribir "--------------------------------"
                            escribir "Nombre : ", nombres[j]
                            escribir "Codigo : ", codigos[j]
                            escribir "Precio : ", precios[j]
                            escribir "Stock  : ", stocks[j]
                            escribir "--------------------------------"
                        finpara
                    finsi                    
                4:
                    escribir "Saliendo del modulo productos..."                    
            finsegun            
        finsi        
    hasta que opcion = 4	
finsubproceso