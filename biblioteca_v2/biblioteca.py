# biblioteca.py
from libro import Libro

class Biblioteca:
    def __init__(self, sede):
        self.sede = sede
        self.catalogo = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo == titulo:
                return libro

    def libros_disponibles(self):
        libros_disponibles = [libro for libro in self.catalogo if libro.disponible]
        return libros_disponibles

    def libros_prestados(self):
        libros_prestados = [libro for libro in self.catalogo if not libro.disponible]
        return libros_prestados

    def cargar_libros_desde_archivo(self, archivo):
        try:
            with open(archivo, "r") as file:
                for line in file:
                    titulo, autor = line.strip().split(",")
                    libro = Libro(titulo, autor)
                    self.agregar_libro(libro)
        except FileNotFoundError:
            print(f"El archivo {archivo} no fue encontrado.")
