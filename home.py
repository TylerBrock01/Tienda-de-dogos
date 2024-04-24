#invocar menu
def funcion_home():
    respuesta = int(input(" \n\n#########################\nBienvenido a dogoshit\nle mostramos el menu\n [1] Ordenar\n [2] Modificar\n [3] verificar pedido\n [0] salir\n_______________________________\nIngrese una opcion:"))
    funcion_agregar(respuesta)

def funcion_agregar(respuesta):
    try:
        if respuesta == 1:
            import comida
            comida.mostrar_menu()
        elif respuesta == 2:
            print("elegiste la opcion 2")
        else:
            print("#########################\n\n")
            print("opcion no valida")
            funcion_home()
    except ValueError:
        print("#########################\n\n")
        print("opcion no valida")
        funcion_home()
