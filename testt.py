""" Messing about with tkinter """
import tkinter as tk
from tkinter import Frame, PhotoImage, StringVar, ttk
from tkinter import messagebox
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

    
  

class First(tk.Frame):
    """ Main frame of program """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
       
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
        self.controller = controller
        # Add image file
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        image1 = Image.open("knee12_copy.png")
        if image1.size != (width, height):
            
            img1_width, img1_height = image1.size
            img1_width = int(img1_width / img1_height) * height
            #img1_height = int(img1_height / img1_width) * width

            image1 = image1.resize((img1_width, height), Image.ANTIALIAS)
        bg = ImageTk.PhotoImage(image1)
        # Show image using label
        bg_label = tk.Label(self, image = bg)
        bg_label.place(x=-1, y=0, relwidth=1, relheight=1)
        bg_label.image = bg

        #Create Frame
        self.first_frame = Frame(self, border= 5, relief= 'raised')
        self.first_frame.pack()
        self.first_frame.place(relheight=0.7, relwidth=0.45, relx = 0.5, rely =0.15)

        # Hospitall name
        ttk.Label(self.first_frame,font= ('Algerian', 25), text="Knee OA Classification").place(relx = 0.19, rely =0.07)

        #Add User Button        
        add_image = Image.open("handsomeAdd.png")
        img_width, img_height = add_image.size
        add_image = add_image.resize((230, 230*int(img_height/img_width)), Image.ANTIALIAS)
        add_user = ImageTk.PhotoImage(add_image)
        add_user_btn = tk.Button(self.first_frame,text="Add Patient", 
                            image = add_user, 
                            #command= lambda : controller.show_frame(Interface),
                            compound="top",
                            relief= "raised",
                            font=('Helvetica', 15, BOLD),
                            activeforeground='white',
                            activebackground='green',
                            )
        add_user_btn.place(relx=0.06, rely=0.2, relwidth=0.4, relheight=0.55)
        add_user_btn.image = add_user
        self.changeOnHover(add_user_btn, 'green', 'snow2')


        #Existing User Button        
        search_image = Image.open("search_user.jpg")
        img_width, img_height = search_image.size
        search_image = search_image.resize((230, 230), Image.ANTIALIAS)
        search_user = ImageTk.PhotoImage(search_image)
        search_user_btn = tk.Button(self.first_frame,text="Search Patient", 
                                image = search_user, 
                                #command= lambda : controller.show_frame(SearchUser), 
                                compound="top",
                                relief= "raised",
                                font=('Helvetica', 15, BOLD),
                                activeforeground='white',
                                activebackground='mediumblue',
                                )
        search_user_btn.place(relx=0.53, rely=0.2, relwidth=0.4, relheight=0.55)
        search_user_btn.image = search_user
        self.changeOnHover(search_user_btn, 'mediumblue', 'snow2')

        #Exit Button
        exit_image = Image.open("exit22.png")
        img_width, img_height = exit_image.size
        exit_image = exit_image.resize((120, 60), Image.ANTIALIAS)
        exit_frame = ImageTk.PhotoImage(exit_image)
        exit_btn = tk.Button(self.first_frame,
                                #image = exit_frame, 
                                border = 0, text='Exit',
                                #command= lambda : quit(), 
                                font=('Feorgia', 19, BOLD),
                                foreground='white',
                                background='black',
                                activeforeground='white',
                                activebackground='red4',
                                )
        exit_btn.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.075)
        exit_btn.image = exit_frame

    def changeOnHover(self, button, colorOnHover, colorOnLeave):
  
        # background on entering widget
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))

        # background on leaving widget
        button.bind("<Leave>", func=lambda e: button.config(
            background = colorOnLeave))

