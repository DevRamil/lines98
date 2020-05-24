from tkinter import Tk, Button, constants as cnst
from view.main_frame import MainFrame


try:
    """
    w_button_1 = Button(root, text='Файл')
    w_button_1.pack(side=LEFT)


    widget = Label(root)
    widget.config(text='Hello my world!')
    widget.pack(side=TOP, expand=YES, fill=BOTH)
    

    root.columnconfigure(0, pad=3)
    root.columnconfigure(1, pad=3)
    root.columnconfigure(2, pad=3)
    root.columnconfigure(3, pad=3)
        
    root.rowconfigure(0, pad=3)
    root.rowconfigure(1, pad=3)
    root.rowconfigure(2, pad=3)
    root.rowconfigure(3, pad=3)
    root.rowconfigure(4, pad=3)
    """
    MainFrame()

except Exception as exc:
    print('Somthing wrong: ' + str(exc))