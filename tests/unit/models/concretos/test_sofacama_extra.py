import pytest
from src.models.concretos.sofacama import SofaCama


class TestSofaCamaExtra:

    def test_tamaño_normalization_and_properties(self):
        s = SofaCama("Sofa1", "Tela", "Gris", 1000.0, 3, "Tela", "Queen", True, "hidraulico")
        assert s.tamaño_cama == "queen"
        assert s.tamaño_cama_sofacama == "queen"
        assert s.modo_actual == "sofa"

    def test_conversion_methods(self):
        s = SofaCama("Sofa2", "Tela", "Beige", 800.0, 2, "Tela", "matrimonial", False, "plegable")
        # convertir a cama
        msg = s.convertir_a_cama()
        assert "convertido a cama" in msg.lower() or "convertir" in msg.lower()
        assert s.modo_actual == "cama"
        # convertir a sofa
        msg2 = s.convertir_a_sofa()
        assert "convertida a sofá" in msg2.lower() or "convertida a sofa" in msg2.lower() or "convertir" in msg2.lower()
        assert s.modo_actual == "sofa"

    def test_calcular_precio_branches(self):
        s1 = SofaCama("S1", "Tela", "Negro", 500.0, 2, "Tela", "matrimonial", True, "hidraulico")
        p1 = s1.calcular_precio()
        # baseline should be > precio_base because of cama + colchón + mecanismo hidraulico
        assert p1 > 500
        s2 = SofaCama("S2", "Tela", "Negro", 500.0, 2, "Tela", "queen", True, "electrico")
        p2 = s2.calcular_precio()
        assert p2 > p1

    def test_calcular_factor_comodidad_and_errors(self):
        s = SofaCama("S3", "Tela", "Negro", 600.0, 2, "Cuero", "king", True, "electrico")
        # tiene material_tapizado 'Cuero' -> extra
        f = s.calcular_factor_comodidad()
        assert f > 1.0
        # invalid capacidad_personas leads to TypeError in factor
        s_bad = SofaCama("S4", "Tela", "Negro", 600.0, 2, "Tela", "matrimonial", True, "plegable")
        # Forcing an invalid internal value to exercise the error branch
        s_bad._capacidad_personas = "not_an_int"
        with pytest.raises(TypeError):
            s_bad.calcular_factor_comodidad()
