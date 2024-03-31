import modules.functions as functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter to-do", key="todo")
add_button = Sg.Button("Add")
list_box = Sg.Listbox(values= functions.get_todos(),
                      key='list',
                      enable_events=True,
                      size=(45, 10))
edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")
exit_button = Sg.Button("Exit")

window = Sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
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
            window['list'].update(values=to_dos)

        case "Edit":
            todo_to_edit = values['list'][0]
            new_todo = values['todo']

            to_dos = functions.get_todos()
            index = to_dos.index(todo_to_edit)
            to_dos[index] = new_todo
            functions.write_todos(to_dos)
            window['list'].update(values=to_dos)

        case "Complete":
            to_do_to_complete = values['list'][0]
            to_dos = functions.get_todos()
            to_dos.remove(to_do_to_complete)
            functions.write_todos(to_dos)
            window['list'].update(values=to_dos)
            window['todo'].update(value="")

        case "Exit":
            break

        case 'list':
            window['todo'].update(value=values['list'][0])

        case Sg.WINDOW_CLOSED:
            break


window.close()
