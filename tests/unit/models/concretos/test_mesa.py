
import pytest
from src.models.concretos.mesa import Mesa


class TestMesa:
	@pytest.fixture
	def mesa_basica(self):
		return Mesa("Mesa", "Roble", "Marrón", 200.0, "rectangular", 120.0, 80.0, 75.0, 6)

	def test_instanciacion(self, mesa_basica):
		assert mesa_basica.nombre == "Mesa"
		assert mesa_basica.material == "Roble"
		assert mesa_basica.capacidad_personas == 6

	def test_forma_setter_invalid(self, mesa_basica):
		with pytest.raises(ValueError):
			mesa_basica.forma = "triangular"

	def test_calcular_precio_rectangular(self, mesa_basica):
		precio = mesa_basica.calcular_precio()
		assert isinstance(precio, float)
		# base price should be at least the precio_base
		assert precio >= mesa_basica.precio_base

