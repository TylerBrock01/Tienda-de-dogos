from bucle import bucles
class home:
    loop = bucles()
    #invocar menu
    def funcion_menu(self,respuesta):
        respuesta = input("Bienvenido a dogoshit\nle mostramos el menu\n [1] Ordenar\n [2] Modificar\n [3] verificar pedido\n [0] salir")
        self.loop.bucle_menu(respuesta)
        #fin de codigo
