import modules.functions as functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter to-do", key="todo")
add_button = Sg.Button("Add")

window = Sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            to_dos = functions.get_todos()
            new_item = values['todo'] + "\n"
            to_dos.append(new_item)
            functions.write_todos(to_dos)
        case Sg.WINDOW_CLOSED:
            break


window.close()
