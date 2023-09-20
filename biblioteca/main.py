from libro import Libro
from biblioteca import Biblioteca
from persona import Estudiante, Docente, Administrativo
from Login import*

def main():
    # Crear bibliotecas y personas
    biblioteca1 = Biblioteca("Sede A")
    biblioteca2 = Biblioteca("Sede B")
    usuario = iniciar_sesion()
    # Cargar lista de libros desde un archivo de texto
    biblioteca1.cargar_libros_desde_archivo("libros.txt")
    while True:
        print("\nMenú:")
        print("1. Pedir prestado un libro")
        print("2. Devolver un libro")
        print("3. Mostrar libros disponibles")
        print("4. Mostrar libros prestados")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo_libro = input("Ingrese el título del libro que desea pedir prestado: ")
            libro_buscado = biblioteca1.buscar_libro(titulo_libro)

            if libro_buscado:
                if libro_buscado.prestar():
                    print(f"{libro_buscado.titulo} ha sido prestado.")
                else:
                    print("El libro no está disponible en este momento.")
            else:
                print("El libro no se encuentra en la biblioteca.")
        
        elif opcion == "2":
            titulo_libro = input("Ingrese el título del libro que desea devolver: ")
            libro_devuelto = biblioteca1.buscar_libro(titulo_libro)

            if libro_devuelto:
                libro_devuelto.devolver()
                print(f"{libro_devuelto.titulo} ha sido devuelto.")
            else:
                print("El libro no se encuentra en la biblioteca.")
        
        elif opcion == "3":
            print("\nLibros Disponibles:")
            for libro in biblioteca1.libros_disponibles():
                print(f"- {libro.titulo} de {libro.autor}")
        
        elif opcion == "4":
            print("\nLibros Prestados:")
            for libro in biblioteca1.libros_prestados():
                print(f"- {libro.titulo} de {libro.autor}")
        
        elif opcion == "5":
            print("Gracias por usar el sistema de biblioteca.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()