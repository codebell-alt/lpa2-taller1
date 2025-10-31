
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
