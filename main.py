from tkinter import *


root = Tk()

widget = Label(root)
widget.config(text='Hello my world!')
widget.pack(side=TOP, expand=YES, fill=BOTH)

root.title('lines98')
root.mainloop()