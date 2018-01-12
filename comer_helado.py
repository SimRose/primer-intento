si = "Y"
no= "N"
valor_del_helado = 80
respuesta_usuario = input("Quieres comer un helado? Y/N: ").upper()

if respuesta_usuario == si:
     dinero_del_usuario = int(input("Cuanto dinero tienes?:"))
     if dinero_del_usuario >= valor_del_helado:
         print("Entonces compralo")
     else:
         print("No tienes dinero suficiente")
elif respuesta_usuario == no:
    print("Entonces te saludo")
else:
    print("Respuesta invalida")


