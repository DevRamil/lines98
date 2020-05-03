from tkinter import *
from menu.main_menu import MainMenu

try:
    root = Tk()
    root.title('lines98')
    root.geometry('300x250')

    w_button_1 = Button(root, text='Файл')
    w_button_1.pack(side=LEFT)


    widget = Label(root)
    widget.config(text='Hello my world!')
    widget.pack(side=TOP, expand=YES, fill=BOTH)

    root.config(menu=MainMenu())
    root.mainloop()

except Exception as exc:
    print('Somthing wrong: ' + str(exc))