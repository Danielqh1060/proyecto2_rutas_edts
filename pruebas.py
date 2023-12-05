import funciones

"""Se creo un espacio para poder probar las munciones mediante un menu, para poder ejecutar las funciones de la aplicacion
por medio de la consola, antes de hacerlo por medio de la interfaz grafica"""

"""Lo que sucede es que cuando usuario coloca uno de los numeros de las opciones ejecutara la funcion creada para el proyecto
de las rutas del aereopuerto, de forma infinita con posibilidad de hacerlo las veces que vea necesario"""

while True:
    print("----- Menú de opciones -----")
    print("1. Crear aeropuerto")
    print("2. Crear ruta")
    print("3. Modificar ruta")
    print("4. Mostrar aereopuertos")
    print("5. Mostrar rutas")
    print("6. Buscar mejor ruta por tiempo")
    print("7. Buscar mejor ruta por distancia")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        funciones.crearAereopuertos()

    elif opcion == "2":
        funciones.crearRutas()  

    elif opcion == "3":
        funciones.modificarRutas()

    elif opcion == "4":
        funciones.mostrarAereopuertos()

    elif opcion == "5":
        funciones.mostrarRutas()

    elif opcion == "6":
        funciones.buscarRutaPorTiempo()

    elif opcion == "7":
        funciones.buscarRutaPorDistancia(input("Nombre del aeropuerto de origen: "), input("Nombre del aeropuerto de destino: "))      

    elif opcion == "8":
        break

    else:
        print("Opcion invalida, intente con las opciones disponibles")
        print()

print()
print("Gracias por usar el programa")           


