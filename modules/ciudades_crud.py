def CRUD(datos):
    # Modulo de ciudades C.R.U.D
    datos = dict(datos) 
    while True:
        choice = -1
        try:

            print("Modulo de ciudades")
            print("Los cambios solo se guardan cuando termine el programa.")
            print("Ingresa la opcion: ")
            print("(1) Agregar Ciudad.")
            print("(2) Editar Ciudad.")
            print("(3) Buscar ciudad.")
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
        elif choice == 0:
            print("Terminando proceso")
            break
    return datos