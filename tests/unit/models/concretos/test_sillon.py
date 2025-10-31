from src.models.concretos.sillon import Sillon


def test_sillon_instanciacion_y_precio():
    s = Sillon(
        "Sillón Relax",
        "Cuero",
        "Negro",
        800,
        capacidad_personas=2,
        material_tapizado="Cuero",
        tiene_brazos=True,
        es_reclinable=True,
        tiene_reposapiés=True,
    )
    assert s.nombre == "Sillón Relax"
    precio = s.calcular_precio()
    # precio_base + tapizado + brazos + reclinable + reposapiés
    assert precio == 800 + 200 + 100 + 250 + 80


def test_obtener_descripcion_contiene_campos():
    s = Sillon("Sillón Simple", "Tela", "Gris", 300)
    desc = s.obtener_descripcion()
    assert "Sillón 'Sillón Simple'" in desc
    assert "Capacidad=" in desc
