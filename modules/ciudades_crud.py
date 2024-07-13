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
    datos =dict(datos)

    print()
    print("************************************************")
    print("¿En cual de los siguientes paises quieres agregar la ciudad?")
    print("1). Colombia")
    print("2). Argentina")
    print("3). Salir")
    
    try:
        opc= int(input("ingresa una opcion: "))
    except Exception as e:
            print("Ese valor no es valido")
            print(e)
    
    # Colombia
    if opc == 1:

        print()
        print("************************************************")
        print("Elegiste colombia")
        print("¿de que departamento de colombia agregaras la ciudad?")
        print("1). Cundinamarca")
        print("2). Santander")
        print("3). Quindio")
        print("4). Salir")
        try:    
            opc2=int(input("ingresa una opcion: "))
        except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos
        
        
        if opc2== 1:

            print()
            print("***********************************************")
            
            try:
                cundinamarca={}
                cundinamarca["ciudad"]=str(input("ingresa la nueva ciudad dentro del departamento: "))
                cundinamarca["poblacion"]=int(input("ingresa la poblacion de la ciudad: "))
                cundinamarca["codigo postal"]=int(input("ingresa el codigo postal: "))  
                datos["pais"]["colombia"]["cundidamarca"].append(cundinamarca)
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos
            
            print("ciudad creada con exito :3")
            return datos
            
                        
        elif opc2==2 :  

            print()
            print("***********************************************")
            
            try:
                santander={}
                santander["ciudad"]=str(input("ingresa la nueva ciudad dentro del departamento: "))
                santander["poblacion"]=int(input("ingresa la poblacion de la ciudad: ")) 
                santander["codigo postal"]=int(input("ingresa el codigo postal: "))  
                datos["pais"]["colombia"]["santander"].append(santander)
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos
            
            print("ciudad creada con exito :3")
            return datos  
        
        
        elif opc2==3:

            print()
            print("***********************************************")
            
            try:
                quindio={}
                quindio["ciudad"]=str(input("ingresa la nueva ciudad dentro del departamento: "))
                quindio["poblacion"]=int(input("ingresa la poblacion de la ciudad: ")) 
                quindio["codigo postal"]=int(input("ingresa el codigo postal: "))  
                datos["pais"]["colombia"]["quindio"].append(quindio)
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos
            
            print("ciudad creada con exito :3")
            return datos 
        
        elif opc2== 4:
            print("salio")
            return datos

        else:
            print("Esa opcion no es valida")
            return datos
        
        
        
        
    #Argentina      
    elif opc == 2:

        print()
        print("************************************************")
        print("Elegiste Argentina")
        print("¿de que estado de Argentina agregaras la ciudad?")
        print("1). Santiago del estero")
        print("2). San juan")
        print("3). Santa fe")
        print("4). Salir")
        try:
            opc3=int(input("ingresa una opcion: "))
        except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos
        
        
        if opc3== 1:

            print()
            print("***********************************************")
            
            try:
                santiago_del_estero={}
                santiago_del_estero["ciudad"]=str(input("ingresa la nueva ciudad dentro del departamento: "))
                santiago_del_estero["poblacion"]=int(input("ingresa la poblacion de la ciudad: ")) 
                santiago_del_estero["codigo postal"]=int(input("ingresa el codigo postal: "))  
                datos["pais"]["argentina"]["santiago del estero"].append(santiago_del_estero)
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos
            
            print("ciudad creada con exito :3")
            return datos
            
                        
        elif opc3==2 :  

            print()
            print("***********************************************")
            
            try:
                san_juan={}
                san_juan["ciudad"]=str(input("ingresa la nueva ciudad dentro del departamento: "))
                san_juan["poblacion"]=int(input("ingresa la poblacion de la ciudad: ")) 
                san_juan["codigo postal"]=int(input("ingresa el codigo postal: "))  
                datos["pais"]["argentina"]["san juan"].append(san_juan)
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos
            
            print("ciudad creada con exito :3")
            return datos  
        
        
        elif opc3==3:
            
            print()
            print("***********************************************")
            
            try:
                santa_fe={}
                santa_fe["ciudad"]=str(input("ingresa la nueva ciudad dentro del departamento: "))
                santa_fe["poblacion"]=int(input("ingresa la poblacion de la ciudad: ")) 
                santa_fe["codigo postal"]=int(input("ingresa el codigo postal: "))  
                datos["pais"]["argentina"]["santa fe"].append(santa_fe)
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos
            
            print("ciudad creada con exito :3")
            return datos 
        
        elif opc3== 4:
            print("salio")
            return datos

        else:
            print("Esa opcion no es valida")
            return datos
    
    elif opc==3:
        print("saliste del apartado de agregar")
        print("************************************")
        return datos

