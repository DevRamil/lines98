"""
    @brief Build main frame class.
    @author DevRamil
"""
from tkinter import Tk
from view.constant import CELL_WIDTH, CELL_HEIGHT
from view.menu.main_menu import MainMenu
from view.cell import Cell


class MainFrame():
    """
        @brief Wrapper for filling Tk.
        @author DevRamil
    """
    def __init__(self):
        """
            @author DevRamil
        """
        self.root = Tk()
        self.root.title('lines98')

        self.width = CELL_WIDTH * 9 + 10
        self.height = CELL_WIDTH * 10 + 11

        self.root.geometry(str(self.width) + 'x' + str(self.height) + '+200+200')
        self.root.resizable(0, 0)
        self.root.config(menu=MainMenu())
        
        cls1 = Cell(self.root).pack()
        cls2 = Cell(self.root).pack()

        self.root.mainloop()