def Filtrar(datos):
    # Modulo de filtrar ciudades
    datos = dict(datos) 
    while True:
        choice = -1
        try:

            print()
            print("Modulo de filtrar ciudades")
            print("Los cambios solo se guardan cuando termine el programa.")
            print("(1) Buscar por nombre.")
            print("(2) Buscar por país.")
            print("(3) Buscar por código postal.")
            print("(4) Filtrar por poblacion.")
            print("(0) Terminar.")
            choice = int(input("Ingresa la opcion: "))
        
        except Exception as e:
            print("Ese valor no es valido")
            print(e)

        if choice == 1:
            None
        elif choice == 2:
            None
        elif choice == 3:
            None
        elif choice == 4:
            Filtrar_poblacion(datos)
        elif choice == 0:
            print("Terminando proceso")
            break
    return

def Filtrar_poblacion(datos):
    # Modulo de filtrar ciudades
    datos = dict(datos)

    numero = int(input("Ingresa el numero de la poblacion: "))

    while True:
        choice = -1
        try:

            print()
            print("Modulo de filtrar ciudades")
            print("Los cambios solo se guardan cuando termine el programa.")
            print("(1) Buscar por menor poblacion.")
            print("(2) Buscar por mayor poblacion.")
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
    return