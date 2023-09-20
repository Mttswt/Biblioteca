class Persona:
    def __init__(self, nombre,sede):
        self.nombre = nombre
        self.sede = sede

class Estudiante(Persona):
    def __init__(self, nombre, carrera,sede):
        super().__init__(nombre)
        self.carrera = carrera

class Docente(Persona):
    def __init__(self, nombre, departamento,sede):
        super().__init__(nombre)
        self.departamento = departamento

class Administrativo(Persona):
    def __init__(self, nombre,sede):
        super().__init__(nombre)
