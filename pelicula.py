class Pelicula:
    def __init__(self, nombre, anio, genero, duracion):
        self.__nombre = nombre
        self.__anio = anio
        self.__genero = genero
        self.__duracion = duracion  # en minutos

    def get_nombre(self):
        return self.__nombre

    def get_anio(self):
        return self.__anio

    def get_genero(self):
        return self.__genero

    def get_duracion(self):
        return self.__duracion

    def __str__(self):
        return f"{self.__nombre} ({self.__anio}) - {self.__genero} - {self.__duracion} min"