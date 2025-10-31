
from src.models.concretos.cajonera import Cajonera


def test_cajonera_precio_con_ruedas():
	c = Cajonera("Cajonera", "Madera", "Natural", 150, num_cajones=4, tiene_ruedas=True)
	precio = c.calcular_precio()
	assert precio == 150 + 4 * 20 + 30

def test_obtener_descripcion_contains_name():
	c = Cajonera("Cajonera", "Madera", "Natural", 100)
	assert "Cajonera 'Cajonera'" in c.obtener_descripcion()
