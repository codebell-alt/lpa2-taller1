"""
Clase concreta Silla.
Implementa un mueble de asiento específico para una persona.
"""

from ..categorias.asientos import Asiento


class Silla(Asiento):
    """Representa una silla concreta.

    Añade atributos como número de patas y tipo de madera y rasgos de
    oficina (altura regulable, ruedas).
    """

    def __init__(
        self,
        nombre: str,
        material: str,
        color: str,
        precio_base: float,
        numero_patas: int = 4,
        tipo_madera: str = "Madera",
        tiene_respaldo: bool = True,
        material_tapizado: str = None,
        altura_regulable: bool = False,
        tiene_ruedas: bool = False,
    ):
        # Silla siempre tiene capacidad de 1 persona
        super().__init__(
            nombre, material, color, precio_base, 1, tiene_respaldo, material_tapizado
        )
        self._numero_patas = numero_patas
        self._tipo_madera = tipo_madera
        self._altura_regulable = altura_regulable
        self._tiene_ruedas = tiene_ruedas

    @property
    def altura_regulable(self) -> bool:
        return self._altura_regulable

    @altura_regulable.setter
    def altura_regulable(self, value: bool) -> None:
        self._altura_regulable = value

    @property
    def tiene_ruedas(self) -> bool:
        return self._tiene_ruedas

    @tiene_ruedas.setter
    def tiene_ruedas(self, value: bool) -> None:
        self._tiene_ruedas = value

    @property
    def numero_patas(self) -> int:
        return self._numero_patas

    @property
    def tipo_madera(self) -> str:
        return self._tipo_madera

    def calcular_precio(self) -> float:
        """Calcula el precio final de la silla aplicando factores de comodidad y extras."""
        precio = self.precio_base

        # Extras
        if self.altura_regulable:
            precio += 10.0
        if self.tiene_ruedas:
            precio += 15.0

        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        desc = f"Silla: {self.nombre}\n"
        desc += f"  Material: {self.material}\n"
        desc += f"  Color: {self.color}\n"
        desc += f"  {self.obtener_info_asiento()}\n"
        desc += f"  Altura regulable: {'Sí' if self.altura_regulable else 'No'}\n"
        desc += f"  Ruedas: {'Sí' if self.tiene_ruedas else 'No'}\n"
        desc += f"  Precio final: ${self.calcular_precio()}"
        return desc

    def regular_altura(self, nueva_altura: int) -> str:
        if not self.altura_regulable:
            return "Esta silla no tiene altura regulable"
        if nueva_altura < 40 or nueva_altura > 100:
            return "La altura debe estar entre 40 y 100 cm"
        return f"Altura ajustada a {nueva_altura} cm"

    def es_silla_oficina(self) -> bool:
        return self.altura_regulable and self.tiene_ruedas