class Interface(tk.Frame):

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
        self.controller = controller
        # Hospitall name
        ttk.Label(self,font= ('Arial', 25), text="Knee OA Classification").place(relx = 0.3, rely =0.01)

        # ******* Buttons ADD and Send ***********
        ttk.Button(self, text= "Save & Send", command= self.add_data).place(
            relx=0.7,rely=0.27)
        ttk.Button(self, text= "Clear", command= self.clear).place(relx=0.8,rely=0.27)
        #***********
        

    def makeWidgets(self):
        self.id_text = StringVar()
        self.name_text = StringVar()
        self.address_text = StringVar()
        self.city_text = StringVar()
        self.gender_value = StringVar()
        self.age_value = StringVar()
        self.contact_text = StringVar()
        self.blood_value = StringVar()
        # self.description = StringVar()
        
        style = entryStyle = labelStyle = buttonStyle = ttk.Style()
        style.configure('.', font=('Helvetica', 12))
        entryStyle.configure('TEntry',foreground = 'green')
        labelStyle.configure('TLable', )
        buttonStyle.configure('TButton',background='#232323', foreground = 'black', borderwidth=1, focusthickness=3, focuscolor='green')
        buttonStyle.map('TButton', background=[('active','green')])

        # Patient Id
        ttk.Label(self, text="*Patient Id:").place(relx = 0.05, rely =0.1)
        ttk.Entry(self, font = ('Arial', 12), textvariable = self.id_text, style="TEntry").place(
            relx = 0.11, rely =0.1, width=200, height=25)

        # Name
        ttk.Label(self, text="*Full Name:").place(relx = 0.37, rely =0.1)
        ttk.Entry(self, font = ('Arial', 12), textvariable = self.name_text, style="TEntry").place(
            relx = 0.44, rely =0.1, width=250, height=25)

        # Gender
        ttk.Label(self, text="*Gender:").place(relx = 0.64, rely =0.1)
       
        # Gender Combobox
        self.gender = ttk.Combobox(self, textvariable=self.gender_value, 
                                state='readonly')
        self.gender['values'] = ('None', 'Male', 'Female')
        self.gender.current(0)
        self.gender.place(
             relx = 0.69, rely =0.1, width=100, height=25)

        # Age
        ttk.Label(self, text="*Age:").place(relx = 0.77, rely =0.1)
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

        # Description
        from tkinter.scrolledtext import ScrolledText
        ttk.Label(self, text="Description:").place(relx = 0.05, rely =0.25)
        self.description = ScrolledText(self, wrap=tk.WORD,
                                      width=40, height=4,
                                      font=("Times New Roman", 15))
        self.description.place(
            relx = 0.13, rely =0.25)
        # ttk.(self, font = ('Arial', 12), textvariable = self.description).place(
        #     relx = 0.1, rely =0.23, width=100, height=25)

        # ***********************************
        ttk.Button(self, text= "Search ID", command= self.auto_fill).place(relx=0.27,rely=0.1)    

    def auto_fill(self):
        book = load_workbook("stored-data.xlsx")
        active_book = book.active
        iterRows = iter(book.active)
        entered_id = self.id_text.get()
        for i, row in enumerate(iterRows, 1):
            if i != 1:
                rowData = [ cell.value for cell in row ]
                if entered_id == rowData[0]:
                    print(rowData[0])
                    self.id_text.set(rowData[0])
                    self.name_text.set(rowData[1])
                    self.gender_value.set(rowData[2])
                    self.age_value.set(rowData[3])
                    self.blood_value.set(rowData[4])
                    self.contact_text.set(rowData[5])
                    self.address_text.set(rowData[6])
                    self.city_text.set(rowData[7])
                    break
            if i == active_book.max_row:
                messagebox.showinfo(title = "Error",message = "Patient ID doesnot exists")

        book.close()


    def clear(self):
        self.id_text.set("")
        self.name_text.set("")
        self.address_text.set("")
        self.city_text.set("")
        self.gender_value.set("")
        self.age_value.set("")
        self.contact_text.set("")
        self.blood_value.set("")
        self.description.delete("1.0","end")

    def add_data(self):
        duplicate_id  = False
        if self.id_text.get() and self.name_text.get() and self.gender_value.get() and self.age_value.get():
            wb = load_workbook('data.xlsx')
            ws = wb.active 
            for i in range(2, ws.max_row + 1):
                for j in range(1,2):
                    if str(self.id_text.get()) == str(ws.cell(i,j).value):
                        duplicate_id = True
            wb.close()
            if duplicate_id == False:
                now = datetime.now()
                dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")

                self.data = [self.id_text.get(), self.name_text.get(), self.gender_value.get(), self.age_value.get(),
                self.blood_value.get(), self.contact_text.get(), self.address_text.get(), self.city_text.get(),
                self.description.get("1.0", 'end-1c') , "", "", dt_string]

                if path.exists("data.xlsx"):
                    wb = load_workbook('data.xlsx')
                    work_sheet = wb.active # Get active sheet
                    work_sheet.append(self.data)
                    wb.save('data.xlsx')

                
                res = messagebox.askquestion(title = "Save",message = "Data Saved. Do you want to send for Prediction?")
                if res == 'yes':
                    self.selected_id = self.id_text.get()
                    self.controller.show_frame(Predict)
            
            else:
                messagebox.showinfo(title = "Error",message = "Patient ID already exists")
        else:
            # self.clear()
            messagebox.showinfo(title = "Error",message = "Please Fill all required fields")

    

