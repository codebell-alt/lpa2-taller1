from src.models.concretos.mesa import Mesa


def test_calcular_area_y_factor():
    m = Mesa("MesaTest", "Roble", "Marrón", 200.0, "rectangular", 100.0, 50.0, 75.0, 4)
    area = m.calcular_area()
    assert area == 100.0 * 50.0
    factor = m.calcular_factor_tamaño()
    assert factor > 0


def test_setters_validacion():
    m = Mesa("MesaTest", "Roble", "Marrón", 200.0)
    try:
        m.largo = -10
    except ValueError:
        pass
    else:
        raise AssertionError("Asignación de largo inválido no lanzó ValueError")
