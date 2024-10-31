def Filtrar(datos):
    # Modulo de filtrar ciudades
    datos = dict(datos) 
    while True:
        choice = -1

        try:
            print()
            print("***********************************************")
            print("Modulo de filtrar ciudades")
            print("1) Buscar por nombre.")
            print("2) Buscar por país.")
            print("3) Buscar por código postal.")
            print("4) Filtrar por poblacion.")
            print("0) Terminar.")
            choice = int(input("Ingresa la opcion: "))
        except Exception as e:
            print("Ese valor no es valido")
            print(e)

        if choice == 1:
            Filtrar_Nombre(datos)
        elif choice == 2:
            Filtrar_Pais(datos)
        elif choice == 3:
            Filtrar_Codigo_Postal(datos)
        elif choice == 4:
            Filtrar_Poblacion(datos)
        elif choice == 0:
            print("Terminando proceso")
            break
    return

# Filtrar Por Nombre
def Filtrar_Nombre(datos):
    datos = dict(datos)

    Nombre = ""
    print()
    print("***********************************************")
    Nombre = str(input("Ingresa el nombre de la ciudad: "))

    for i in datos["pais"]:
        for j in datos["pais"][i]:
            for k in datos["pais"][i][j]:
                if k["ciudad"].lower() == Nombre.lower():
                    print()
                    print("***********************************************")
                    print("Ciudad:",k["ciudad"])
                    print("Poblacion:",k["poblacion"])
                    print("Codigo Postal:",k["codigo postal"])

# Filtrar Por Pais
def Filtrar_Pais(datos):
    datos = dict(datos)
    while True:
        opc = -1
        print()
        print("************************************************")
        print("¿En cual de los siguientes paises quieres filtrar la ciudad?")
        print("1). Colombia")
        print("2). Argentina")
        print("0). Salir")
        
        try:
            opc= int(input("Ingresa una opcion: "))
        except Exception as e:
            print("Ese valor no es valido")
            print(e)

        if opc == 1:
            Filtrar_Pais_Colombia(datos)
        elif opc == 2:
            Filtrar_Pais_Argentina(datos)
        elif opc == 0:
            print("Saliste de filtrar por país")
            print("************************************")
            return datos

# Filtrar Por Pais Colombia
def Filtrar_Pais_Colombia(datos):
    datos = dict(datos)
    for i in datos["pais"]["colombia"]:
        for j in datos["pais"]["colombia"][i]:
            print()
            print("***********************************************")
            print("Ciudad:",j["ciudad"])
            print("Poblacion:",j["poblacion"])
            print("Codigo Postal:",j["codigo postal"])

# Filtrar Por Pais Argentina
def Filtrar_Pais_Argentina(datos):
    datos = dict(datos)
    for i in datos["pais"]["argentina"]:
        for j in datos["pais"]["argentina"][i]:
            print()
            print("***********************************************")
            print("Ciudad:",j["ciudad"])
            print("Poblacion:",j["poblacion"])
            print("Codigo Postal:",j["codigo postal"])

# Filtrar Por Codigo Postal
def Filtrar_Codigo_Postal(datos):
    datos = dict(datos)

    while True:
        Codigo = -1
        try:
            print()
            print("***********************************************")
            Codigo = int(input("Ingresa el codigo postal de la ciudad: "))
            break
        except Exception as e:
            print("Ese valor no es valido")
            print(e)

    for i in datos["pais"]:
        for j in datos["pais"][i]:
            for k in datos["pais"][i][j]:
                if k["codigo postal"] == Codigo:
                    print()
                    print("***********************************************")
                    print("Ciudad:",k["ciudad"])
                    print("Poblacion:",k["poblacion"])
                    print("Codigo Postal:",k["codigo postal"])

# Filtrar Por Poblacion
def Filtrar_Poblacion(datos):
    # Modulo de filtrar ciudades
    datos = dict(datos)


    while True:
        choice = -1
        numero = -1
        try:
            print()
            print("***********************************************")
            print("Modulo de filtrar ciudades")
            print("Los cambios solo se guardan cuando termine el programa.")
            print("1) Buscar por menor poblacion.")
            print("2) Buscar por mayor poblacion.")
            print("0) Terminar.")
            choice = int(input("Ingresa la opcion: "))
            numero = int(input("Ingresa el numero de la poblacion: "))
            break
        except Exception as e:
            print("Ese valor no es valido")
            print(e)

    if choice == 1:
        Filtrar_Menor_Poblacion(datos,numero)
    elif choice == 2:
        Filtrar_Mayor_Poblacion(datos,numero)
    elif choice == 0:
        print("Saliste de filtrar por poblacion")
        print("************************************")
        return

# Filtrar Por Poblacion Menor Que 
def Filtrar_Menor_Poblacion(datos, numero):
    datos = dict(datos)
    for i in datos["pais"]:
        for j in datos["pais"][i]:
            for k in datos["pais"][i][j]:
                if k["poblacion"] <= numero:
                    print()
                    print("***********************************************")
                    print("Ciudad:",k["ciudad"])
                    print("Poblacion:",k["poblacion"])
                    print("Codigo Postal:",k["codigo postal"])

# Filtrar Por Poblacion Mayor Que 
def Filtrar_Mayor_Poblacion(datos, numero):
    datos = dict(datos)
    for i in datos["pais"]:
        for j in datos["pais"][i]:
            for k in datos["pais"][i][j]:
                if k["poblacion"] >= numero:
                    print()
                    print("***********************************************")
                    print("Ciudad:",k["ciudad"])
                    print("Poblacion:",k["poblacion"])
                    print("Codigo Postal:",k["codigo postal"])