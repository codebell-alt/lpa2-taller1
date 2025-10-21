import pytest
from src.models.composicion.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla
from src.services.tienda import TiendaMuebles as Tienda

class TestComedor:
    @pytest.fixture
    def comedor_basico(self):
        mesa = Mesa("Mesa Comedor", "Roble", "Marrón", 200.0, "Rectangular", 120.0, 80.0, 75.0, 6)
        sillas = [Silla("Silla Comedor", "Roble", "Marrón", 50.0, 4, "Roble") for _ in range(6)]
        return Comedor("Comedor Familiar", mesa, sillas)

    def test_composicion_correcta(self, comedor_basico):    
        assert comedor_basico.mesa is not None
        assert len(comedor_basico.sillas) == 6
        assert isinstance(comedor_basico.mesa, Mesa)
        assert all(isinstance(silla, Silla) for silla in comedor_basico.sillas)

    def test_calcular_precio_total(self, comedor_basico):
        precio_total = comedor_basico.calcular_precio_total()
        # Calcular el precio esperado sumando el precio calculado de la mesa y de cada silla
        precio_esperado = comedor_basico.mesa.calcular_precio() + sum(s.calcular_precio() for s in comedor_basico.sillas)
        assert precio_total == precio_esperado

# Pruebas con Mocks
# tests/unit/services/test_tienda.py

import pytest
from unittest.mock import Mock, patch
from src.services.tienda import TiendaMuebles as Tienda
from src.models.concretos.silla import Silla

class TestTienda:
    @pytest.fixture
    def tienda_vacia(self):
        return Tienda()
    
    @pytest.fixture
    def silla_mock(self):
        mock_silla = Mock(spec=Silla)
        mock_silla.nombre = "Silla Mock"
        mock_silla.calcular_precio.return_value = 75.0
        return mock_silla
    
    def test_agregar_producto(self, tienda_vacia, silla_mock):
        tienda_vacia.agregar_producto(silla_mock)
        assert len(tienda_vacia.inventario) == 1
        assert tienda_vacia.inventario[0] == silla_mock
    
    def test_vender_producto_existente(self, tienda_vacia, silla_mock):
        tienda_vacia.agregar_producto(silla_mock)
        
        with patch('builtins.print') as mock_print:
            resultado = tienda_vacia.vender_producto("Silla Mock")
            
            assert resultado is True
            assert len(tienda_vacia.inventario) == 0
            mock_print.assert_called_once()
    
    def test_vender_producto_inexistente(self, tienda_vacia):
        resultado = tienda_vacia.vender_producto("Producto Inexistente")
        assert resultado is False