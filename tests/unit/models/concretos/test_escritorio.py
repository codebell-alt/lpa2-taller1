from src.models.concretos.escritorio import Escritorio


def test_escritorio_precio_largo_y_iluminacion():
    e = Escritorio(
        "Escritorio",
        "Madera",
        "Negro",
        250,
        forma="rectangular",
        tiene_cajones=True,
        num_cajones=2,
        largo=1.6,
        tiene_iluminacion=True,
    )
    precio = e.calcular_precio()
    # base + cajones*25 + largo>1.5 + iluminacion
    assert precio == 250 + 2 * 25 + 50 + 40


def test_descripcion_contains_fields():
    e = Escritorio("Escritorio", "Madera", "Negro", 200)
    assert "Escritorio 'Escritorio'" in e.obtener_descripcion()
