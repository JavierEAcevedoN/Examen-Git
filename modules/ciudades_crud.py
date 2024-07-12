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
            None
        elif choice == 0:
            print("Terminando proceso")
            break
    return datos

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
    
    # colombia
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
        
        
        if opc2== 1:

            print()
            print("***********************************************")
            
            try:
                cundinamarca={}
                cundinamarca["ciudad"]=str(input("ingresa la nueva ciudad dentro del departamento: "))
                cundinamarca["poblacion"]=str(input("ingresa la poblacion de la ciudad: "))
                cundinamarca["codigo postal"]=int(input("ingresa el codigo postal: "))  
                cundinamarca["pais"]=str(input("ingresa al pais que pertenece: "))
                datos["pais"]["colombia"]["cundidamarca"].append(cundinamarca)
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
            
            print("ciudad creada con exito :3")
            return datos
            
                        
        elif opc2==2 :  

            print()
            print("***********************************************")
            
            try:
                santander={}
                santander["ciudad"]=str(input("ingresa la nueva ciudad dentro del departamento: "))
                santander["poblacion"]=str(input("ingresa la poblacion de la ciudad: ")) 
                santander["codigo postal"]=int(input("ingresa el codigo postal: "))  
                santander["pais"]=str(input("ingresa al pais que pertenece: "))
                datos["pais"]["colombia"]["santander"].append(santander)
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
            
            print("ciudad creada con exito :3")
            return datos  
        
        
        elif opc2==3:

            print()
            print("***********************************************")
            
            try:
                quindio={}
                quindio["ciudad"]=str(input("ingresa la nueva ciudad dentro del departamento: "))
                quindio["poblacion"]=str(input("ingresa la poblacion de la ciudad: ")) 
                quindio["codigo postal"]=int(input("ingresa el codigo postal: "))  
                quindio["pais"]=str(input("ingresa al pais que pertenece: "))
                datos["pais"]["colombia"]["quindio"].append(quindio)
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
            
            print("ciudad creada con exito :3")
            return datos 
        
        elif opc2== 4:
            print("salio")
        return datos
        
            
        
        
  #argentina      
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
        
        
        if opc3== 1:

            print()
            print("***********************************************")
            
            try:
                santiago_del_estero={}
                santiago_del_estero["ciudad"]=str(input("ingresa la nueva ciudad dentro del departamento: "))
                santiago_del_estero["poblacion"]=str(input("ingresa la poblacion de la ciudad: ")) 
                santiago_del_estero["codigo postal"]=int(input("ingresa el codigo postal: "))  
                santiago_del_estero["pais"]=str(input("ingresa al pais que pertenece: "))
                datos["pais"]["argentina"]["santiago del estero"].append(santiago_del_estero)
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
            
            print("ciudad creada con exito :3")
            return datos
            
                        
        elif opc3==2 :  

            print()
            print("***********************************************")
            
            try:
                san_juan={}
                san_juan["ciudad"]=str(input("ingresa la nueva ciudad dentro del departamento: "))
                san_juan["poblacion"]=str(input("ingresa la poblacion de la ciudad: ")) 
                san_juan["codigo postal"]=int(input("ingresa el codigo postal: "))  
                san_juan["pais"]=str(input("ingresa al pais que pertenece: "))
                datos["pais"]["argentina"]["san juan"].append(san_juan)
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
            
            print("ciudad creada con exito :3")
            return datos  
        
        
        elif opc3==3:
            
            print()
            print("***********************************************")
            
            try:
                santa_fe={}
                santa_fe["ciudad"]=str(input("ingresa la nueva ciudad dentro del departamento: "))
                santa_fe["poblacion"]=str(input("ingresa la poblacion de la ciudad: ")) 
                santa_fe["codigo postal"]=int(input("ingresa el codigo postal: "))  
                santa_fe["pais"]=str(input("ingresa al pais que pertenece: "))
                datos["pais"]["argentina"]["santa fe"].append(santa_fe)
            except Exception as e:
                print("Ese valor no es valido")
                print(e)
            
            print("ciudad creada con exito :3")
            return datos 
        
        elif opc3== 4:
            print("salio")
        
        return datos
    
    elif opc==3:
        print("saliste del apartado de agregar")
        print("************************************")
    
    return datos 