class SearchUser(tk.Frame):
    """ Main frame of program """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.tree()

        ttk.Button(self, text= "Send", command= lambda : self.goto_predict(controller)).place(relx=0.8,rely=0.9)

        #ttk.Button(self, text= "Send", command= lambda : controller.show_frame(Predict)).place(relx=0.8,rely=0.9)
        
        # ****** Delete record of treeview ********
        ttk.Button(self, text= "Delete", command= self.delete).place(relx=0.1,rely=0.9)
        #****** Search For Treeview***********

        self.search_text = StringVar()
        self.searchBy = StringVar()

        ttk.Label(self, text="Search By").place(relx = 0.65, rely =0.35)

        self.search_by = ttk.Combobox(self, textvariable=self.searchBy, 
                                state='readonly')
        self.search_by['values'] = ('Name', 'Address', 'City')
        self.search_by.current(0)
        self.search_by.place(
             relx = 0.72, rely =0.35, width=100, height=25)

        ttk.Entry(self, font = ('Arial', 12), textvariable = self.search_text).place(
            relx = 0.8, rely =0.35, width=150, height=25)
        self.search_text.trace("w",self.filterSearch)

    def filterSearch(self, *args):
        self.category = self.searchBy.get()
        j = 0
        for i in self.column:
            j = j + 1
            if self.category == i:
                break

        ItemsOnTreeview = self.tree.get_children()
        search = self.search_text.get()
        search = search.lower()
        for eachItem in ItemsOnTreeview:
            if search in self.tree.item(eachItem)['values'][j-1].lower():
                # print(search)
                #print(self.tree.item(eachItem)['values'][2])
                search_var = self.tree.item(eachItem)['values']
                self.tree.delete(eachItem)

                self.tree.insert("", 0, values=search_var)

    def tree(self):

        frame1 = Frame(self)
        frame1.pack()
        frame1.place(relheight=0.5, relwidth=0.9, relx = 0.05, rely =0.4)

        tk.Grid.rowconfigure(frame1, 0, weight=1)
        tk.Grid.columnconfigure(frame1, 0, weight=1)

        self.tree = ttk.Treeview(frame1,selectmode="browse", show="headings", height=2)
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
        
        self.column = ['Patient ID', 'Name', 'Gender', 'Age', 'Blood Group', 'Contact', 'Address', 'City', 'Description', 'Image', 'Result', 'Date Created']
        self.tree["columns"] = self.column

        for i in self.column:
            self.tree.column(i, width=80, minwidth=50)
            self.tree.heading(i, text = i)
        
        if path.exists("data.xlsx"):
            self.load_data()
        else:
            book = openpyxl.Workbook()
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


    def load_data(self):
        book = load_workbook("data.xlsx")
        iterRows = iter(book.active)
        for i, row in enumerate(iterRows, 1):
            if i != 1:
                rowData = [ cell.value for cell in row ]
                self.tree.insert('', "end", values=rowData)
        book.close()

    def add_data(self):
        duplicate_id  = False
        if self.id_text.get() and self.name_text.get() and self.gender_value.get() and self.age_value.get():
            wb = load_workbook('data.xlsx')
            ws = wb.active 
            for i in range(2, ws.max_row + 1):
                for j in range(1,2):
                    if str(self.id_text.get()) == str(ws.cell(i,j).value):
                        duplicate_id = True
            wb.close()
            if duplicate_id == False:
                now = datetime.now()
                dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
                self.tree_rows = len(self.tree.get_children())

                self.data = [self.id_text.get(), self.name_text.get(), self.gender_value.get(), self.age_value.get(),
                self.blood_value.get(), self.contact_text.get(), self.address_text.get(), self.city_text.get(),
                self.description.get("1.0", 'end-1c') , "", "", dt_string]

                self.tree.insert('', tk.END, values=self.data)
                self.clear()
                self.saveView()
            
            else:
                messagebox.showinfo(title = "Error",message = "Patient ID already exists")
        else:
            self.clear()
            messagebox.showinfo(title = "Error",message = "Please Fill all required fields")


    def saveView(self):
        
        if path.exists("data.xlsx"):
            wb = load_workbook('data.xlsx')
            work_sheet = wb.active # Get active sheet
            work_sheet.append(self.data)
            wb.save('data.xlsx')

        child_id = self.tree.get_children()[-1]
        self.tree.focus(child_id)
        self.tree.selection_set(child_id)
        res = messagebox.askquestion(title = "Save",message = "Data Saved. Do you want to send for Prediction?")
        if res == 'yes':
            self.goto_predict(self.controller)
        # else:
        #     messagebox.showwarning('error', 'Something went wrong!')

    def delete(self):
        self.selected_item = self.tree.selection()## get selected item

        for item in self.tree.selection():
            self.row_item = self.tree.item(item)
        self.selected_row = self.row_item['values']
        to_delete = self.selected_row[0]
        # print(to_delete)

        self.tree.delete(self.selected_item)

        wb = load_workbook('data.xlsx')
        ws = wb.active # Get active sheet

                # Find Cell Place in Data
        for i in range(2, ws.max_row + 1):
            for j in range(1,2):
                if str(to_delete) == str(ws.cell(i,j).value):
                    cell_place = (ws.cell(i,j))  


        delete_cell = cell_place.coordinate

        delete_cell = delete_cell.replace('A','')


        ws.delete_rows(int(delete_cell))
        wb.save('data.xlsx')
        messagebox.showinfo(title = "Success",message = "Data Delete Successful")

            
    def goto_predict(self, controller):
        try:
            for item in self.tree.selection():
                self.row_item = self.tree.item(item)
            self.selected_row = self.row_item['values']
            # print(self.selected_row)
            controller.show_frame(Predict)
        except:
            messagebox.showinfo(title = "Error",message = "Select any data first")

