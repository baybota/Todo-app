import functions
import time
import FreeSimpleGUI as Gui


# Gui theme
Gui.theme('DarkTeal2')

# Label, input, and list box for gui
clock = Gui.Text('', key='clock')
label = Gui.Text("Type in a to-do")
input_box = Gui.InputText(tooltip="Enter todo", key='todo')
list_box = Gui.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=(45, 10))

# Buttons for gui
add_button = Gui.Button("Add")
edit_button = Gui.Button("Edit")
complete_button = Gui.Button("Complete")
exit_button = Gui.Button("Exit")

# GUi window and its layout
window = Gui.Window('My To-Do App',
                    layout=[[label, clock],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b-%d-%y %H:%M:%S"))

    match event:

        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "Edit":
            try:
                todo_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                Gui.popup("Please select an item", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                Gui.popup("Please select an item", font=("Helvetica", 20))

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case Gui.WIN_CLOSED:
            break
window.close()

