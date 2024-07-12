from modules.datos_json import *

# Importacion del dato
try:
    Ciudades = cargar_datos_json("./Ciudades.json")
except Exception as e:
        print("Hubo un error en la Importacion del dato")
        print(e)

# Menu de seleccion
while True:
    choice = -1
    try:

        # opciones
        print("Menu general")
        print("Ingresa la opcion: ")
        print("(1) Modulo Ciudades CRUD.")
        print("(2) Modulo Filtrar Ciudades.")
        print("(0) Terminar.")
        choice = int(input("Ingresa la opcion: "))

    except Exception as e:
        print("Ese valor no es valido")
        print(e)

    if choice == 1:
        None
    elif choice == 2:
        None
    elif choice == 0:
        print("Terminando proceso")
        break

    # guardado de los datos
    guardar_datos_json(Ciudades,"./Ciudades.json")