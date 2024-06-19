import Producto

class Alimento(Producto) :
    productor = ''
    distribuidor = ''

    def __str__ (self) :
        return f"REFERENCIA\t {self.referencia}\n" \
                f"NOMBRE\t {self.nombre}\n" \
                f"PVP\t {self.pvp}\n" \
                f"DESCRIPCIÓN\t {self.descripcion}\n" \
                f"PRODUCTOR\t\t {self.productor}\n" \
                f"DISTRIBUIDOR\t\t {self.distribuidor}\n"