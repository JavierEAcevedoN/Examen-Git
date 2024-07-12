from modules.datos_json import *
from modules.ciudades_crud import CRUD
from modules.filtrar_ciudades import Filtrar

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

        # Opciones
        print()
        print("***********************************************")
        print("Menu general")
        print("(1) Modulo Ciudades CRUD.")
        print("(2) Modulo Filtrar Ciudades.")
        print("(0) Terminar.")
        choice = int(input("Ingresa la opcion: "))

    except Exception as e:
        print("Ese valor no es valido")
        print(e)

    if choice == 1:
        Ciudades = CRUD(Ciudades)
    elif choice == 2:
        Filtrar(Ciudades)
    elif choice == 0:
        print("Terminando proceso")
        break

    # Guardado del dato
    guardar_datos_json(Ciudades,"./Ciudades.json")