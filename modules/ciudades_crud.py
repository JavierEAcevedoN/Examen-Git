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
            print("(2) Editar Ciudad.")
            print("(0) Terminar.")
            choice = int(input("Ingresa la opcion: "))
        
        except Exception as e:
            print("Ese valor no es valido")
            print(e)

        if choice == 1:
            datos = Agregar_ciudades(datos)
        elif choice == 2:
            datos = Editar_ciudades(datos)
        elif choice == 0:
            print("Terminando proceso")
            break
    return datos

# Modulo de agregar ciudades
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
            datos = Add_Colombia(datos)
        elif opc == 2:
            datos = Add_Argentina(datos)
        elif opc == 0:
            print("Saliste del apartado de agregar")
            print("************************************")
            return datos

# Colombia
def Add_Colombia(datos):
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
            datos = Add_Colombia_Cundinamarca(datos)
        elif opc == 2:  
            datos = Add_Colombia_Santander(datos)
        elif opc == 3:
            datos = Add_Colombia_Quindio(datos)
        elif opc== 0:
            print("Salio")
            return datos

# Colombia Cundinamarca
def Add_Colombia_Cundinamarca(datos):
    datos = dict(datos)
    while True:
        print()
        print("***********************************************")

        try:
            cundinamarca = {}
            cundinamarca["ciudad"]=str(input("Ingresa la nueva ciudad dentro del departamento: "))
            cundinamarca["poblacion"]=int(input("Ingresa la poblacion de la ciudad: "))
            cundinamarca["codigo postal"]=int(input("Ingresa el codigo postal: "))
            datos["pais"]["colombia"]["cundidamarca"].append(cundinamarca)
            break
        except Exception as e:
            print("Ese valor no es valido")
            print(e)
        
    print("Ciudad creada con exito :3")
    return datos

# Colombia Santander
def Add_Colombia_Santander(datos):
    datos = dict(datos)
    while True:
        print()
        print("***********************************************")

        try:
            santander = {}
            santander["ciudad"]=str(input("Ingresa la nueva ciudad dentro del departamento: "))
            santander["poblacion"]=int(input("Ingresa la poblacion de la ciudad: ")) 
            santander["codigo postal"]=int(input("Ingresa el codigo postal: "))
            datos["pais"]["colombia"]["santander"].append(santander)
            break
        except Exception as e:
            print("Ese valor no es valido")
            print(e)
        
    print("Ciudad creada con exito :3")
    return datos

# Colombia Quindio
def Add_Colombia_Quindio(datos):
    datos = dict(datos)
    while True:
        print()
        print("***********************************************")

        try:
            quindio = {}
            quindio["ciudad"]=str(input("Ingresa la nueva ciudad dentro del departamento: "))
            quindio["poblacion"]=int(input("Ingresa la poblacion de la ciudad: ")) 
            quindio["codigo postal"]=int(input("Ingresa el codigo postal: "))
            datos["pais"]["colombia"]["quindio"].append(quindio)
            break
        except Exception as e:
            print("Ese valor no es valido")
            print(e)
        
    print("Ciudad creada con exito :3")
    return datos 
            
# Argentina
def Add_Argentina(datos):       
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
            datos = Add_Argentina_SDE(datos)
        elif opc == 2:  
            datos = Add_Argentina_SJ(datos)
        elif opc == 3:
            datos = Add_Argentina_SF(datos)
        elif opc== 0:
            print("Salio")
            return datos
        
# Argentina Santiago del Estero
def Add_Argentina_SDE(datos):
    datos = dict(datos)
    while True:
        print()
        print("***********************************************")
                
        try:
            santiago_del_estero = {}
            santiago_del_estero["ciudad"]=str(input("Ingresa la nueva ciudad dentro del departamento: "))
            santiago_del_estero["poblacion"]=int(input("Ingresa la poblacion de la ciudad: ")) 
            santiago_del_estero["codigo postal"]=int(input("Ingresa el codigo postal: "))  
            datos["pais"]["argentina"]["santiago del estero"].append(santiago_del_estero)
            break
        except Exception as e:
            print("Ese valor no es valido")
            print(e)
            
    print("Ciudad creada con exito :3")
    return datos