class Predict(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        self.controller = controller
        self.get_data = self.controller.get_page(Interface)
       
        style = ttk.Style()
        style.configure('W.TLabel', font=('Helvetica', 20))

        ttk.Label(self, text="Predictions", style = 'W.TLabel').place(relx = 0.5, rely =0.02)
        # File Explorer Button
        ttk.Button(self, text= "Open Image", command= self.fileOpen).place(relx = 0.26, rely = 0.12)

        # Predict Button
        ttk.Button(self, text= "Predict", 
        command= self.showResult).place(relx = 0.26, rely = 0.6)

    def tkraise(self):
        print(self.get_data.selected_id)
        self.col_name = self.get_data.column
        self.row_data = self.get_data.selected_row
        #print(self.row)
        #print(self.get_data.item_row)
        tk.Frame.tkraise(self)

        
        self.image_frame = Frame(self, border= 10, relief= RIDGE)
        self.image_frame.pack()
        self.image_frame.place(relheight=0.5, relwidth=0.5, relx = 0.4, rely =0.1)
        frame1 = Frame(self, border= 10, relief= RIDGE)
        frame1.pack()
        frame1.place(relheight=1, relwidth=0.25, relx = 0, rely =0)
        ttk.Label(self.image_frame, text = "Upload an Xray Image", foreground= 'grey', style= 'W.TLabel').place(
            relx = 0.2, rely =0.4)

        frame2 = Frame(self, border= 10, relief= RIDGE)
        frame2.pack()
        frame2.place(relheight=1, relwidth=1, relx = 0.25, rely =0.65)


        ttk.Label(self, text="Results", style = 'W.TLabel').place(relx = 0.6, rely =0.68)
        ttk.Label(self, text= "KL Grade : ").place(relx = 0.3, rely =0.75)
        ttk.Label(self, text= "Accuracy : ").place(relx = 0.3, rely =0.8)


        # Move to Previous Frame
        ttk.Button(frame1, text= "Back", command= lambda : self.controller.show_frame(Interface)).place(relx = 0, rely =0)
        

        ttk.Label(self, text="Details", style = 'W.TLabel').place(relx = 0.1, rely =0.1)
        m = 0
        row_pos = 0.18
        for each in self.col_name:
            ttk.Label(self, text=each +" :").place(relx = 0.05, rely = row_pos)
            
            ttk.Label(self, text=self.row_data[m]).place(relx = 0.13, rely = row_pos)

            row_pos = row_pos + 0.05
            m += 1
            if m == 8:
                break

        
        

    def fileOpen(self):
        FILE_name = tk.filedialog.askopenfilename(
            initialdir = ".",
            title      = "Open",
            filetypes  = (
                ("Photo files", "*.png"),
                ("All", "*.*")
            )
        )
        if FILE_name:
            self.fileName = FILE_name
            image1 = Image.open(self.fileName)
            test = ImageTk.PhotoImage(image1)
            label1 = tkinter.Label(image=test)
            label1.image = test
            ttk.Label(self.image_frame, image=test).place(relx = 0.2, rely =0.01)
            ttk.Label(self, text= self.fileName).place(relx = 0.26, rely =0.19)
    
    def showResult(self):
        if self.fileName == "":
            messagebox.showinfo(title = "Alert",message = "Please Open Any File First")
        else:
            img = open_image(self.fileName)
            # Load Model
            # self.x = load_learner('F:\\8thproject\\', 'final.pkl') 
            self.x = load_learner('E:\\8th sem project\\Project Final\\final-project\\','trainfinal_vgg_model_after_fit.pkl') 
            # self.fileName = ""
            
            predict = self.x.predict(img)

            max_value = max(predict[2],key=lambda x:float(x))
            #print("KL Grade : "+ str(predict[0]) + " with value " + str(max_value.item()*100))
            self.result = "KL Grade : "+ str(predict[0]) + " with value " + str(round(max_value.item()*100, 2))
            grade = str(predict[0])
            accuracy_percent = str(max_value.item()*100)
            ttk.Label(self, text= grade).place(relx = 0.38, rely =0.75)
            ttk.Label(self, text= accuracy_percent).place(relx = 0.38, rely =0.8)

            ttk.Button(self, text= "Save Result", command= self.save_result).place(relx = 0.38, rely = 0.85)
            ttk.Button(self, text= "Download Result", command= self.download).place(relx = 0.5, rely =0.85)

    def save_result(self):
        wb = load_workbook('data.xlsx')
        self.ws = wb.active # Get active sheet
        # print(self.get_data.item_row)
        # row_number = self.get_data.item_row
        # cell = "J"+ str(row_number + 1)
        #  
        row_id = self.row_data[0]


        wb = load_workbook('data.xlsx')
        ws = wb.active # Get active sheet

                # Find Cell Place in Data
        for i in range(2, ws.max_row + 1):
            for j in range(1,2):
                # print(ws.cell(i,j).value)
                if str(row_id) == str(ws.cell(i,j).value):
                    print(ws.cell(i,j).value)
                    cell_place = (ws.cell(i,j))  


        cell_id = cell_place.coordinate

        cell_id_result = cell_id.replace('A','K')
        cell_id_image = cell_id.replace('A','J')
        
        ws[cell_id_result] = self.result
        ws[cell_id_image] = self.fileName

        wb.save('data.xlsx')
        #****** Update Treeview*********
        ItemsOnTreeview = self.get_data.tree.get_children()

        for eachItem in ItemsOnTreeview:
                self.get_data.tree.delete(eachItem)
        # refresh data from xlsl file
        book = load_workbook("data.xlsx")
        iterRows = iter(book.active)
        for i, row in enumerate(iterRows, 1):
            if i != 1:
                rowData = [ cell.value for cell in row ]
                self.get_data.tree.insert('', "end", values=rowData)
        book.close()

        messagebox.showinfo(title = "Success",message = "Result Saved Successful")
    
    def download(self):
        self.save_result()
        report_generator.makePDF(self)


def main():
    
    root = Window()
    root.title('Knee OA')
    #root.configure(bg='green')
    
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d+0+0'% (width, height))
    root.state('zoomed')
    root.resizable(False,False)
    # root.iconbitmap('./assets/pythontutorial.ico')
    root.bind('<Key-Escape>', lambda event: quit())
    root.update()

    return root


if __name__ == '__main__':

    main().mainloop()
    
    