""" Messing about with tkinter """
import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import messagebox
from fastai.basic_train import load_learner
from fastai.vision.image import open_image
import numpy as np
from fastai import *
from fastai.vision import *
# from fastai.vision.all import *

import tkinter.filedialog

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

        for frame in (Main, Predict):
            current_frame = frame(container, self)
            self.frames[frame] = current_frame
            current_frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Main)

    def show_frame(self, cont):
        """ Raises a particular frame, bringing it into view """

        frame = self.frames[cont]
        frame.tkraise()

class Main(tk.Frame):
    """ Main frame of program """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.makeWidgets()
        menubar = tk.Menu(controller)
        mFile = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="File", menu=mFile)

        # mFile.add_command(label="Open", command=self.checkView)
        # mFile.add_command(label="Save", command=self.check_saveView)
        mFile.add_separator()
        mFile.add_command(label="Exit", command=lambda: quit())

        # Help Section
        mHelp = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Help", menu=mHelp)

        mHelp.add_command(label="About")
        controller.config(menu=menubar)

        # Hospitall name
        ttk.Label(self,font= ('Arial', 25), text="Knee OA Detection System").place(relx = 0.3, rely =0.01)

        # ******* Buttons ADD and Send ***********
        ttk.Button(self, text= "Add & Send", command= self).place(
            relx=0.4,rely=0.27)
        ttk.Button(self, text= "Clear", command= self.clear).place(relx=0.5,rely=0.27)


        ttk.Button(self, text= "Send", command= lambda : controller.show_frame(Predict)).place(relx=0.7,rely=0.9)
        ttk.Button(self, text= "Clear", command= self).place(relx=0.8,rely=0.9)

    def makeWidgets(self):

        self.id_text = StringVar()
        self.name_text = StringVar()
        self.address_text = StringVar()
        self.city_text = StringVar()
        self.gender_value = StringVar()
        self.age_value = StringVar()
        self.contact_text = StringVar()
        self.blood_value = StringVar()
        
        
        style = entryStyle = labelStyle = buttonStyle = ttk.Style()
        style.configure('.', font=('Helvetica', 12))
        entryStyle.configure('TEntry',foreground = 'green')
        labelStyle.configure('TLable', )
        buttonStyle.configure('TButton',background='#232323', foreground = 'black', borderwidth=1, focusthickness=3, focuscolor='green')
        buttonStyle.map('TButton', background=[('active','green')])

        # Patient Id
        ttk.Label(self, text="Patient Id:").place(relx = 0.05, rely =0.1)
        ttk.Entry(self, font = ('Arial', 12), textvariable = self.id_text, style="TEntry").place(
            relx = 0.11, rely =0.1, width=200, height=25)

        # Name
        ttk.Label(self, text="Full Name:").place(relx = 0.3, rely =0.1)
        ttk.Entry(self, font = ('Arial', 12), textvariable = self.name_text, style="TEntry").place(
            relx = 0.37, rely =0.1, width=250, height=25)

        # Gender
        ttk.Label(self, text="Gender:").place(relx = 0.6, rely =0.1)
       
        # Gender Combobox
        self.gender = ttk.Combobox(self, textvariable=self.gender_value, 
                                state='readonly')
        self.gender['values'] = ('None', 'Male', 'Female')
        self.gender.current()
        self.gender.place(
             relx = 0.65, rely =0.1, width=100, height=25)

        # Age
        ttk.Label(self, text="Age:").place(relx = 0.77, rely =0.1)
        ttk.Entry(self, font = ('Arial', 12), textvariable = self.age_value).place(
            relx = 0.8, rely =0.1, width=100, height=25)
        
        #********************************************************************

        # Blood Group
        ttk.Label(self, text="Blood Group:").place(relx = 0.05, rely =0.18)
        self.blood_group = ttk.Combobox(self, textvariable=self.blood_value, 
                                state='readonly')
        self.blood_group['values'] = ('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-')
        self.blood_group.current()
        self.blood_group.place(
            relx = 0.13, rely =0.18, width=150, height=25)

        # Contact Number
        ttk.Label(self, text="Contact No.:").place(relx = 0.3, rely =0.18)
        ttk.Entry(self, font = ('Arial', 12), textvariable = self.contact_text, style="TEntry").place(
            relx = 0.37, rely =0.18, width=200, height=25)

        # Address
        ttk.Label(self, text="Address:").place(relx = 0.55, rely =0.18)
        ttk.Entry(self, font = ('Arial', 12), textvariable = self.address_text).place(
            relx = 0.6, rely =0.18, width=200, height=25)
        
        # City
        ttk.Label(self, text="City:").place(relx = 0.77, rely =0.18)
        ttk.Entry(self, font = ('Arial', 12), textvariable = self.city_text).place(
            relx = 0.8, rely =0.18, width=100, height=25)


    def clear(self):
        self.id_text.set("")
        self.name_text.set("")
        self.address_text.set("")
        self.city_text.set("")
        self.gender_value.set("")
        self.age_value.set("")
        self.contact_text.set("")
        self.blood_value.set("")






class Predict(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Load Model
    #     self.x = load_learner('F:\\8thproject\\', 'final.pkl') 

    #     label = tk.Label(self, text="Preditions", font=LARGE_FONT)
    #     label.pack(pady=10, padx=10)

    #     self.fileName = ""
    #     # File Explorer Button
    #     ttk.Button(self, text= "Open File", command= self.fileOpen).place(x=100, y=0)

    #     # Predict Button
    #     ttk.Button(self, text= "Predict", 
    #     command= self.showResult).place(x=100,y=100)

    #     # Move to Previous Frame
    #     ttk.Button(self, text= "Page 1", command= lambda : controller.show_frame(Main)).place(x=200, y=100)

    # def fileOpen(self):
    #     FILE_name = tk.filedialog.askopenfilename(
    #         initialdir = ".",
    #         title      = "Open",
    #         filetypes  = (
    #             ("Photo files", "*.png"),
    #             ("All", "*.*")
    #         )
    #     )
    #     if FILE_name:
    #         self.fileName = FILE_name
    
    # def showResult(self):
    #     if self.fileName == "":
    #         messagebox.showinfo(title = "Alert",message = "Please Open Any File First")
    #     else:
    #         img = open_image(self.fileName)
    #         predict = self.x.predict(img)
    #         max_value = max(predict[2],key=lambda x:float(x)) 
    #         print("KL Grade : "+ str(predict[0]) + " with value " + str(max_value.item()*100))
    #         result = "KL Grade : "+ str(predict[0]) + " with value " + str(max_value.item()*100)
    #         ttk.Label(self, text= result).place(relx = 0.3, rely =0.1)

    

def main():
    root = Window()
    root.title('xl2web')
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d+0+0'% (width, height))
    root.state('zoomed')
   
    root.bind('<Key-Escape>', lambda event: quit())
    root.update()

    return root


if __name__ == '__main__':
    main().mainloop()