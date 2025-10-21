import pytest
from src.models.composicion.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla

class TestComedorAdditional:
    @pytest.fixture
    def comedor(self):
        mesa = Mesa("Mesa Extra", "Pino", "Natural", 180.0, "rectangular", 100.0, 80.0, 75.0, 4)
        sillas = [Silla("Silla E", "Pino", "Natural", 45.0, 4, "Pino") for _ in range(3)]
        return Comedor("Comedor E", mesa, sillas)

    def test_agregar_quitar_silla(self, comedor):
        s = Silla("Nueva","Pino","Natural",50.0,4,"Pino")
        res = comedor.agregar_silla(s)
        assert "agregada" in res
        res2 = comedor.quitar_silla()
        assert "removida" in res2

    def test_descripcion_y_precio(self, comedor):
        desc = comedor.obtener_descripcion_completa()
        assert "COMEDOR" in desc
        assert comedor.calcular_precio_total() > 0
