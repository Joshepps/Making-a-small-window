#Building simple graphics interface
import PySimpleGUI as sg
layout = [[sg.Text("Hello I'm a test program")], [sg.Button("OK")]]
window = sg.Window("Demo", layout)
#Event loop)

while True:
    event, values = window.read()
    #Will terminate if user closes window or presses OK
    if event == "OK" or event == sg.WIN_Closed:
        break
window.close()