# Modulo de editar ciudades
def Editar_ciudades(datos):
    datos = dict(datos) 

    print()
    print("************************************************")
    print("¿En cual de los siguientes paises quieres editar la ciudad?")
    print("1). Colombia")
    print("2). Argentina")
    print("3). Salir")
    
    try:
        opc= int(input("ingresa una opcion: "))
    except Exception as e:
            print("Ese valor no es valido")
            print(e)
    
    # Colombia
    if opc == 1:

        print()
        print("************************************************")
        print("Elegiste colombia")
        print("¿de que departamento de colombia editaras la ciudad?")
        print("1). Cundinamarca")
        print("2). Santander")
        print("3). Quindio")
        print("4). Salir")
        try:
            opc2=int(input("ingresa una opcion: "))
        except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos
        
        
        if opc2== 1:

            print()
            print("***********************************************")
            
            try:
                codigo_postal = int(input("ingresa el codigo postal de la ciudad que va a editar: "))
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos

            for i in datos["pais"]["colombia"]["cundidamarca"]:
                if i["codigo postal"] == codigo_postal:
                    
                    try:
                        i["ciudad"]=str(input("ingresa el nuevo nombre de la ciudad: "))
                        i["poblacion"]=int(input("ingresa el nuevo numero de poblacion: "))
                        i["codigo postal"]=int(input("ingresa el nuevo codigo postal: "))  
                        datos["pais"]["colombia"]["cundidamarca"].update(i)
                    except Exception as e:
                        print("Ese valor no es valido")
                        print(e)
                        return datos
                    print("ciudad editada con exito :3")
                    return datos
            print("No se encotro esa ciudad")
            return datos
        
        elif opc2==2 :

            print()
            print("***********************************************")
            
            try:
                codigo_postal = int(input("ingresa el codigo postal de la ciudad que va a editar: "))
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos

            for i in datos["pais"]["colombia"]["santander"]:
                if i["codigo postal"] == codigo_postal:
                    
                    try:
                        i["ciudad"]=str(input("ingresa el nuevo nombre de la ciudad: "))
                        i["poblacion"]=int(input("ingresa el nuevo numero de poblacion: "))
                        i["codigo postal"]=int(input("ingresa el nuevo codigo postal: "))  
                        datos["pais"]["colombia"]["santander"].update(i)
                    except Exception as e:
                        print("Ese valor no es valido")
                        print(e)
                        return datos
                    print("ciudad editada con exito :3")
                    return datos
            print("No se encotro esa ciudad")
            return datos
        
        elif opc2==3:

            print()
            print("***********************************************")
            
            try:
                codigo_postal = int(input("ingresa el codigo postal de la ciudad que va a editar: "))
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos

            for i in datos["pais"]["colombia"]["quindio"]:
                if i["codigo postal"] == codigo_postal:
                    
                    try:
                        i["ciudad"]=str(input("ingresa el nuevo nombre de la ciudad: "))
                        i["poblacion"]=int(input("ingresa el nuevo numero de poblacion: "))
                        i["codigo postal"]=int(input("ingresa el nuevo codigo postal: "))  
                        datos["pais"]["colombia"]["quindio"].update(i)
                    except Exception as e:
                        print("Ese valor no es valido")
                        print(e)
                        return datos
                    print("ciudad editada con exito :3")
                    return datos
            print("No se encotro esa ciudad")
            return datos
        
        elif opc2== 4:
            print("salio")
            return datos

        else:
            print("Esa opcion no es valida")
            return datos
    
    # Argentina
    elif opc == 2:

        print()
        print("************************************************")
        print("Elegiste argentina")
        print("¿de que estado de argentina editaras la ciudad?")
        print("1). Santiago del estero")
        print("2). San juan")
        print("3). Santa fe")
        print("4). Salir")
        try:
            opc3=int(input("ingresa una opcion: "))
        except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos
        
        
        if opc3== 1:

            print()
            print("***********************************************")
            
            try:
                codigo_postal = int(input("ingresa el codigo postal de la ciudad que va a editar: "))
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos

            for i in datos["pais"]["argentina"]["santiago del estero"]:
                if i["codigo postal"] == codigo_postal:
                    
                    try:
                        i["ciudad"]=str(input("ingresa el nuevo nombre de la ciudad: "))
                        i["poblacion"]=int(input("ingresa el nuevo numero de poblacion: "))
                        i["codigo postal"]=int(input("ingresa el nuevo codigo postal: "))  
                        datos["pais"]["argentina"]["santiago del estero"].update(i)
                    except Exception as e:
                        print("Ese valor no es valido")
                        print(e)
                        return datos
                    print("ciudad editada con exito :3")
                    return datos
            print("No se encotro esa ciudad")
            return datos
        
        elif opc3==2 :

            print()
            print("***********************************************")
            
            try:
                codigo_postal = int(input("ingresa el codigo postal de la ciudad que va a editar: "))
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos

            for i in datos["pais"]["argentina"]["san juan"]:
                if i["codigo postal"] == codigo_postal:
                    
                    try:
                        i["ciudad"]=str(input("ingresa el nuevo nombre de la ciudad: "))
                        i["poblacion"]=int(input("ingresa el nuevo numero de poblacion: "))
                        i["codigo postal"]=int(input("ingresa el nuevo codigo postal: "))  
                        datos["pais"]["argentina"]["san juan"].update(i)
                    except Exception as e:
                        print("Ese valor no es valido")
                        print(e)
                        return datos
                    print("ciudad editada con exito :3")
                    return datos
            print("No se encotro esa ciudad")
            return datos

        elif opc3==3:

            print()
            print("***********************************************")
            
            try:
                codigo_postal = int(input("ingresa el codigo postal de la ciudad que va a editar: "))
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
                return datos

            for i in datos["pais"]["argentina"]["santa fe"]:
                if i["codigo postal"] == codigo_postal:
                    
                    try:
                        i["ciudad"]=str(input("ingresa el nuevo nombre de la ciudad: "))
                        i["poblacion"]=int(input("ingresa el nuevo numero de poblacion: "))
                        i["codigo postal"]=int(input("ingresa el nuevo codigo postal: "))  
                        datos["pais"]["argentina"]["santa fe"].update(i)
                    except Exception as e:
                        print("Ese valor no es valido")
                        print(e)
                        return datos
                    print("ciudad editada con exito :3")
                    return datos
            print("No se encotro esa ciudad")
            return datos
        
        elif opc3== 4:
            print("salio")
            return datos

        else:
            print("Esa opcion no es valida")
            return datos
    
    elif opc==3:
        print("saliste del apartado de agregar")
        print("************************************")
        return datos

    else:
        print("Esa opcion no es valida")
        return datos