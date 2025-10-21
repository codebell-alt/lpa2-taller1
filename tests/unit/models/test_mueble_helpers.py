import pytest
from src.models.mueble import Mueble

class Dummy(Mueble):
    def calcular_precio(self):
        return 10.0
    def obtener_descripcion(self):
        return "dummy"

class TestMuebleHelpers:
    def test_dummy_implementation(self):
        d = Dummy("X","Y","Z", 5.0)
        assert d.calcular_precio() == 10.0
        assert d.obtener_descripcion() == "dummy"
