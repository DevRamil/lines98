from tkinter import Tk, Button, constants as cnst
from menu.main_menu import MainMenu
from panel.cell import Cell


try:
    root = Tk()
    root.title('lines98')

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
    cls1 = Cell(root).pack(expand=cnst.YES, fill=cnst.X, padx=5)
    cls2 = Cell(root).pack(expand=cnst.YES, fill=cnst.X, padx=5)\
    
    root.geometry('495x600+200+200')
    root.resizable(0, 0)
    root.config(menu=MainMenu())
    root.mainloop()

except Exception as exc:
    print('Somthing wrong: ' + str(exc))