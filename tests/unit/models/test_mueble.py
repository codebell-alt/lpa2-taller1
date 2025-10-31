from src.models.mueble import Mueble
import pytest


class ConcreteMueble(Mueble):
    def calcular_precio(self) -> float:
        return round(self.precio_base * 1.1, 2)

    def obtener_descripcion(self) -> str:
        return f"Concrete {self.nombre}"


def test_getters_setters_and_validation():
    m = ConcreteMueble("MesaX", "Roble", "Natural", 100.0)
    assert m.nombre == "MesaX"
    assert m.material == "Roble"
    assert m.color == "Natural"
    assert m.precio_base == 100.0

    # nombre vacio
    with pytest.raises(ValueError):
        m.nombre = "  "

    # material vacío
    with pytest.raises(ValueError):
        m.material = ""

    # color vacío
    with pytest.raises(ValueError):
        m.color = None

    # precio_base negativo
    with pytest.raises(ValueError):
        m.precio_base = -10

    # __str__ and __repr__
    assert "MesaX" in str(m)
    r = repr(m)
    assert "Mueble(" in r or "Concrete" in r


def test_calcular_precio_y_descripcion():
    m = ConcreteMueble("P", "M", "C", 50.0)
    assert m.calcular_precio() == 55.0
    assert "Concrete" in m.obtener_descripcion()
