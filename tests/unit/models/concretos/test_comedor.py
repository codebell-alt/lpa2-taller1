
from src.models.concretos.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla


def test_comedor_calcular_precio_total():
	mesa = Mesa("MesaPrueba", "Roble", "Marrón", 200.0, "rectangular", 120.0, 80.0, 75.0, 4)
	sillas = [Silla("Silla", "Madera", "Marrón", 50.0) for _ in range(4)]
	comedor = Comedor(mesa, sillas)
	esperado = mesa.calcular_precio() + sum(s.calcular_precio() for s in sillas)
	assert comedor.calcular_precio_total() == esperado

def test_agregar_quitar_silla():
	mesa = Mesa("MesaPrueba", "Roble", "Marrón", 200.0)
	comedor = Comedor(mesa)
	s = Silla("Silla", "Madera", "Marrón", 50.0)
	comedor.agregar_silla(s)
	assert comedor.cantidad_sillas() == 1
	comedor.quitar_silla(s)
	assert comedor.cantidad_sillas() == 0
