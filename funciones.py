import tkinter
from tkinter.simpledialog import askfloat, askstring
from aeropuertos import Aeropuerto

"""Aclarar primero que funcionesTkinter es exactamente el mismo a funciones, simplemente
que se intentaron lograr cosas aqui no tuvieron exito"""

"""Definimos una lista vacia para almacenar los aereopuertos, recordemos que las rutas ya se almacenan en la clase
aereopuertos"""

aereopuertos = []

"""la primera funcion nos permite crear los aereopuertos, pedimos los tres datos que tienen los aereopuertos
por defecto y creamos una varible que creara el objeto aereopuerto que lo guardara despues en nuestra lista"""


def crearAereopuertosTkinter():
    print()
    while True:
        ventana = tkinter.Toplevel()
        ventana.attributes('-topmost', True)  # Mantén la ventana al frente
        ventana.withdraw()

        nombre = askstring("Crear Aeropuerto", "Nombre del aeropuerto (o 'salir' para terminar): ")
        
        if nombre is None:
            ventana.destroy()
            break

        if nombre.lower() == 'salir':
            ventana.destroy()
            break

        ubicacion = askstring("Crear Aeropuerto", "Ubicación del aeropuerto:")
        codigo = askstring("Crear Aeropuerto", "Código del aeropuerto:")

        aeropuerto = Aeropuerto(nombre, ubicacion, codigo)
        aereopuertos.append(aeropuerto) 

        tkinter.messagebox.showinfo("Aeropuerto Creado", "Aeropuerto creado con éxito.")
        print("Aeropuerto registrado correctamente.")
        print()

        ventana.destroy()

      
"""Esta es la segunda funcion que es la creacion de rutas, primero explicamos que si no hay dos aereopuertos
creados no se puede crear la ruta entre ellos, y si no hay ninguno avisar al usuario para que cree los aereopuertos.

si se cumple la condicion de que hay dos aereopuertos pasaremos a pedir los datos de la ruta que es el tiempo y la
distancia.

despues creamos dos variables que seran los dos nombres de los aereopuertos que queremos relacionar, si los dos mencionados
existen en la lista estos se aplicaran a dos nuevas variables que seran aereopuerto origen y destino.

finalmente si el origen y el destino existe usamos el agregar ruta de la clase aereopuertos para almacenar la ruta a los
aereopuertos especificados y ya quedaria la ruta entre ellos dos."""      
                
def crearRutasTkinter():
    ventana = tkinter.Tk()
    ventana.withdraw()  # Ocultar la ventana principal, ya que solo necesitamos el cuadro de diálogo

    if len(aereopuertos) == 0:
        tkinter.messagebox.showinfo("Sin aeropuertos", "No tienes aeropuertos creados todavía.")
        print("No tienes aeropuertos creados todavía")
        print()
    elif len(aereopuertos) < 2:
        tkinter.messagebox.showinfo("Sin aeropuertos", "No podemos realizar una ruta porque no hay otro aeropuerto para relacionarlo.")
        print("No podemos realizar una ruta porque no hay otro aeropuerto para relacionarlo")
        print()
    else:
        tkinter.messagebox.showinfo("Crear Ruta", "Creemos la ruta entre esos aeropuertos")
        print("Creemos la ruta entre esos aeropuertos\n")

        distancia = askfloat("Crear Ruta", "Distancia de la ruta en Km:")
        tiempo_vuelo = askfloat("Crear Ruta", "Tiempo de vuelo de la ruta en Horas:")

        nombre_origen = askstring("Crear Ruta", "Nombre del aeropuerto de origen:")
        nombre_destino = askstring("Crear Ruta", "Nombre del aeropuerto de destino:")

        aeropuerto_origen = None
        aeropuerto_destino = None

        for aeropuerto in aereopuertos:
            if aeropuerto.nombre == nombre_origen:
                aeropuerto_origen = aeropuerto
            elif aeropuerto.nombre == nombre_destino:
                aeropuerto_destino = aeropuerto

        if aeropuerto_origen is not None and aeropuerto_destino is not None:
            aeropuerto_origen.agregar_ruta(aeropuerto_destino, distancia, tiempo_vuelo)
            aeropuerto_destino.agregar_ruta(aeropuerto_origen, distancia, tiempo_vuelo)
            tkinter.messagebox.showinfo("Ruta Creado", "Ruta creada exitosamente.")
            print("Ruta creada exitosamente.")
            print()
        else:
            print("No se encontraron los aeropuertos especificados.")
            print()

    ventana.destroy() 

