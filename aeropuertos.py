from rutas import rutas

"""Importamos a la clase aereopuertos las rutas para que las podamos asociar, se define la clase constructora
con sus respectivos variables, y se define una lista vacia de rutas donde se almacenaran las rutas asociadas.

Se crea Nuevamente su parte de string para que cuando la llamemos pueda decirnos en forma de string lo que contiene
un aereopuerto.

Y por ultimo el metodo agregar rutas creara un objeto de una ruta para almacenarlo en la lista de rutas que se creo anteriormente
entonces se guardara siempre la ruta para el aereopuerto especifico que estemos trabajando"""

class Aeropuerto:
    def __init__(self, nombre, ubicacion, codigo):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.codigo = codigo
        self.rutas = []

    def __str__(self):
        return f"Aeropuerto: {self.nombre}, Ubicación: {self.ubicacion}, Código: {self.codigo}"
    
    def agregar_ruta(self, aeropuerto_destino, distancia, tiempo_vuelo):
        ruta = rutas(distancia, tiempo_vuelo)
        self.rutas.append((aeropuerto_destino, ruta))

