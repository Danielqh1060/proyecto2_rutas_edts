from tkinter import *
from funciones import *
from PIL import Image, ImageTk

class InterfazApp:
    def __init__(self, root):
        root.geometry("900x480")
        root.title("Proyecto Rutas de Aeropuertos")
        root.resizable(0, 0)

        self.imagen_tk = self.cargar_imagen()
        if self.imagen_tk:
            print("Imagen cargada correctamente")
            self.label_imagen = Label(root, image=self.imagen_tk)
            self.label_imagen.pack()

        self.texto = Text(root)
        self.texto.place(x=175, y=60)

        boton1 = Button(root, text="Crear Aeropuertos", command=self.crear_aereopuertos)
        boton1.place(x=5, y=120)

        boton2 = Button(root, text="Crear Rutas", command=self.crear_rutas)
        boton2.place(x=5, y=200)

        boton3 = Button(root, text="Modificar Rutas", command=self.modificar_rutas)
        boton3.place(x=5, y=280)

        boton4 = Button(root, text="Mostrar Aeropuertos", command=self.mostrar_aereopuertos)
        boton4.place(x=150, y=5)

        boton5 = Button(root, text="Mostrar Rutas", command=self.mostrar_rutas)
        boton5.place(x=300, y=5)

        boton6 = Button(root, text="Buscar ruta mas corta por tiempo", command=self.buscar_ruta_por_tiempo)
        boton6.place(x=480, y=5)

        boton7 = Button(root, text="Buscar ruta mas corta por distancia", command=self.buscar_ruta_por_distancia)
        boton7.place(x=680, y=5)

        boton8 = Button(root, text="Salir", command=root.destroy)
        boton8.place(x=850, y=440)


    def cargar_imagen(self):
        try:
            imagen = Image.open("avion.jpg")
            imagen_tk = ImageTk.PhotoImage(imagen)
            return imagen_tk
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            return None

    def crear_aereopuertos(self):
        crearAereopuertosTkinter()

    def crear_rutas(self):
        crearRutasTkinter()

    def modificar_rutas(self):
        modificarRutasTkinter()

    def mostrar_aereopuertos(self):
        mostrarAereopuertosTkinter()
        self.actualizar_texto_aeropuerto()

    def mostrar_rutas(self):
        mostrarRutasTkinter()
        self.actualizar_texto_rutas()

    def buscar_ruta_por_tiempo(self):
        self.actualizar_texto_tiempo()

    def buscar_ruta_por_distancia(self):
        self.actualizar_texto_distancia()


    def actualizar_texto_aeropuerto(self):
        # Verifica si hay aeropuertos creados
        if not aereopuertos:
            return "No hay aeropuertos creados aún."

        # Formatea la información de los aeropuertos
        texto = "Aeropuertos creados:\n"
        for aeropuerto in aereopuertos:
            texto += f"Nombre: {aeropuerto.nombre}, Ubicación: {aeropuerto.ubicacion}, Código: {aeropuerto.codigo}\n"

        self.texto.delete(1.0, END)
        self.texto.insert(END, texto)

    def actualizar_texto_rutas(self):
        # Verifica si hay aeropuertos creados
        if not aereopuertos:
            texto = "No hay aeropuertos creados aún."
        else:
            # Formatea la información de las rutas de los aeropuertos
            texto = "Rutas de los aeropuertos:\n"
            for aeropuerto in aereopuertos:
                if aeropuerto.rutas:
                    texto += f"\nAeropuerto {aeropuerto.nombre}:\n"
                    for destino, ruta in aeropuerto.rutas:
                        texto += f"  Destino: {destino.nombre}, Distancia: {ruta.distancia} Km, Tiempo de vuelo: {ruta.tiempo_vuelo} horas\n"

        self.texto.delete(1.0, END)
        self.texto.insert(END, texto)

    def actualizar_texto_tiempo(self):
        resultado = buscarRutaPorTiempoTkinter()    
        self.texto.delete(1.0, "end")
        self.texto.insert("end", resultado)

    def actualizar_texto_distancia(self):
        resultado = buscarRutaPorDistanciaTkinter()
        self.texto.delete(1.0, "end")
        self.texto.insert("end", resultado)


root = Tk()
app = InterfazApp(root)
root.mainloop()