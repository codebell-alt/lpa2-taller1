
from src.models.concretos.armario import Armario


def test_armario_calcular_precio():
	a = Armario("Armario", "MDF", "Blanco", 400, num_puertas=3, num_cajones=2, tiene_espejos=True)
	precio = a.calcular_precio()
	# precio_base + puertas*50 + cajones*30 + espejos*100
	assert precio == 400 + 3 * 50 + 2 * 30 + 100

def test_obtener_descripcion_contains_fields():
	a = Armario("Armario", "MDF", "Blanco", 200)
	desc = a.obtener_descripcion()
	assert "Armario 'Armario'" in desc
