from src.models.concretos.armario import Armario


def test_armario_precio_y_descripcion():
    # Armario concrete implements price calculation and description
    a = Armario(
        "Arm1",
        "Pino",
        "Natural",
        300.0,
        num_puertas=3,
        num_cajones=2,
        tiene_espejos=True,
    )
    # precio esperado: base + puertas*50 + cajones*30 + espejos(100)
    expected = 300 + 3 * 50 + 2 * 30 + 100
    assert a.calcular_precio() == expected
    desc = a.obtener_descripcion()
    assert "Armario 'Arm1'" in desc
    assert "Espejos=Sí" in desc or "Espejos='Sí'" in desc


def test_armario_atributos_y_defaults():
    a = Armario("Arm2", "Pino", "Blanco", 150.0, num_puertas=2)
    # atributos expuestos
    assert hasattr(a, "num_puertas")
    assert hasattr(a, "num_cajones")
    assert a.num_cajones == 0
    # calcular_precio funciona con valores por defecto
    precio = a.calcular_precio()
    assert isinstance(precio, int)
