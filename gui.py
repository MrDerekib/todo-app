import functions
import PySimpleGUI as sg

sg.theme("DarkAmber")

# creamos las instancias que queremos en la GUI
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# Creamos la ventana de la GUI y el título. En layout añadimos las instancias a mostrar en un list de list. Cada list
# representa una fila
window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 16))
#window.read()  # muestra la interface con las instancias (buttons y demás). A partir de la siguiente línea va el código

while True:
    event, values = window.read()
    # print(1, event)
    # print(2, values)
    # print(3, values["todos"])
    match event:
        case "Add":
            todos = functions.get_todos()
            # print(todos)
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            # print(todos)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Exit":
            break
        case "todos": #copia el valor seleccionado del Listbox al Textbox
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break

window.close()
