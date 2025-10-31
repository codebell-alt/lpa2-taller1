import pytest
from src.models.concretos.cama import Cama


class TestCama:
    @pytest.fixture
    def cama_basica(self):
        return Cama("Cama", "Madera", "Blanco", 300.0)

    def test_instanciacion(self, cama_basica):
        assert cama_basica.nombre == "Cama"
        assert cama_basica.tamaño == "individual"

    def test_tamano_setter_invalid(self, cama_basica):
        with pytest.raises(ValueError):
            cama_basica.tamaño = "gigante"

    def test_calcular_precio_con_colchon(self, cama_basica):
        cama_basica._incluye_colchon = True
        precio = cama_basica.calcular_precio()
        assert precio >= cama_basica.precio_base

    def test_precio_por_tamanos_y_extras(self, cama_basica):
        # probar tamaños y extras
        c = Cama(
            "C2",
            "Madera",
            "Blanco",
            200.0,
            tamaño="matrimonial",
            incluye_colchon=True,
            tiene_cabecera=True,
        )
        precio = c.calcular_precio()
        assert precio == round(200.0 + 200 + 300 + 100, 2)

        c.tamaño = "king"
        assert c.tamaño == "king"

    def test_obtener_descripcion_contiene_campos(self, cama_basica):
        desc = cama_basica.obtener_descripcion()
        assert "Cama:" in desc
        assert "Precio final" in desc
