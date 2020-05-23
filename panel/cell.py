"""
    @brief Basic cell class.
    @author DevRamil
"""
from tkinter import Tk, Frame
from tkinter.ttk import Style


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
        #self.style = CELL_STYLE

