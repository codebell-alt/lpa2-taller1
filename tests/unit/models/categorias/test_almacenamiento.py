import pytest

from src.models.concretos.armario import Armario


def test_armario_precio_y_descripcion():
    # Armario concrete implements price calculation and description
    a = Armario(
        "Arm1",
        "Pino",
        "Natural",
        300.0,
        num_puertas=3,
        num_cajones=2,
        tiene_espejos=True,
    )
    # precio esperado: base + puertas*50 + cajones*30 + espejos(100)
    expected = 300 + 3 * 50 + 2 * 30 + 100
    assert a.calcular_precio() == expected
    desc = a.obtener_descripcion()
    assert "Armario 'Arm1'" in desc
    assert "Espejos=Sí" in desc or "Espejos='Sí'" in desc


def test_armario_atributos_y_defaults():
    a = Armario("Arm2", "Pino", "Blanco", 150.0, num_puertas=2)
    # atributos expuestos
    assert hasattr(a, "num_puertas")
    assert hasattr(a, "num_cajones")
    assert a.num_cajones == 0
    # calcular_precio funciona con valores por defecto
    precio = a.calcular_precio()
    assert isinstance(precio, int)


def test_abstract_almacenamiento_behavior():
    # Crear una implementación concreta mínima para la clase abstracta
    from src.models.categorias.almacenamiento import Almacenamiento

    class DummyAlm(Almacenamiento):
        def calcular_precio(self):
            # usar el factor de almacenamiento como multiplicador
            return round(self.precio_base * self.calcular_factor_almacenamiento(), 2)

        def obtener_descripcion(self):
            return f"Dummy {self.nombre} - {self.obtener_info_almacenamiento()}"

    d = DummyAlm("D1", "Metal", "Gris", 100.0, 2, 120.0)
    assert d.num_compartimentos == 2
    assert d.capacidad_litros == 120.0

    # factor de almacenamiento > 1
    factor = d.calcular_factor_almacenamiento()
    assert factor > 1.0

    info = d.obtener_info_almacenamiento()
    assert "Compartimentos" in info

    # setters validación
    with pytest.raises(ValueError):
        d.num_compartimentos = 0

    with pytest.raises(ValueError):
        d.capacidad_litros = -5
