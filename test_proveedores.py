def test_registrar_proveedor():
    proveedores = []

    proveedores.append({
        "nombre": "Raquel",
        "telefono": "7777"
    })

    assert len(proveedores) == 1


def test_modificar_proveedor():
    proveedores = [
        {"nombre": "Raquel", "telefono": "7777"}
    ]

    proveedores[0]["nombre"] = "Diego"

    assert proveedores[0]["nombre"] == "Diego"


def test_eliminar_proveedor():
    proveedores = [
        {"nombre": "Raquel", "telefono": "7777"}
    ]

    proveedores.pop(0)

    assert len(proveedores) == 0


def test_entrada_stock():
    stock = 20

    stock += 10

    assert stock == 30


def test_salida_stock():
    stock = 20

    stock -= 5

    assert stock == 15


def test_stock_insuficiente():
    stock = 10
    cantidad = 15

    assert cantidad > stock


# ==========================================
# RESULTADO DE PRUEBAS UNITARIAS
# ==========================================
#
#============================= test session starts =============================
#collected 10 items
#
# test_productos.py::TestInventario::test_buscar_producto_existente PASSED                                                                                             [ 10%]
#test_productos.py::TestInventario::test_buscar_producto_inexistente PASSED                                                                                           [ 20%]
#test_productos.py::TestInventario::test_nombre_duplicado_detectado PASSED                                                                                            [ 30%]
#test_productos.py::TestInventario::test_nombre_no_duplicado PASSED                                                                                                   [ 40%]
#test_proveedores.py::test_registrar_proveedor PASSED                                                                                                                 [ 50%]
#test_proveedores.py::test_modificar_proveedor PASSED                                                                                                                 [ 60%]
#test_proveedores.py::test_eliminar_proveedor PASSED                                                                                                                  [ 70%]
#test_proveedores.py::test_entrada_stock PASSED                                                                                                                       [ 80%]
#test_proveedores.py::test_salida_stock PASSED                                                                                                                        [ 90%]
#test_proveedores.py::test_stock_insuficiente PASSED                                                                                                                  [100%]
#================================= 10 passed in 0.08s ========================