"""En esta funcion pedimos los aereopuertos de origen y destino para averiguar si existen primero y despues
mirar si hay una ruta entre ellos, si la hay, la funcion pedira de nuevo la informacion de la ruta para hacer el cambio
de los valores para actualizarlos y nuevamente las agrega a la lista de las rutas de los aereopuertos"""            

def modificarRutasTkinter():
    ventana = tkinter.Tk()
    ventana.withdraw()  # Ocultar la ventana principal, ya que solo necesitamos el cuadro de diálogo

    print()
    nombre_origen = askstring("Modificar Ruta", "Nombre del aeropuerto de origen:")
    nombre_destino = askstring("Modificar Ruta", "Nombre del aeropuerto de destino:")

    aeropuerto_origen = None
    aeropuerto_destino = None

    for aeropuerto in aereopuertos:
        if aeropuerto.nombre == nombre_origen:
            aeropuerto_origen = aeropuerto
        elif aeropuerto.nombre == nombre_destino:
            aeropuerto_destino = aeropuerto

    if aeropuerto_origen is not None and aeropuerto_destino is not None:
        rutas_origen = aeropuerto_origen.rutas
        rutas_destino = aeropuerto_destino.rutas

        ruta_modificar_origen = None
        ruta_modificar_destino = None

        for destino, ruta in rutas_origen:
            if destino == aeropuerto_destino:
                ruta_modificar_origen = ruta
                break

        for destino, ruta in rutas_destino:
            if destino == aeropuerto_origen:
                ruta_modificar_destino = ruta
                break

        if ruta_modificar_origen is not None and ruta_modificar_destino is not None:
            print(f"Ruta encontrada: {ruta_modificar_origen}")
            distancia = askfloat("Modificar Ruta", "Nueva distancia de la ruta en Km:")
            tiempo_vuelo = askfloat("Modificar Ruta", "Nuevo tiempo de vuelo de la ruta en Horas:")

            ruta_modificar_origen.distancia = distancia
            ruta_modificar_origen.tiempo_vuelo = tiempo_vuelo

            ruta_modificar_destino.distancia = distancia
            ruta_modificar_destino.tiempo_vuelo = tiempo_vuelo

            print("Rutas modificadas exitosamente.")
        else:
            print("No se encontró la ruta especificada.")
            print()
    else:
        print("No se encontraron los aeropuertos especificados.")
        print()

    ventana.destroy()
"""Esta funcion mostrara los aereopuertos por medio de la lista usando el metodo __str__ creado anteriormente en la 
clase aereopuertos"""        
                
def mostrarAereopuertosTkinter():
    print()
    
    if not aereopuertos:
        tkinter.messagebox.showinfo("Sin aeropuertos", "No hay aeropuertos creados aún.")
        print("No hay aeropuertos creados aún.")
    else:
        for aereopuerto in aereopuertos:
            print(aereopuerto)
            print()

"""esta funcion mostrara las rutas existentes, se hace desde un bucle for por el hecho de que se muestren todas las rutas
en el aereopuerto que se encuentre, es decir por cada aereopuerto se mostraran todas las rutas existentes"""

def mostrarRutasTkinter():
    print()

    if not aereopuertos:
        tkinter.messagebox.showinfo("Sin rutas", "No hay aeropuertos creados aún.")
        print("No hay aeropuertos creados aún.")
    else:
        for aeropuerto in aereopuertos:
            print()
            print(f"Rutas desde el aeropuerto {aeropuerto.nombre}:")
            print()  
            for destino, ruta in aeropuerto.rutas:
                print(f"Destino: {destino.nombre}, Ruta: {ruta}")
            print()       

def buscarRutaPorTiempoTkinter():
    ventana = tkinter.Toplevel()
    ventana.withdraw()

    nombre_origen = askstring("Input", "Nombre del aeropuerto de origen:")
    nombre_destino = askstring("Input", "Nombre del aeropuerto de destino:")

    ventana.destroy()

    resultado = buscarRutaPorTiempo(nombre_origen, nombre_destino)
    return resultado