# Argentina San Juan
def Add_Argentina_SJ(datos):
    datos = dict(datos)
    while True:
        print()
        print("***********************************************")
                
        try:
            san_juan = {}
            san_juan["ciudad"]=str(input("Ingresa la nueva ciudad dentro del departamento: "))
            san_juan["poblacion"]=int(input("Ingresa la poblacion de la ciudad: ")) 
            san_juan["codigo postal"]=int(input("Ingresa el codigo postal: "))
            datos["pais"]["argentina"]["san juan"].append(san_juan)
            break
        except Exception as e:
            print("Ese valor no es valido")
            print(e)
            
    print("Ciudad creada con exito :3")
    return datos

# Argentina Santa Fe
def Add_Argentina_SF(datos):
    datos = dict(datos)
    while True:
        print()
        print("***********************************************")
                
        try:
            santa_fe={}
            santa_fe["ciudad"]=str(input("Ingresa la nueva ciudad dentro del departamento: "))
            santa_fe["poblacion"]=int(input("Ingresa la poblacion de la ciudad: ")) 
            santa_fe["codigo postal"]=int(input("Ingresa el codigo postal: "))
            datos["pais"]["argentina"]["santa fe"].append(santa_fe)
            break
        except Exception as e:
            print("Ese valor no es valido")
            print(e)
            
    print("Ciudad creada con exito :3")
    return datos

# Modulo de editar ciudades
def Editar_ciudades(datos):
    datos = dict(datos) 
    while True:
        opc = -1
        print()
        print("************************************************")
        print("¿En cual de los siguientes paises quieres editar la ciudad?")
        print("1). Colombia")
        print("2). Argentina")
        print("0). Salir")
        
        try:
            opc= int(input("Ingresa una opcion: "))
        except Exception as e:
            print("Ese valor no es valido")
            print(e)
        
        if opc == 1:
            datos = Edit_Colombia(datos)
        elif opc == 2:
            datos = Edit_Argentina(datos)
        elif opc == 0:
            print("Saliste del apartado de editar")
            print("************************************")
            return datos
    
# Colombia
def Edit_Colombia(datos):
    datos = dict(datos)
    while True:
        opc = -1
        print()
        print("************************************************")
        print("Elegiste colombia")
        print("¿De que departamento de colombia editaras la ciudad?")
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
            datos = Edit_Colombia_Cundinamarca(datos)
        elif opc == 2:  
            datos = Edit_Colombia_Santander(datos)
        elif opc == 3:
            datos = Edit_Colombia_Quindio(datos)
        elif opc == 0:
            print("Salio")
            return datos
        
# Colombia Cundinamarca 
def Edit_Colombia_Cundinamarca(datos):
    datos = dict(datos)
    print()
    print("***********************************************")
    
    try:
        codigo_postal = int(input("Ingresa el codigo postal de la ciudad que va a editar: "))
    except Exception as e:
        print("Ese valor no es valido")
        print(e)
        return datos
    
    for i in datos["pais"]["colombia"]["cundidamarca"]:
        if i["codigo postal"] == codigo_postal:

            try:
                i["ciudad"]=str(input("Ingresa el nuevo nombre de la ciudad: "))
                i["poblacion"]=int(input("Ingresa el nuevo numero de poblacion: "))
                i["codigo postal"]=int(input("Ingresa el nuevo codigo postal: "))
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos
            
            print("Ciudad editada con exito :3")
            return datos
    print("No se encotro esa ciudad")
    return datos
        
# Colombia Santander
def Edit_Colombia_Santander(datos):
    datos = dict(datos)
    print()
    print("***********************************************")
    
    try:
        codigo_postal = int(input("Ingresa el codigo postal de la ciudad que va a editar: "))
    except Exception as e:
        print("Ese valor no es valido")
        print(e)
        return datos
    
    for i in datos["pais"]["colombia"]["santander"]:
        if i["codigo postal"] == codigo_postal:

            try:
                i["ciudad"]=str(input("Ingresa el nuevo nombre de la ciudad: "))
                i["poblacion"]=int(input("Ingresa el nuevo numero de poblacion: "))
                i["codigo postal"]=int(input("Ingresa el nuevo codigo postal: "))
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos
            
            print("Ciudad editada con exito :3")
            return datos
    print("No se encotro esa ciudad")
    return datos
        
