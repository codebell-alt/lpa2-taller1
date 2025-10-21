import pytest
from src.models.mueble import Mueble


class DummyMueble(Mueble):
    def calcular_precio(self) -> float:
        return self.precio_base

    def obtener_descripcion(self) -> str:
        return f"Dummy: {self.nombre}"


def test_mueble_es_abstracta_no_instanciable():
    with pytest.raises(TypeError):
        Mueble("n", "m", "c", 10.0)


def test_dummy_mueble_behaviour_and_setters():
    d = DummyMueble("Nombre", "Madera", "Rojo", 100.0)
    assert str(d) == "Nombre de Madera en color Rojo"
    assert "Mueble(" in repr(d)

    # setters validos
    d.nombre = " Nuevo "
    assert d.nombre == "Nuevo"
    d.material = " Metal "
    assert d.material == "Metal"
    d.color = " Azul "
    assert d.color == "Azul"
    d.precio_base = 50
    assert d.precio_base == 50

    # setters invalidos
    with pytest.raises(ValueError):
        d.nombre = ""
    with pytest.raises(ValueError):
        d.material = ""
    with pytest.raises(ValueError):
        d.color = ""
    with pytest.raises(ValueError):
        d.precio_base = -10
