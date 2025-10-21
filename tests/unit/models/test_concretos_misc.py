import pytest
from src.models.concretos.armario import Armario
from src.models.concretos.cajonera import Cajonera
from src.models.concretos.escritorio import Escritorio
from src.models.concretos.sillon import Sillon
from src.models.concretos.comedor import Comedor as ComedorConcreto
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla

class TestConcretosMisc:
    def test_armario_precio_y_descripcion(self):
        a = Armario("Arm1","Madera","Blanco",200,3,2,True)
        assert a.calcular_precio() == 200 + 3*50 + 2*30 + 100
        assert "Armario 'Arm1'" in a.obtener_descripcion()

    def test_cajonera_precio_y_descripcion(self):
        c = Cajonera("Caj1","Metal","Gris",120,4,True)
        assert c.calcular_precio() == 120 + 4*20 + 30
        assert "Cajonera 'Caj1'" in c.obtener_descripcion()

    def test_escritorio_varios(self):
        e = Escritorio("Esc1","Madera","Negro",150, forma="ovalada", tiene_cajones=True, num_cajones=2, largo=1.6, tiene_iluminacion=True)
        precio = e.calcular_precio()
        assert precio >= 150
        assert "Escritorio 'Esc1'" in e.obtener_descripcion()

    def test_sillon_recargos(self):
        s = Sillon("Sill1","Tela","Azul",300, capacidad_personas=2, tiene_respaldo=True, material_tapizado="tela", tiene_brazos=True, es_reclinable=True, tiene_reposapiés=True)
        precio = s.calcular_precio()
        assert precio == 300 + 200 + 100 + 250 + 80

    def test_concreto_comedor(self):
        mesa = Mesa("M","Roble","N",200.0, "rectangular",120.0,80.0,75.0,4)
        sillas = [Silla("S","Roble","N",50.0,4,"Roble") for _ in range(2)]
        c = ComedorConcreto(mesa, sillas)
        assert c.cantidad_sillas() == 2
        total = c.calcular_precio_total()
        assert total == mesa.calcular_precio() + sum(s.calcular_precio() for s in sillas)
