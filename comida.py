import home
def mostrar_menu():
    try:
        
        respuesta = int(input("#################\n\nmenu de hot dogs:\n[1]\tnormal\n\n[0] CANCELAR pedido\n\nIngrese su opcion:"))
        if respuesta == 0:
            home.funcion_home()
        elif respuesta >= 1:
            elegir_ingrediente()
            
    except ValueError:
        print("\n\nIngrese una opcion valida en [mostrar_menu]")
        mostrar_menu()
        
def elegir_ingrediente():
    try:
        ingredientes = []
        respuesta = int(input("#################\n\Ingredientes\n[1] mayonesa\n[2] catsup\n[3] cebolla cocida\n[4] cebolla cruda\n[5] salsa(chile)\n[6] con todos los ingredientes\n[7] sin ingredientes\n\n[0] Cancelar operacion"))
        if respuesta == 0:
            home.funcion_home()
        elif respuesta >= 1 and respuesta <=7:
            # agregar_ingrediente(respuesta)
            # mostrar_ingrediente()
            elegir_ingrediente()
    except ValueError:
        elegir_ingrediente()
 