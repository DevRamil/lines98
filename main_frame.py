"""
    @brief Build main frame class.
    @author DevRamil
"""
from tkinter import Tk
from menu.main_menu import MainMenu


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