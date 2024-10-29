def CRUD(datos):
    # Modulo de ciudades C.R.U.D
    datos = dict(datos) 
    while True:
        choice = -1
        try:

            print()
            print("***********************************************")
            print("Modulo de ciudades")
            print("Los cambios solo se guardan cuando termine el programa.")
            print("(1) Agregar Ciudad.")
            print("(2) Editar Ciudad. (no funciona)")
            print("(0) Terminar.")
            choice = int(input("Ingresa la opcion: "))
        
        except Exception as e:
            print("Ese valor no es valido")
            print(e)

        if choice == 1:
            datos = Agregar_ciudades(datos)
        elif choice == 2:
            None
        elif choice == 0:
            print("Terminando proceso")
            break
    return datos

def Agregar_ciudades(datos):
    datos = dict(datos)
    while True:
        opc = -1
        print()
        print("************************************************")
        print("¿En cual de los siguientes paises quieres agregar la ciudad?")
        print("1). Colombia")
        print("2). Argentina")
        print("0). Salir")
        
        try:
            opc= int(input("Ingresa una opcion: "))
        except Exception as e:
            print("Ese valor no es valido")
            print(e)

        if opc == 1:
            datos = Colombia(datos)
        elif opc == 2:
            datos = Argentina(datos)
        elif opc == 0:
            print("Saliste del apartado de agregar")
            print("************************************")
            return datos

# Colombia
def Colombia(datos):
    datos = dict(datos)
    while True:
        opc = -1
        print()
        print("************************************************")
        print("Elegiste Colombia")
        print("¿De que departamento de colombia agregaras la ciudad?")
        print("1). Cundinamarca")
        print("2). Santander")
        print("3). Quindio")
        print("0). Salir")

        try:    
            opc=int(input("Ingresa una opcion: "))
        except Exception as e:
            print("Ese valor no es valido")
            print(e)
            
        if opc == 1:
            datos = Colombia_Cundinamarca(datos)
        elif opc == 2:  
            datos = Colombia_Santander(datos)
        elif opc == 3:
            datos = Colombia_Quindio(datos)
        elif opc== 0:
            print("Salio")
            return datos

# Colombia Cundinamarca
def Colombia_Cundinamarca(datos):
    datos = dict(datos)
    while True:
        print()
        print("***********************************************")

        try:
            cundinamarca = {}
            cundinamarca["ciudad"]=str(input("Ingresa la nueva ciudad dentro del departamento: "))
            cundinamarca["poblacion"]=str(input("Ingresa la poblacion de la ciudad: "))
            cundinamarca["codigo postal"]=int(input("Ingresa el codigo postal: "))
            datos["pais"]["colombia"]["cundidamarca"].append(cundinamarca)
            break
        except Exception as e:
            print("Ese valor no es valido")
            print(e)
        
    print("Ciudad creada con exito :3")
    return datos

# Colombia Santander
def Colombia_Santander(datos):
    datos = dict(datos)
    while True:
        print()
        print("***********************************************")

        try:
            santander = {}
            santander["ciudad"]=str(input("Ingresa la nueva ciudad dentro del departamento: "))
            santander["poblacion"]=str(input("Ingresa la poblacion de la ciudad: ")) 
            santander["codigo postal"]=int(input("Ingresa el codigo postal: "))
            datos["pais"]["colombia"]["santander"].append(santander)
            break
        except Exception as e:
            print("Ese valor no es valido")
            print(e)
        
    print("Ciudad creada con exito :3")
    return datos

# Colombia Quindio
def Colombia_Quindio(datos):
    datos = dict(datos)
    while True:
        print()
        print("***********************************************")

        try:
            quindio = {}
            quindio["ciudad"]=str(input("Ingresa la nueva ciudad dentro del departamento: "))
            quindio["poblacion"]=str(input("Ingresa la poblacion de la ciudad: ")) 
            quindio["codigo postal"]=int(input("Ingresa el codigo postal: "))
            datos["pais"]["colombia"]["quindio"].append(quindio)
            break
        except Exception as e:
            print("Ese valor no es valido")
            print(e)
        
    print("Ciudad creada con exito :3")
    return datos 
            
# Argentina
def Argentina(datos):       
    datos = dict(datos)
    while True:
        opc = -1
        print()
        print("************************************************")
        print("Elegiste Argentina")
        print("¿De que estado de Argentina agregaras la ciudad?")
        print("1). Santiago del Estero")
        print("2). San Juan")
        print("3). Santa Fe")
        print("0). Salir")

        try:
            opc=int(input("Ingresa una opcion: "))
        except Exception as e:
                print("Ese valor no es valido")
                print(e)
                
        if opc == 1:
            datos = Argentina_SDE(datos)
        elif opc == 2:  
            datos = Argentina_SJ(datos)
        elif opc == 3:
            datos = Argentina_SF(datos)
        elif opc== 0:
            print("Salio")
            return datos
        
# Argentina Santiago del Estero
def Argentina_SDE(datos):
    datos = dict(datos)
    while True:
        print()
        print("***********************************************")
                
        try:
            santiago_del_estero = {}
            santiago_del_estero["ciudad"]=str(input("Ingresa la nueva ciudad dentro del departamento: "))
            santiago_del_estero["poblacion"]=str(input("Ingresa la poblacion de la ciudad: ")) 
            santiago_del_estero["codigo postal"]=int(input("Ingresa el codigo postal: "))  
            datos["pais"]["argentina"]["santiago del estero"].append(santiago_del_estero)
            break
        except Exception as e:
            print("Ese valor no es valido")
            print(e)
            
    print("Ciudad creada con exito :3")
    return datos

# Argentina San Juan
def Argentina_SJ(datos):
    datos = dict(datos)
    while True:
        print()
        print("***********************************************")
                
        try:
            san_juan = {}
            san_juan["ciudad"]=str(input("Ingresa la nueva ciudad dentro del departamento: "))
            san_juan["poblacion"]=str(input("Ingresa la poblacion de la ciudad: ")) 
            san_juan["codigo postal"]=int(input("Ingresa el codigo postal: "))
            datos["pais"]["argentina"]["san juan"].append(san_juan)
            break
        except Exception as e:
            print("Ese valor no es valido")
            print(e)
            
    print("Ciudad creada con exito :3")
    return datos

# Argentina Santa Fe
def Argentina_SF(datos):
    datos = dict(datos)
    while True:
        print()
        print("***********************************************")
                
        try:
            santa_fe={}
            santa_fe["ciudad"]=str(input("Ingresa la nueva ciudad dentro del departamento: "))
            santa_fe["poblacion"]=str(input("Ingresa la poblacion de la ciudad: ")) 
            santa_fe["codigo postal"]=int(input("Ingresa el codigo postal: "))
            datos["pais"]["argentina"]["santa fe"].append(santa_fe)
            break
        except Exception as e:
            print("Ese valor no es valido")
            print(e)
            
    print("Ciudad creada con exito :3")
    return datos