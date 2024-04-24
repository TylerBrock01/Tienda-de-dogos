#invocar menu
def funcion_home():
    try:
        respuesta = int(input("#########################\nBienvenido a dogoshit\nle mostramos el menu\n [1] Ordenar\n [2] Modificar\n [3] verificar pedido\n\n_______________________________\nIngrese una opcion:"))
        funcion_agregar(respuesta)
    except ValueError:
        print("\n\nhome opcion invalida")
        funcion_home()

def funcion_agregar(respuesta):
    if respuesta == 1:
        import comida
        comida.mostrar_menu()
    elif respuesta == 2:
        print("elegiste la opcion 2")
            
    else:
        print("#########################\n\n")
        print("opcion no valida")
        funcion_home()