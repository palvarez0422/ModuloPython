import Producto

class Libro(Producto) :
    isbn = ''
    autor = ''

    def __str__ (self) :
        return  f"REFERENCIA\t {self.referencia}\n" \
                f"NOMBRE\t\t {self.nombre}\n" \
                f"ISBN\t\t {self.isbn}\n" \
                f"AUTOR\t\t {self.autor}\n"