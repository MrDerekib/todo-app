import functions
import PySimpleGUI as sg

sg.theme("DarkAmber")

# creamos las instancias que queremos en la GUI
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

# Creamos la ventana de la GUI y el título. En layout añadimos las instancias a mostrar en un list de list. Cada list
# representa una fila
window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20))
#window.read()  # muestra la interface con las instancias (buttons y demás). A partir de la siguiente línea va el código

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            print(todos)
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            print(todos)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
