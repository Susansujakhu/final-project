# Python program to create
# a pdf file

from datetime import datetime
import tkinter as tk
from tkinter import StringVar, messagebox
from tkinter import font
from tkinter.constants import RIDGE
from typing import Text
from fastai.vision.image import show_image
from fpdf import FPDF
import tkinter.filedialog
from tkinter import Frame, ttk
from PIL import Image, ImageTk
# save FPDF() class into a
# variable pdf

class Window(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, *kwargs)
		ttk.Button(self, text="Open File", command= self.fileOpen).place(relx=0.05, rely=0.05)


	def fileOpen(self):
		self.FILE_name = tkinter.filedialog.askopenfilenames(
			initialdir = ".",
			title      = "Open",
			filetypes  = (
				("Photo files", "*.png"),
				("All", "*.*")
			)
		)
		if self.FILE_name != '':
			self.pdf_title = StringVar()
			self.pdf_name = StringVar()
			ttk.Label(self, text="Pdf Title:").place(relx=0.4, rely=0.4)
			ttk.Entry(self, textvariable= self.pdf_title).place(relx=0.45, rely=0.4)
			ttk.Label(self, text="Pdf Name:").place(relx=0.4, rely=0.45)
			ttk.Entry(self, textvariable= self.pdf_name).place(relx=0.45, rely=0.45)
			ttk.Button(self, text = "Create", command = self.createPdf).place(relx=0.55, rely=0.5, relheight=0.1, relwidth=0.13)

	def createPdf(self):
		pdf = FPDF()
		
		# filename = fileOpen()
		title = (self.pdf_title.get())
		name = str(self.pdf_name.get()) + ".pdf"
		pdf.set_title(title)
		for image_name in self.FILE_name:
			pdf.add_page()
			pdf.image(image_name, h=297, w = 210, x = 0, y = 0)
			print(image_name)


		pdf.output(name)
		messagebox.showinfo(title="Success", Text="PDF successfully created")

def main():
    root = Window()
    root.title('PDF Creator')
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d+0+0'% (width, height))
    root.state('zoomed')
   
    root.bind('<Key-Escape>', lambda event: quit())
    root.update()

    return root


if __name__ == '__main__':

    main().mainloop()