from modules.datos_json import *

# importe de los datos
try:
    Ciudades = cargar_datos_json("./Ciudades.json")
except Exception as e:
        print("hubo un error en la importacion de los datos")
        print(e)

# menu de seleccion
while True:
    choice = -1
    try:

        # opciones
        choice = 0
        print("Menu general")
        print("ingresa la opcion: ")
        print("(1) Modulo Ciudades CRUD.")
        print("(2) Modulo Filtrar Ciudades.")
        print("(0) Terminar.")
    
    except Exception as e:
        print("ese valor no es valido")
        print(e)

    if choice == 1:
        None
    elif choice == 2:
        None
    elif choice == 0:
        print("Terminando proceso")
        break

    # guardado de los datos
    guardar_datos_json(Ciudades,"JSON/usuarios.json")