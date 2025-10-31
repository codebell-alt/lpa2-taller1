from src.models.concretos.sofacama import SofaCama


class TestSofaCama:
    def test_herencia_multiple_y_propiedades_basicas(self):
        sofa_cama = SofaCama("Sofá Cama Moderno", "Tela", 500.0, 2, "Queen")

        # Verificar atributos de Sofa
        assert sofa_cama.capacidad_personas == 2

        # Verificar atributos de Cama (propiedad de compatibilidad)
        assert sofa_cama.tamaño_cama_sofacama == "queen"

        # Verificar existencia de métodos
        assert hasattr(sofa_cama, "convertir_a_cama")

    def test_precio_por_tamaño_y_mecanismo(self):
        base = 400.0
        s_mat = SofaCama(
            "S1", "Tela", "Azul", base, 3, "tela", "matrimonial", True, "plegable"
        )
        s_queen = SofaCama(
            "S2", "Tela", "Azul", base, 3, "tela", "queen", True, "plegable"
        )
        s_king = SofaCama(
            "S3", "Tela", "Azul", base, 3, "tela", "king", True, "plegable"
        )

        assert (
            s_king.calcular_precio()
            > s_queen.calcular_precio()
            > s_mat.calcular_precio()
        )

        # mecanismo hidraulico y electrico deben incrementar el precio respecto a plegable
        s_hid = SofaCama(
            "Hid", "Tela", "Azul", base, 3, "tela", "queen", True, "hidraulico"
        )
        s_elec = SofaCama(
            "Elec", "Tela", "Azul", base, 3, "tela", "queen", True, "electrico"
        )
        assert (
            s_elec.calcular_precio()
            > s_hid.calcular_precio()
            > s_queen.calcular_precio()
        )

    def test_convertir_a_cama_y_sofa(self):
        s = SofaCama("Convert", "Tela", "Negro", 300.0)
        assert s.modo_actual == "sofa"
        msg = s.convertir_a_cama()
        assert "convertido a cama" in msg or s.modo_actual == "cama"
        # convertir de nuevo
        msg2 = s.convertir_a_cama()
        assert "ya está en modo cama" in msg2
        # volver a sofá
        back = s.convertir_a_sofa()
        assert "convertida a sofá" in back or s.modo_actual == "sofa"

    def test_constructor_firma_alternativa(self):
        # activar la firma alternativa: pasar color numérico, precio_base numérico y capacidad como str
        alt = SofaCama("Alt", "Tela", 350.0, 2, "queen")
        # tras normalización, tamaño debe ser 'queen' y capacidad 2
        assert alt.tamaño_cama == "queen"
        assert isinstance(alt.capacidad_personas, int)

    def test_incluir_colchon_flag_y_descripcion(self):
        s_no_col = SofaCama(
            "NoCol",
            "Tela",
            "Gris",
            250.0,
            3,
            "tela",
            "matrimonial",
            incluye_colchon=False,
        )
        assert s_no_col.incluye_colchon is False
        desc = s_no_col.obtener_descripcion()
        assert "Incluye colchón" in desc

    def test_obtener_capacidad_total_y_factor_comodidad(self):
        s = SofaCama("Comod", "Cuero", "Negro", 500.0, 4, "cuero", "queen", True)
        caps = s.obtener_capacidad_total()
        assert "como_sofa" in caps and "como_cama" in caps

        # factor comodidad: cuero + respaldo + capacidad
        factor = s.calcular_factor_comodidad()
        # cálculo manual aproximado: 1 + 0.1(respaldo) + 0.2(cuero) + (cap-1)*0.05
        expected = 1.0 + 0.1 + 0.2 + (int(s.capacidad_personas) - 1) * 0.05
        assert abs(factor - round(expected, 2)) < 0.01

    def test_str_representation(self):
        s = SofaCama("StrTest", "Tela", "Blanco", 320.0)
        assert "Sofá-cama" in str(s) or "StrTest" in str(s)
