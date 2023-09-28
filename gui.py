import functions
import PySimpleGUI as sg

sg.theme("DarkAmber")

#creamos las instancias que queremos en la GUI
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

#creamos la ventan de la GUI y el título. En layout añadimos las instancias a mostrar en un list de list. Cada list
#representa una fila
window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read() # muestra la interface con las instancias (buttons y demás). A partir de la siguiente línea va el código

print("Hello")

window.close()