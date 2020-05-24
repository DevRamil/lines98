"""
    @brief Basic cell class.
    @author DevRamil
"""
from tkinter import Tk, Frame, Canvas, constants as cnst
from view.constant import CELL_WIDTH, CELL_HEIGHT


class Cell(Frame):
    """
        @brief Basic cell class.
        @author DevRamil
    """
    def __init__(self, root):
        """
            @param root base parent element,
            @author DevRamil
        """
        Frame.__init__(self, root, background="blue")
        self.root = root
        self.config(width=CELL_WIDTH, height=CELL_HEIGHT)
        #self.style = CELL_STYLE

        canvas = Canvas(self)
        canvas.create_oval(5, 5, CELL_WIDTH-2, CELL_HEIGHT-2, outline="gray", fill="gray")
        canvas.config(width=CELL_WIDTH, height=CELL_HEIGHT, background="blue")
        canvas.pack(expand=cnst.YES)

