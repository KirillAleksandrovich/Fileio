from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import requests
from PyInstaller.loader.pyiboot01_bootstrap import entry
from bottle import response


def upload():
    filepath = fd.askopenfilename()
    if filepath:
        files = {'file': open(filepath,'rb')}
        response = requests.post('https://file.io', files=files)
        if response.status_code == 200:
            link = response.json()['link']
            entry.insert(0, link)

window = Tk()
window.title('Сохранение файла в облаке')
window.geometry('400x200')


button = ttk.Button(text='Загрузить фаил', command=upload)
button.pack()

entry = ttk.Entry()
entry.pack()

window.mainloop()