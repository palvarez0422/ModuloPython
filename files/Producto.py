
class Producto:
    def __init__ (self, referencia, nombre, pvp, descripcion) :
        self.referencia = referencia
        self.nombre = nombre
        self. pvp = pvp
        self.descripcion = descripcion

    def __str__ (self) :
        return f"REFERENCIA\t {self.referencia}\n" \
                f"NOMBRE\t {self.nombre}\n" \
                f"PVP\t {self.pvp}\n" \
                f"DESCRIPCIÓN\t {self.descripcion}\n"

