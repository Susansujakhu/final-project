""" Messing about with tkinter """
import tkinter as tk
from tkinter import Frame, StringVar, ttk
from tkinter import messagebox
from fastai.basic_train import load_learner
from fastai.vision.image import open_image
import numpy as np
from fastai import *
from fastai.vision import *
# from fastai.vision.all import *

import tkinter.filedialog
from openpyxl import Workbook
from datetime import datetime

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
        self.tree()
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
        ttk.Button(self, text= "Save & Send", command= self.add_data).place(
            relx=0.4,rely=0.27)
        ttk.Button(self, text= "Clear", command= self.clear).place(relx=0.5,rely=0.27)
        #***********
        ttk.Button(self, text= "Send", command= lambda : controller.show_frame(Predict)).place(relx=0.8,rely=0.9)
        

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

        # ***********************************
    def clear(self):
        self.id_text.set("")
        self.name_text.set("")
        self.address_text.set("")
        self.city_text.set("")
        self.gender_value.set("")
        self.age_value.set("")
        self.contact_text.set("")
        self.blood_value.set("")


    def add_data(self):
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
        tree_rows = len(self.tree.get_children())
        self.data = [tree_rows+1, self.id_text.get(), self.name_text.get(), self.gender_value.get(), self.age_value.get(),
        self.blood_value.get(), self.contact_text.get(), self.address_text.get(), self.city_text.get(), dt_string, ""]
        self.tree.insert('', tk.END, values=self.data)
        self.saveView()

    def saveView(self):
        import os.path
        from os import path
        from openpyxl import load_workbook
        if path.exists("data.xlsx"):
            wb = load_workbook('data.xlsx')
            work_sheet = wb.active # Get active sheet
            work_sheet.append(self.data)
            wb.save('data.xlsx')

        else:
            book = Workbook()
            sheet = book.active
            headIndex = 1
            for head in self.tree['column']:
                sheet.cell(row=1, column=headIndex).value = head
                headIndex += 1

            rowIndex = 2
            for row in self.tree.get_children():
                colIndex = 1
                for value in self.tree.item(row)['values']:
                    sheet.cell(row = rowIndex, column = colIndex).value = value
                    colIndex += 1
                rowIndex += 1

            
            book.save('data'+".xlsx")
            book.close()
        messagebox.showinfo(title = "Save",message = "File Save Successful")
        

    def tree(self):
        frame1 = Frame(self)
        frame1.pack()
        frame1.place(relheight=0.5, relwidth=0.9, relx = 0.05, rely =0.4)

        tk.Grid.rowconfigure(frame1, 0, weight=1)
        tk.Grid.columnconfigure(frame1, 0, weight=1)

        self.tree = ttk.Treeview(frame1,selectmode="extended", show="headings", height=2)
        self.tree.grid(column=0, row=0, sticky='news')
        ## Adds scrollbars
        wY = ttk.Scrollbar(frame1, orient="vertical", command=self.tree.yview)
        wY.grid(column=1, row=0, sticky='ns')
        wY.config(takefocus=0)

        wX = ttk.Scrollbar(frame1, orient="horizontal", command=self.tree.xview)
        wX.grid(column=0, row=1, sticky='we')
        wX.config(takefocus=0)

        self.tree.configure(xscrollcommand=wX.set, yscrollcommand=wY.set)
        
        #column_index = ["1","2","3", "4", "5", "6", "7", "8", "9", "10"]
        column = ['Patient ID', 'Name', 'Gender', 'Age', 'Blood Group', 'Contact', 'Address', 'City', 'Date Created', 'Result']
        self.tree["columns"] = ['#'] + column

        self.tree.heading('#', text='#')
        self.tree.column('#', minwidth=20, width=30, stretch=False)

        for i in column:
            self.tree.column(i, width=100, minwidth=50)
            self.tree.heading(i, text = i)
            

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