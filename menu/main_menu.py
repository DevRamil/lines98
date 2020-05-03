"""
    @author DevRamil
"""
from tkinter import Menu
from tkinter.constants import *


class MainMenu(Menu):
    """
        @author DevRamil
    """
    def __init__(self):
        """
            @author DevRamil
        """
        Menu.__init__(self)
        self.add_cascade(label="File")
        self.add_cascade(label="Edit")
        self.add_cascade(label="View",)


        self.add_command(label='Leaderboard')

        self.add_separator()
