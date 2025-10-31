import pytest
from src.models.composicion.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla
from src.services.tienda import TiendaMuebles as Tienda
from unittest.mock import Mock, patch


class TestComedor:
    @pytest.fixture
    def comedor_basico(self):
        mesa = Mesa(
            "Mesa Comedor",
            "Roble",
            "Marrón",
            200.0,
            "Rectangular",
            120.0,
            80.0,
            75.0,
            6,
        )
        sillas = [
            Silla("Silla Comedor", "Roble", "Marrón", 50.0, 4, "Roble")
            for _ in range(6)
        ]
        return Comedor("Comedor Familiar", mesa, sillas)

    def test_composicion_correcta(self, comedor_basico):
        assert comedor_basico.mesa is not None
        assert len(comedor_basico.sillas) == 6
        assert isinstance(comedor_basico.mesa, Mesa)
        assert all(isinstance(silla, Silla) for silla in comedor_basico.sillas)

    def test_calcular_precio_total(self, comedor_basico):
        precio_total = comedor_basico.calcular_precio_total()
        # Calcular el precio esperado sumando el precio calculado de la mesa y de cada silla
        precio_esperado = comedor_basico.mesa.calcular_precio() + sum(
            s.calcular_precio() for s in comedor_basico.sillas
        )
        assert precio_total == precio_esperado

    def test_agregar_silla_tipo_invalido(self, comedor_basico):
        # intentar agregar una mesa en lugar de silla debe fallar
        from src.models.concretos.mesa import Mesa

        mesa = Mesa("NoSilla", "Pino", "Natural", 100.0, "rectangular", 50, 40, 70, 4)
        res = comedor_basico.agregar_silla(mesa)
        assert "Error: Solo se pueden agregar objetos de tipo Silla" in res

    def test_agregar_silla_capacidad_maxima(self):
        # crear comedor con mesa capacidad 2 y ya 2 sillas
        mesa = Mesa(
            "Peque", "Pino", "Natural", 120.0, "rectangular", 80.0, 40.0, 75.0, 2
        )
        s1 = Silla("S1", "Pino", "Natural", 30.0)
        s2 = Silla("S2", "Pino", "Natural", 30.0)
        comedor = Comedor("Pequeño", mesa, [s1, s2])
        s3 = Silla("S3", "Pino", "Natural", 30.0)
        res = comedor.agregar_silla(s3)
        assert "No se pueden agregar más sillas" in res

    def test_quitar_silla_vacia_e_indice_invalido(self):
        mesa = Mesa("M", "Pino", "Natural", 100.0, "rectangular", 50, 40, 70, 4)
        comedor = Comedor("Vacio", mesa, [])
        assert comedor.quitar_silla() == "No hay sillas para quitar"

        # índice inválido
        comedor2 = Comedor("Uno", mesa, [Silla("S", "Pino", "N", 20.0)])
        assert comedor2.quitar_silla(10) == "Índice de silla inválido"

    def test_obtener_descripcion_incluye_descuento(self, comedor_basico):
        desc = comedor_basico.obtener_descripcion_completa()
        assert "PRECIO TOTAL" in desc
        assert "descuento" in desc.lower() or "set completo" in desc.lower()

    def test_obtener_resumen_y_materiales(self):
        mesa = Mesa(
            "MesaR", "Roble", "Marrón", 150.0, "rectangular", 100.0, 50.0, 75.0, 4
        )
        sillas = [
            Silla("A", "Roble", "Marrón", 40.0, material_tapizado="Tela")
            for _ in range(2)
        ]
        comedor = Comedor("Resumen", mesa, sillas)
        resumen = comedor.obtener_resumen()
        assert resumen["nombre"] == "Resumen"
        assert resumen["total_muebles"] == 3
        assert isinstance(resumen["materiales_utilizados"], list)

    def test_calcular_capacidad_maxima_default_y_len_str(self):
        # crear una "mesa" sin atributo capacidad_personas
        class DummyMesa:
            def __init__(self):
                self.material = "MDF"

            def calcular_precio(self):
                return 10.0

            def obtener_descripcion(self):
                return "DummyMesa"

        dummy = DummyMesa()
        comedor = Comedor("D", dummy, [])
        # capacidad máxima por defecto es 6
        # intentar agregar sillas hasta 6 y la séptima debe fallar
        for i in range(6):
            comedor.agregar_silla(Silla(f"s{i}", "MDF", "N", 10.0))
        res = comedor.agregar_silla(Silla("s6", "MDF", "N", 10.0))
        assert "No se pueden agregar más sillas" in res
        assert len(comedor) == 7  # 1 mesa + 6 sillas
        assert "Comedor" in str(comedor)


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

        with patch("builtins.print") as mock_print:
            resultado = tienda_vacia.vender_producto("Silla Mock")

            assert resultado is True
            assert len(tienda_vacia.inventario) == 0
            mock_print.assert_called_once()

    def test_vender_producto_inexistente(self, tienda_vacia):
        resultado = tienda_vacia.vender_producto("Producto Inexistente")
        assert resultado is False
