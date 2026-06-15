import unittest #libreria para las pruebas
from Modulo_productos import buscar_producto, nombre_duplicado #funciones a hacer el test
 #pruebas del modulo productos
class TestInventario(unittest.TestCase):
    def setUp(self): #lista de productos ejemplo para hacer las pruebas
        self.productos_lista = [
            {"codigo": "123", "nombre": "Peras", "precio": 0.25, "stock": 50},
            {"codigo": "1515", "nombre": "Manzana", "precio": 0.35, "stock": 30}
        ]
    def test_buscar_producto_existente(self): # sí codigo existente
        resultado = buscar_producto(self.productos_lista, "123")
        self.assertEqual(resultado, 0)
    def test_buscar_producto_inexistente(self): #sí producto no existe
        resultado = buscar_producto(self.productos_lista, "999")
        self.assertIsNone(resultado)
    def test_nombre_duplicado_detectado(self): # comprobación de productos ya registrados
        resultado = nombre_duplicado(self.productos_lista, "PERAS")
        self.assertTrue(resultado)
    def test_nombre_no_duplicado(self): # comprobación de nombre nuevo
        resultado = nombre_duplicado(self.productos_lista, "Uvas")
        self.assertFalse(resultado)
if __name__ == '__main__':
    unittest.main()

"""
RESUTADO DEL TEST: 

============================= test session starts =============================
collecting ... collected 4 items

test_productos.py::TestInventario::test_buscar_producto_existente PASSED [ 25%]    --- encontró producto existente
test_productos.py::TestInventario::test_buscar_producto_inexistente PASSED [ 50%]  --- confirma si producto inexistente es none
test_productos.py::TestInventario::test_nombre_duplicado_detectado PASSED [ 75%]   --- detecto nombre repetido 
test_productos.py::TestInventario::test_nombre_no_duplicado PASSED       [100%]    --- confirma nombre nuevo no esta duplicado

============================== 4 passed in 0.10s ==============================

Proceso terminado con código de salida 0

---confirma que las funciones buscar_producto() y nombre_duplicado() funcionan según lo esperado para los casos evaluados---
"""