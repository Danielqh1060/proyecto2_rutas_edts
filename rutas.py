"""Esta es la primera clase que se crea para realizar el proyecto,
se crea la clase rutas que almacenara la variable distancia y la variable tiempo de vuelo,
se crea otra clase la cual nos dara en forma de string el texto cuando se llama a la clase,
es decir cuando se llama a la ruta por el print, imprimira lo que retorna la clase __str__."""

class rutas:
    def __init__(self, distancia, tiempo_vuelo):
        self.distancia = distancia
        self.tiempo_vuelo = tiempo_vuelo

    def __str__(self):
        return f"Distancia (Km): {self.distancia}, Tiempo de vuelo (Horas): {self.tiempo_vuelo}"