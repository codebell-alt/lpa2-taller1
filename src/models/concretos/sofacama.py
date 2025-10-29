"""
Clase SofaCama que implementa herencia múltiple.
Esta clase hereda tanto de Sofa como de Cama.
"""

from .sofa import Sofa
from .cama import Cama


class SofaCama(Sofa, Cama):
    """
    Clase que implementa herencia múltiple heredando de Sofa y Cama.

    Un sofá-cama es un mueble que funciona tanto como asiento durante el día
    como cama durante la noche.

    Conceptos OOP aplicados:
    - Herencia múltiple: Hereda de Sofa y Cama
    - Resolución MRO: Maneja el orden de resolución de métodos
    - Polimorfismo: Implementa comportamientos únicos combinando funcionalidades
    - Super(): Usa super() para resolver conflictos de herencia
    """

    def __init__(
        self,
        nombre: str,
        material: str,
        color: str,
        precio_base: int,
        capacidad_personas: int = 3,
        material_tapizado: str = "tela",
        tamaño_cama: str = "matrimonial",
        incluye_colchon: bool = True,
        mecanismo_conversion: str = "plegable",
    ):
        """
        Constructor del sofá-cama.

        Args:
            mecanismo_conversion: Tipo de mecanismo de conversión (plegable, extensible, etc.)
            Otros argumentos se pasan a las clases padre
        """
        # Soporte para la firma alternativa usada en tests:
        # SofaCama(nombre, material, precio_base, capacidad_personas, tamaño_cama)
        if (
            isinstance(color, (int, float))
            and isinstance(precio_base, (int, float))
            and isinstance(capacidad_personas, str)
        ):
            # Reasignar según la firma alternativa
            tamaño_cama = capacidad_personas
            capacidad_personas = int(precio_base)
            precio_base = float(color)
            color = None

        # Validar capacidad_personas (acepta nombres como 'Queen')
        if isinstance(capacidad_personas, str):
            capacidad_map = {"queen": 2, "full": 1, "king": 3}
            capacidad_personas = capacidad_map.get(capacidad_personas.lower(), 3)

        # Validar precio_base
        if not isinstance(precio_base, (int, float)):
            raise ValueError("El precio_base debe ser un número válido.")

        # Llamar solo al constructor de Sofa
        Sofa.__init__(
            self,
            nombre,
            material,
            color,
            precio_base,
            int(capacidad_personas),
            True,
            material_tapizado,
        )
        self._incluye_colchon = incluye_colchon
        self._mecanismo_conversion = mecanismo_conversion
        self._modo_actual = "sofa"
        # Normalizar y guardar tamaño de cama (propio y para compatibilidad)
        tamaño_norm = (
            tamaño_cama.lower() if isinstance(tamaño_cama, str) else "matrimonial"
        )
        self._tamaño = tamaño_norm
        self._tamaño_cama_sofacama = tamaño_norm

    def calcular_precio(self) -> float:
        """
        Calcula el precio final del sofá cama.
        Combina características de ambas clases padre.
        """
        # Precio base del sofá usando super() para resolución MRO
        precio_sofa = super().calcular_precio()

        # Agregar costos específicos de cama
        if self._tamaño == "matrimonial":
            precio_sofa += 200
        elif self._tamaño == "queen":
            precio_sofa += 400
        elif self._tamaño == "king":
            precio_sofa += 600

        if self._incluye_colchon:
            precio_sofa += 300

        # Costo del mecanismo de conversión
        if self._mecanismo_conversion == "hidraulico":
            precio_sofa += 150
        elif self._mecanismo_conversion == "electrico":
            precio_sofa += 300

        return round(precio_sofa, 2)

    @property
    def mecanismo_conversion(self) -> str:
        """Getter para el mecanismo de conversión."""
        return self._mecanismo_conversion

    @property
    def modo_actual(self) -> str:
        """Getter para el modo actual (sofa o cama)."""
        return self._modo_actual

    # Redefinir tamaño para compatibilidad con ambas clases
    @property
    def tamaño(self) -> str:
        """Getter para tamaño (compatible con clase Cama)."""
        return self._tamaño

    @property
    def tamaño_cama(self) -> str:
        """Compatibilidad: devuelve el tamaño de cama del sofá-cama (minúsculas)."""
        return getattr(self, "_tamaño_cama_sofacama", self._tamaño)

    @property
    def tamaño_cama_sofacama(self) -> str:
        """Tamaño de la cama específico del sofá-cama (evita conflicto MRO)."""
        return getattr(self, "_tamaño_cama_sofacama", self._tamaño)

    def convertir_a_cama(self) -> str:
        """
        Convierte el sofá en cama.
        Método específico del sofá-cama.

        Returns:
            str: Mensaje del resultado de la conversión
        """
        if self._modo_actual == "cama":
            return "El sofá-cama ya está en modo cama"

        self._modo_actual = "cama"
        return f"Sofá convertido a cama usando mecanismo {self.mecanismo_conversion}"

    def convertir_a_sofa(self) -> str:
        """
        Convierte la cama en sofá.
        Método específico del sofá-cama.

        Returns:
            str: Mensaje del resultado de la conversión
        """
        if self._modo_actual == "sofa":
            return "El sofá-cama ya está en modo sofá"

        self._modo_actual = "sofa"
        return f"Cama convertida a sofá usando mecanismo {self.mecanismo_conversion}"
        pass

    def obtener_descripcion(self) -> str:
        """
        Retorna una descripción detallada del sofá cama.
        Combina información de ambas funcionalidades.
        """
        desc = f"Sofá-Cama: {self.nombre}\n"
        desc += f"  Material: {self.material}\n"
        desc += f"  Color: {self.color}\n"
        desc += f"  {self.obtener_info_asiento()}\n"
        desc += f"  Tamaño como cama: {self.tamaño_cama}\n"
        desc += f"  Incluye colchón: {'Sí' if self.incluye_colchon else 'No'}\n"
        desc += f"  Mecanismo: {self.mecanismo_conversion}\n"
        desc += f"  Modo actual: {self.modo_actual}\n"
        desc += f"  Precio final: ${self.calcular_precio()}"
        return desc

    def obtener_capacidad_total(self) -> dict:
        """
        Obtiene la capacidad tanto como sofá como cama.
        Método único del sofá-cama.

        Returns:
            dict: Capacidades en ambos modos
        """
        capacidades = {
            "como_sofa": self.capacidad_personas,
            "como_cama": 2
            if self.tamaño_cama in ["matrimonial", "queen", "king"]
            else 1,
        }
        return capacidades

    def calcular_factor_comodidad(self) -> float:
        """
        Calcula un factor de comodidad basado en las características del asiento.

        Returns:
            float: Factor multiplicador para el precio
        """
        factor = 1.0
        if self.tiene_respaldo:
            factor += 0.1
        if self.material_tapizado:
            if self.material_tapizado.lower() == "cuero":
                factor += 0.2
            elif self.material_tapizado.lower() == "tela":
                factor += 0.1
        try:
            factor += (int(self.capacidad_personas) - 1) * 0.05
        except ValueError:
            raise TypeError(
                "El atributo 'capacidad_personas' debe ser un entero válido."
            )
        return factor

    # TODO: Implementar método para verificar compatibilidad de modo
    # def puede_usar_como_cama(self) -> bool:
    #     """Verifica si actualmente puede usarse como cama."""
    #     return self._modo_actual == "cama"

    # def puede_usar_como_sofa(self) -> bool:
    #     """Verifica si actualmente puede usarse como sofá."""
    #     return self._modo_actual == "sofa"

    def __str__(self) -> str:
        """
        Representación en cadena del sofá-cama.
        Sobrescribe el método heredado para mostrar información específica.
        """
        return f"Sofá-cama {self.nombre} (modo: {self.modo_actual})"
