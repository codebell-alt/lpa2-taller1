"""Implementación limpia de TiendaMuebles — versión única y compacta.

Este archivo fue reemplazado para eliminar duplicados y marcadores de
merge que estaban provocando SyntaxError. Contiene una clase sencilla
pensada para ser usada por los tests unitarios del taller.
"""

from typing import Any, Dict, List, Optional


class TiendaMuebles:
    def __init__(self, nombre: str = "Tienda") -> None:
        self.nombre: str = nombre
        self._inventario: List[Any] = []
        self._descuentos: Dict[str, float] = {}
        self._total_muebles_vendidos: int = 0
        self._valor_total_ventas: float = 0.0

    @property
    def inventario(self) -> List[Any]:
        return self._inventario

    def agregar_producto(self, producto: Any) -> None:
        if producto is None:
            return
        self._inventario.append(producto)

    def agregar_mueble(self, mueble: Any) -> str:
        if mueble is None:
            return "Error: mueble None"
        try:
            precio = mueble.calcular_precio()
        except Exception:
            return "Error al calcular precio"
        try:
            if precio <= 0:
                return "Error: precio inválido"
        except Exception:
            return "Error al validar precio"
        self._inventario.append(mueble)
        return "mueble agregado"

    def agregar_comedor(self, comedor: Any) -> str:
        if comedor is None:
            return "Error: comedor None"
        try:
            res = self.agregar_mueble(comedor)
            if "agregado" in res:
                return res
        except Exception:
            pass
        mesa = getattr(comedor, "mesa", None)
        sillas = getattr(comedor, "sillas", []) or []
        if mesa is not None:
            self.agregar_mueble(mesa)
        for s in sillas:
            self.agregar_producto(s)
        return "comedor agregado"

    def realizar_venta(self, mueble: Any, cliente: Optional[str] = None) -> Any:
        try:
            precio_original = mueble.calcular_precio()
        except Exception:
            return {"error": "no se pudo calcular precio"}
        tipo = type(mueble).__name__.lower()
        descuento_key: Optional[str] = None
        if f"{tipo}s" in self._descuentos:
            descuento_key = f"{tipo}s"
        elif tipo in self._descuentos:
            descuento_key = tipo
        descuento = int(self._descuentos.get(descuento_key, 0)) if descuento_key else 0
        precio_final = round(precio_original * (1 - descuento / 100.0), 2)
        self._total_muebles_vendidos += 1
        try:
            self._valor_total_ventas += precio_final
        except Exception:
            pass
        return {
            "mueble": getattr(mueble, "nombre", str(mueble)),
            "precio_original": precio_original,
            "descuento": descuento,
            "precio_final": precio_final,
            "cliente": cliente,
        }

    def calcular_valor_inventario(self) -> float:
        total = 0.0
        for p in self._inventario:
            try:
                total += float(p.calcular_precio())
            except Exception:
                continue
        return round(total, 2)

    def generar_reporte_inventario(self) -> str:
        lines: List[str] = [
            f"REPORTE - {self.nombre}",
            f"Total: {len(self._inventario)}",
        ]
        for p in self._inventario:
            lines.append(f"- {getattr(p, 'nombre', repr(p))} ({type(p).__name__})")
        return "\n".join(lines)

    def agregar_producto_directo(self, producto: Any) -> None:
        """Alias para tests que quieran añadir sin pasar por validaciones extra."""
        self.agregar_producto(producto)

    def vender_producto(self, nombre_producto: str) -> bool:
        """Vender un producto por nombre. Imprime un mensaje y devuelve True si se vendió, False si no se encontró."""
        for i, p in enumerate(self._inventario):
            try:
                nombre = getattr(p, "nombre", None)
            except Exception:
                nombre = None
            if nombre == nombre_producto or str(p) == nombre_producto:
                # registrar venta (usar realizar_venta para consistencia)
                _ = self.realizar_venta(p)
                # remover del inventario
                try:
                    del self._inventario[i]
                except Exception:
                    pass
                print(f"Vendido: {nombre_producto}")
                return True
        return False
