def mostrar_menu():
    try:
        
        respuesta = int(input("#################\n\nmenu de hot dogs:\n[1]\tnormal\n\n[0] CANCELAR pedido\n\nIngrese su opcion:"))
        if respuesta == 0:
            import home
            home.funcion_home()
        elif respuesta >= 1:
            mostrar_ingredientes()
            
    except ValueError:
        print("\n\nIngrese una opcion valida en [mostrar_menu]")
        mostrar_menu()
        
def mostrar_ingredientes():
    respuesta = int(input(""))