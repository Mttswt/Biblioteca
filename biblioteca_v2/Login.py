from libro import Libro
from biblioteca import Biblioteca
from persona import Estudiante, Docente, Administrativo

def iniciar_sesion():
    print("Bienvenido al sistema de biblioteca.")
    while True:
        print("Por favor, seleccione su clase:")
        print("1. Estudiante")
        print("2. Docente")
        print("3. Administrativo")
        opcion_clase = input("Seleccione su clase (1/2/3): ")

        if opcion_clase == "1":
           nombre = input("Ingrese su nombre: ")
           carrera = input("Ingrese su carrera: ")
           usuario = Estudiante(nombre, carrera, lugar())  # Proporciona 'sede' aquí
           break

        elif opcion_clase == "2":
            nombre = input("Ingrese su nombre: ")
            departamento = input("Ingrese su departamento: ")
            usuario = Docente(nombre, departamento)
            break
        elif opcion_clase == "3":
            nombre = input("Ingrese su nombre: ")
            usuario = Administrativo(nombre)
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    return usuario

def lugar():
    print("Seleccione su sede:")
    print("1. Calle 40 Sabio Caldas")
    print("2. Aduanilla de Paiba")
    print("3. Tecnológica")

    while True:
        opcion = input("Ingrese el número de la sede (1/2/3): ")

        if opcion == "1":
            sede = "Calle 40 Sabio Caldas"
            break
        elif opcion == "2":
            sede = "Aduanilla de Paiba"
            break
        elif opcion == "3":
            sede = "Tecnológica"
            break
        else:
            print("Opción no válida. Por favor, seleccione una sede válida.")

    return sede

