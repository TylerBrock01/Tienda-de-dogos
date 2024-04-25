import home
def mostrar_menu():
    try:
        
        respuesta = int(input("#################\n\nmenu de hot dogs:\n[1]\tnormal\n\n[0] CANCELAR pedido\n\nIngrese su opcion:"))
        if respuesta == 0:
            home.funcion_home()
        elif respuesta == 1:
            elegir_ingrediente()
        else:
            print("\n\nIngrese una opcion valida en [mostrar_menu]")
            mostrar_menu()
    except ValueError:
        print("\n\nIngrese una opcion valida en [mostrar_menu]")
        mostrar_menu()
        
def elegir_ingrediente():
    try:
        respuesta = int(input("#################\n\Ingredientes\n[1] mayonesa\n[2] catsup\n[3] cebolla cocida\n[4] cebolla cruda\n[5] salsa(chile)\n[6] con todos los ingredientes\n[7] sin ingredientes\n\n[0] Cancelar operacion"))
        if respuesta == 0:
            home.funcion_home()
        elif respuesta >= 1 and respuesta <=7:
            agregar_ingrediente(respuesta)#evans funcion que debe utilizar
            # mostrar_ingrediente()
            elegir_ingrediente()
        else:
            print("\n\nIngrese una opcion valida en [elegir_ingrediente]")
            elegir_ingrediente()
    except ValueError:
        elegir_ingrediente()

def agregar_ingrediente(respuesta):#evans task
    ingredientes = []    
    try:
        #bloque de ejemplo
        if respuesta == 1:
            print("\nAgregaste mayonesa")
            ingredientes.append("mayonesa")
            elegir_ingrediente()
        #bloques que debe usar el evans v
        elif respuesta == 2:
            ingredientes.append("catsup")
        elif respuesta == 3:
            ingredientes.append("cebolla cocida")
        elif respuesta == 4:
            ingredientes.append("cebolla cruda")
        elif respuesta == 5:
            ingredientes.append("salsa(chile)")
        elif respuesta == 6:
            ingredientes.append("mayonesa")
            ingredientes.append("catsup")
            ingredientes.append("cebolla cocida")
            ingredientes.append("cebolla cruda")
            ingredientes.append("salsa(chile)")
        elif respuesta == 7:
            pass
    except ValueError:
        print("esto no deberia ocurrir")

mostrar_menu()