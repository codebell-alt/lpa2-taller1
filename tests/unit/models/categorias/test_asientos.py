from src.models.concretos.silla import Silla


def test_calcular_factor_comodidad_basico():
    s = Silla(
        "Silla Test",
        "Madera",
        "Natural",
        50.0,
        numero_patas=4,
        tipo_madera="Madera",
        tiene_respaldo=True,
        material_tapizado="tela",
    )
    # calcular_factor_comodidad está definido en Asiento y usado por Silla
    factor = s.calcular_factor_comodidad()
    assert factor >= 1.0


def test_obtener_info_asiento():
    s = Silla(
        "Silla Test",
        "Madera",
        "Natural",
        50.0,
        numero_patas=4,
        tipo_madera="Madera",
        tiene_respaldo=False,
    )
    info = s.obtener_info_asiento()
    assert "Capacidad" in info
    assert "Respaldo" in info