def buscarRutaPorTiempo(nombre_origen, nombre_destino):
    print()

    aeropuerto_origen = None
    aeropuerto_destino = None

    for aeropuerto in aereopuertos:
        if aeropuerto.nombre == nombre_origen:
            aeropuerto_origen = aeropuerto
        elif aeropuerto.nombre == nombre_destino:
            aeropuerto_destino = aeropuerto

    if aeropuerto_origen is None or aeropuerto_destino is None:
        tkinter.messagebox.showinfo("Error", "No se encontraron los aeropuertos especificados.")
        return

    distancias = {}
    antecesores = {}

    for aeropuerto in aereopuertos:
        distancias[aeropuerto] = float('inf')
        antecesores[aeropuerto] = None

    distancias[aeropuerto_origen] = 0

    aeropuertos_restantes = set(aereopuertos)

    while aeropuertos_restantes:
        aeropuerto_actual = min(aeropuertos_restantes, key=lambda aeropuerto: distancias[aeropuerto])

        if aeropuerto_actual == aeropuerto_destino:
            break

        aeropuertos_restantes.remove(aeropuerto_actual)

        for destino, ruta in aeropuerto_actual.rutas:
            distancia_actual = distancias[aeropuerto_actual]
            distancia_viaje = ruta.tiempo_vuelo

            if distancia_actual + distancia_viaje < distancias[destino]:
                distancias[destino] = distancia_actual + distancia_viaje
                antecesores[destino] = aeropuerto_actual

    ruta_mas_ligera = []
    aeropuerto_actual = aeropuerto_destino

    while aeropuerto_actual != aeropuerto_origen:
        ruta_mas_ligera.append(aeropuerto_actual)
        aeropuerto_actual = antecesores[aeropuerto_actual]

    ruta_mas_ligera.append(aeropuerto_origen)
    ruta_mas_ligera.reverse()

    resultado = f"\nRuta más ligera por tiempo de vuelo desde {nombre_origen} hasta {nombre_destino}:\n"
    for aeropuerto in ruta_mas_ligera:
        resultado += f"{aeropuerto.nombre}\n"

    return resultado
      
"""es exactamente lo mismo con la diferencia que en distancia_viaje = a ruta.distancia y no ruta.tiempo_vuelo"""

def buscarRutaPorDistanciaTkinter():
    ventana = tkinter.Toplevel()
    ventana.withdraw()

    nombre_origen = askstring("Input", "Nombre del aeropuerto de origen:")
    nombre_destino = askstring("Input", "Nombre del aeropuerto de destino:")

    ventana.destroy()

    resultado = buscarRutaPorDistancia(nombre_origen, nombre_destino)
    return resultado

def buscarRutaPorDistancia(nombre_origen, nombre_destino):
    print()
    aeropuerto_origen = None
    aeropuerto_destino = None

    for aeropuerto in aereopuertos:
        if aeropuerto.nombre == nombre_origen:
            aeropuerto_origen = aeropuerto
        elif aeropuerto.nombre == nombre_destino:
            aeropuerto_destino = aeropuerto

    if aeropuerto_origen is None or aeropuerto_destino is None:
        tkinter.messagebox.showinfo("Error", "No se encontraron los aeropuertos especificados.")
        return

    distancias = {} 
    antecesores = {}

    for aeropuerto in aereopuertos:
        distancias[aeropuerto] = float('inf') 
        antecesores[aeropuerto] = None

    distancias[aeropuerto_origen] = 0 

    aeropuertos_restantes = set(aereopuertos)  

    while aeropuertos_restantes:
        aeropuerto_actual = min(aeropuertos_restantes, key=lambda aeropuerto: distancias[aeropuerto])

        if aeropuerto_actual == aeropuerto_destino:
            break  

        aeropuertos_restantes.remove(aeropuerto_actual)

        for destino, ruta in aeropuerto_actual.rutas:
            distancia_actual = distancias[aeropuerto_actual]
            distancia_viaje = ruta.distancia

            if distancia_actual + distancia_viaje < distancias[destino]:
                distancias[destino] = distancia_actual + distancia_viaje
                antecesores[destino] = aeropuerto_actual

    ruta_mas_ligera = []
    aeropuerto_actual = aeropuerto_destino

    while aeropuerto_actual != aeropuerto_origen:
        ruta_mas_ligera.append(aeropuerto_actual)
        aeropuerto_actual = antecesores[aeropuerto_actual]

    ruta_mas_ligera.append(aeropuerto_origen)
    ruta_mas_ligera.reverse()

    resultado = f"\nRuta más ligera por distancia desde {nombre_origen} hasta {nombre_destino}:\n"
    for aeropuerto in ruta_mas_ligera:
        resultado += f"{aeropuerto.nombre}\n"

    return resultado
