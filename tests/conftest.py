"""Fixtures compartidos para las pruebas unitarias.

Este archivo proporciona fixtures reutilizables para crear instancias
comunes (p. ej. tienda, armario, silla) y utilidades de mocking.
"""
import pytest

from src.services.tienda import TiendaMuebles
from src.models.concretos.armario import Armario
from src.models.concretos.silla import Silla


@pytest.fixture
def tienda():
    """Instancia limpia de TiendaMuebles para pruebas."""
    return TiendaMuebles("Tienda Test")


@pytest.fixture
def armario_basico():
    """Armario simple para usar en pruebas de categorías/servicios."""
    return Armario("Armario Test", "Pino", "Natural", 200.0, num_puertas=2)


@pytest.fixture
def silla_basica():
    """Silla simple para usar en pruebas de modelos y tienda."""
    return Silla("Silla Test", "Madera", "Negra", 45.0)
