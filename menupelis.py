import os
from pelicula import Pelicula

class CatalogoPeliculas:
    def __init__(self, nombre, ruta_archivo="catalogo_peliculas.txt"):
        self.nombre = nombre
        self.ruta_archivo = ruta_archivo
        self.inicializar_catalogo()

    def inicializar_catalogo(self):
        if not os.path.exists(self.ruta_archivo):
            peliculas_iniciales = [
                Pelicula("El secreto de sus ojos", 2009, "Suspenso", 129),
                Pelicula("Relatos salvajes", 2014, "Drama", 122),
                Pelicula("Nueve reinas", 2000, "Crimen", 114),
                Pelicula("El hijo de la novia", 2001, "Comedia dramática", 123),
                Pelicula("Cuentos de la selva", 2010, "Infantil", 86),
                Pelicula("La historia oficial", 1985, "Drama histórico", 112),
                Pelicula("Crónica de una fuga", 2006, "Drama", 100),
                Pelicula("La odisea de los giles", 2019, "Comedia dramática", 116),
                Pelicula("El clan", 2015, "Crimen", 110),
                Pelicula("Pizza, birra, faso", 1998, "Drama", 92)
            ]
            for peli in peliculas_iniciales:
                self.agregar_pelicula(peli, mostrar_mensaje=False)

    def agregar_pelicula(self, pelicula, mostrar_mensaje=True):
        with open(self.ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{pelicula.get_nombre()} - {pelicula.get_anio()} - {pelicula.get_genero()} - {pelicula.get_duracion()} min\n")
        if mostrar_mensaje:
            print(f" Película '{pelicula}' agregada correctamente.\n")

    def listar_peliculas(self):
        if os.path.exists(self.ruta_archivo):
            print("🎬 Películas en el catálogo:")
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    print("- " + linea.strip())
            print()
        else:
            print(" No hay un catálogo creado todavía.\n")

    def buscar_pelicula(self, nombre_busqueda):
        if os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    if nombre_busqueda.lower() in linea.lower():
                        print(f" Película encontrada: {linea.strip()}\n")
                        return True
        print(" Película no encontrada.")
        return False

    def eliminar_catalogo(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print(" Catálogo eliminado correctamente.\n")
        else:
            print(" El catálogo no existe.\n")

def menu():
    catalogo = CatalogoPeliculas("Catálogo de Películas Argentinas")

    while True:
        print("---- Menú del Catálogo de Películas ----")
        print("1. Agregar película")
        print("2. Listar películas")
        print("3. Buscar película por nombre")
        print("4. Eliminar catálogo")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la película: ").strip()
            anio = input("Ingrese el año de la película: ").strip()
            genero = input("Ingrese el género de la película: ").strip()
            duracion = input("Ingrese la duración en minutos: ").strip()

            if not nombre or not anio.isdigit() or not duracion.isdigit() or not genero:
                print(" Datos inválidos. Intente de nuevo.\n")
                continue

            pelicula = Pelicula(nombre, int(anio), genero, int(duracion))
            catalogo.agregar_pelicula(pelicula)

        elif opcion == "2":
            catalogo.listar_peliculas()

        elif opcion == "3":
            nombre_buscar = input(" Ingrese el nombre de la película a buscar: ").strip()
            encontrada = catalogo.buscar_pelicula(nombre_buscar)
            if not encontrada:
                agregar = input("¿Desea agregarla al catálogo? (s/n): ").lower()
                if agregar == "s":
                    anio = input("Ingrese el año de la película: ").strip()
                    genero = input("Ingrese el género de la película: ").strip()
                    duracion = input("Ingrese la duración en minutos: ").strip()

                    if anio.isdigit() and duracion.isdigit():
                        nueva_peli = Pelicula(nombre_buscar, int(anio), genero, int(duracion))
                        catalogo.agregar_pelicula(nueva_peli)
                    else:
                        print(" Datos inválidos. No se agregó la película.\n")

        elif opcion == "4":
            confirmacion = input("¿Está seguro que desea eliminar el catálogo? (s/n): ")
            if confirmacion.lower() == "s":
                catalogo.eliminar_catalogo()

        elif opcion == "5":
            print(" Gracias por usar el catálogo de películas.")
            break

        else:
            print(" Opción no válida. Intente nuevamente.\n")

if __name__ == "__main__":
    menu()