""" Messing about with tkinter """
import tkinter as tk
from tkinter import Frame, PhotoImage, StringVar, ttk
from tkinter import messagebox
from tkinter import font
#from tkinter import font
from tkinter.constants import DISABLED, RIDGE, X
from tkinter.font import BOLD
# from fastai.basic_train import load_learner
# from fastai.vision.image import open_image

import numpy as np
from fastai import *
from fastai.vision import *

import tkinter.filedialog
import openpyxl
from openpyxl import Workbook
from datetime import datetime
from os import name, path
from openpyxl import load_workbook
from PIL import Image, ImageTk
import report_generator
from first import First
from search import SearchUser
from interface import Interface
from predict import Predict

LARGE_FONT = ("Verdana", 12)

class Window(tk.Tk):
    """ Main class """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for frame in (Interface, Predict, First, SearchUser):
            current_frame = frame(container, self)
            self.frames[frame] = current_frame
            current_frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(First)

    def show_frame(self, cont):
        """ Raises a particular frame, bringing it into view """
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]


def main():
    
    root = Window()
    root.title('Knee OA')
    #root.configure(bg='green')
    
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d+0+0'% (width, height))
    root.state('zoomed')
    #root.resizable(False,False)
    # root.iconbitmap('./assets/pythontutorial.ico')
    root.bind('<Key-Escape>', lambda event: quit())
    root.update()

    return root


if __name__ == '__main__':

    main().mainloop()
    
    