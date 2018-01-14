numero_ganador = 5
print("Bienvenido al juego, tienes 3 intentos")
numero_del_usuario = int(input("Adivina un numero del 1 al 10:  "))
intentos_restantes = 3

while intentos_restantes > 0:
    if numero_del_usuario != numero_ganador and numero_del_usuario > 0 and numero_del_usuario < 11:
        intentos_restantes -= 1
        print("¡Incorrecto!")
        print("Intentos restantes: {}".format(intentos_restantes))
        numero_del_usuario = int(input("Adivina un numero del 1 al 10:  "))
    elif numero_del_usuario > 10 or numero_del_usuario < 1:
        print("¡He dicho que solo numeros del 1 al 10!")
        intentos_restantes -= 1
        print("Intentos restantes: {}".format(intentos_restantes))
        numero_del_usuario = int(input("Adivina un numero del 1 al 10:  "))
    else:
        intentos_restantes -= 3
        print("¡Correcto!")
        print("¡Hasta la próxima!")

if numero_del_usuario != numero_ganador:
    print("¡Incorrecto!")
    print("¡Has perdido!")
    print("¡Hasta la próxima!")






