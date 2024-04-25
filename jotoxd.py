while True:
    print("Hola bienvenido, este es un test---Te diremos que tipo de persona eres---")
    print("1- que streamer prefieres?\n[0]Didiwinx\n[1]Auronplay\n[2]Puvlo\n[3]Salir")
    answer = int(input("selecciona tu respuesta:"))
    if answer == 0:
        print("##Eres un pajero##")

    elif answer == 1:
        print("##eres un basado##")

    elif answer == 2:
        print("##eres raro pero buena onda##")

    elif answer == 3:
        print("seguro que quieres salir?")
        answer = (input("s/n\n  Respuesta:"))
        break
        
