import functions
import FreeSimpleGUI as Gui


label = Gui.Text("Type in a to-do")
input_box = Gui.InputText(tooltip="Enter todo")
add_button = Gui.Button("Add")

window = Gui.Window('My To-Do App', layout=[[label, input_box, add_button]])
window.read()
window.close()

