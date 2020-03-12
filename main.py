from tkinter import *


root = Tk()

w_button_1 = Button(root, text='Файл')
w_button_1.pack(side=LEFT)


widget = Label(root)
widget.config(text='Hello my world!')
widget.pack(side=TOP, expand=YES, fill=BOTH)

root.title('lines98')
root.mainloop()