import PySimpleGUI as sg
import ctypes
from fileSorter import *

sg.theme('Dark Blue 3')
sg.set_options(auto_size_text=True, margins=(25,25))
ctypes.windll.shcore.SetProcessDpiAwareness(True)

layout = [
            [sg.Text('Origin', size=(10, 1)), sg.InputText("", key='origin', do_not_clear=False), sg.FolderBrowse()],
            [sg.Text('Destination', size=(10, 1)), sg.InputText("", key='destination',do_not_clear=False), sg.FolderBrowse()],
            [sg.Text('Folder Prefix', size=(10,1)),sg.InputText("", key='prefix', do_not_clear=False)],
            [sg.Submit("Sort Files", key="Submit")]
            ]

window = sg.Window('File Sorter 9000', layout, icon="C:/Users/Pulido/Documents/College/Fall2022/Python/Scripts/FileSorterGUI/icon.ico")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if(event == "Submit"):
        if(values["origin"] != "" and values["destination"] != ""):
            fsWorker = FileSorter(values["origin"], values["destination"], values["prefix"])
            fsWorker.start()
            sg.Popup(f"Sorted {fsWorker.count} files!", keep_on_top=True, title="Files Sorted")
        
window.close()