# Colombia Quindio
def Edit_Colombia_Quindio(datos):
    datos = dict(datos)
    print()
    print("***********************************************")
    
    try:
        codigo_postal = int(input("Ingresa el codigo postal de la ciudad que va a editar: "))
    except Exception as e:
        print("Ese valor no es valido")
        print(e)
        return datos
    
    for i in datos["pais"]["colombia"]["quindio"]:
        if i["codigo postal"] == codigo_postal:

            try:
                i["ciudad"]=str(input("Ingresa el nuevo nombre de la ciudad: "))
                i["poblacion"]=int(input("Ingresa el nuevo numero de poblacion: "))
                i["codigo postal"]=int(input("Ingresa el nuevo codigo postal: "))
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos
            
            print("Ciudad editada con exito :3")
            return datos
    print("No se encotro esa ciudad")
    return datos
    
# Argentina
def Edit_Argentina(datos):
    datos = dict(datos)
    while True:
        opc = -1
        print()
        print("************************************************")
        print("Elegiste argentina")
        print("¿De que estado de argentina editaras la ciudad?")
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
            datos = Edit_Argentina_SDE(datos)
        elif opc == 2:  
            datos = Edit_Argentina_SJ(datos)
        elif opc == 3:
            datos = Edit_Argentina_SF(datos)
        elif opc == 0:
            print("Salio")
            return datos
             
# Argentina Santiago del Estero
def Edit_Argentina_SDE(datos):
    datos = dict(datos)
    print()
    print("***********************************************")

    try:
        codigo_postal = int(input("Ingresa el codigo postal de la ciudad que va a editar: "))
    except Exception as e:
        print("Ese valor no es valido")
        print(e)
        return datos
    
    for i in datos["pais"]["argentina"]["santiago del estero"]:
        if i["codigo postal"] == codigo_postal:
           
            try:
                i["ciudad"]=str(input("Ingresa el nuevo nombre de la ciudad: "))
                i["poblacion"]=int(input("Ingresa el nuevo numero de poblacion: "))
                i["codigo postal"]=int(input("Ingresa el nuevo codigo postal: "))
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos
            
            print("ciudad editada con exito :3")
            return datos
    print("No se encotro esa ciudad")
    return datos
        
# Argentina San Juan
def Edit_Argentina_SJ(datos):
    datos = dict(datos)
    print()
    print("***********************************************")
            
    try:
        codigo_postal = int(input("Ingresa el codigo postal de la ciudad que va a editar: "))
    except Exception as e:
        print("Ese valor no es valido")
        print(e)
        return datos
    
    for i in datos["pais"]["argentina"]["san juan"]:
        if i["codigo postal"] == codigo_postal:
           
            try:
                i["ciudad"]=str(input("Ingresa el nuevo nombre de la ciudad: "))
                i["poblacion"]=int(input("Ingresa el nuevo numero de poblacion: "))
                i["codigo postal"]=int(input("Ingresa el nuevo codigo postal: "))
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos
            
            print("ciudad editada con exito :3")
            return datos
    print("No se encotro esa ciudad")
    return datos

# Argentina Santa Fe
def Edit_Argentina_SF(datos):
    datos = dict(datos)
    print()
    print("***********************************************")
    
    try:
        codigo_postal = int(input("Ingresa el codigo postal de la ciudad que va a editar: "))
    except Exception as e:
        print("Ese valor no es valido")
        print(e)
        return datos
    for i in datos["pais"]["argentina"]["santa fe"]:
        if i["codigo postal"] == codigo_postal:
           
            try:
                i["ciudad"]=str(input("Ingresa el nuevo nombre de la ciudad: "))
                i["poblacion"]=int(input("Ingresa el nuevo numero de poblacion: "))
                i["codigo postal"]=int(input("Ingresa el nuevo codigo postal: "))
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos
            
            print("ciudad editada con exito :3")
            return datos
    print("No se encotro esa ciudad")
    return datos