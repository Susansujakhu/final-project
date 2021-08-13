import tkinter as tk
from tkinter import Frame, ttk
#from tkinter import font
from tkinter.constants import DISABLED, RIDGE, X
from tkinter.font import BOLD
from PIL import Image, ImageTk
import interface
import search

class First(tk.Frame):
    """ Main frame of program """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
       
        self.controller = controller
        # Add image file

        menubar = tk.Menu(controller)
        mFile = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="File", menu=mFile)

        # mFile.add_command(label="Open", command=self.checkView)
        # mFile.add_command(label="Save", command=self.check_saveView)
        mFile.add_separator()
        mFile.add_command(label="Exit", command=lambda: quit())

        #mFile.add_separator()
        #mFile.add_command(label="Refresh", command=lambda: self.refresh())

        # Help Section
        mHelp = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Help", menu=mHelp)

        mHelp.add_command(label="About")
        controller.config(menu=menubar)

        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        image1 = Image.open("kneeColorfulLeft.png")
        if image1.size != (width, height):
            
            img1_width, img1_height = image1.size
            img1_width = int(img1_width / img1_height) * height

        image1 = image1.resize((width, height), Image.ANTIALIAS)
        bg = ImageTk.PhotoImage(image1)

        # Show image using label
        bg_label = tk.Label(self, image = bg)
        bg_label.place(x=-1, y=0, relwidth=1, relheight=1)
        bg_label.image = bg

        #Create Frame
        self.first_frame = Frame(self, border= 5, relief= 'raised')
        self.first_frame.pack()
        self.first_frame.place(relheight=0.7, relwidth=0.45, relx = 0.45, rely =0.15)

        # Hospitall name
        ttk.Label(self.first_frame,font= ('Algerian', 25, BOLD), text="Knee OA Classification").place(relx = 0.19, rely =0.06)

        #Add User Button        
        add_image = Image.open("handsomeAdd.png")
        img_width, img_height = add_image.size
        add_image = add_image.resize((230, 230*int(img_height/img_width)), Image.ANTIALIAS)
        add_user = ImageTk.PhotoImage(add_image)
        add_user_btn = tk.Button(self.first_frame,text="Add Patient", 
                                image = add_user, 
                                command= lambda : controller.show_frame(interface.Interface), 
                                compound="top",
                                relief= "raised",
                                font=('Helvetica', 15, BOLD),
                                activeforeground='white',
                                activebackground='green',
                                )
        add_user_btn.place(relx=0.06, rely=0.2, relwidth=0.4, relheight=0.55)
        add_user_btn.image = add_user
        self.changeOnHover(add_user_btn, 'green', 'snow2', 'white', 'black')


        #Existing User Button        
        search_image = Image.open("search_user.jpg")
        img_width, img_height = search_image.size
        search_image = search_image.resize((230, 230), Image.ANTIALIAS)
        search_user = ImageTk.PhotoImage(search_image)
        search_user_btn = tk.Button(self.first_frame,text="Search Patient", 
                                image = search_user, 
                                command= lambda : controller.show_frame(search.SearchUser), 
                                compound="top",
                                relief= "raised",
                                font=('Helvetica', 15, BOLD),
                                activeforeground='white',
                                activebackground='mediumblue',
                                )
        search_user_btn.place(relx=0.53, rely=0.2, relwidth=0.4, relheight=0.55)
        search_user_btn.image = search_user
        self.changeOnHover(search_user_btn, 'mediumblue', 'snow2', 'white', 'black')

        #Exit Button
        exit_btn = tk.Button(self.first_frame,
                                border = 0, text='Exit',
                                command= lambda : quit(), 
                                font=('Georgia', 19, BOLD),
                                foreground='white',
                                background='black',
                                activeforeground='white',
                                activebackground='red4'
                                )
        exit_btn.place(relx=0.4, rely=0.83, relwidth=0.2, relheight=0.075)
        self.changeOnHover(exit_btn, 'red4', 'black', 'white', 'white')

    def changeOnHover(self, button, colorOnHover, colorOnLeave, fgHover, fgLeave):
  
        # background on entering widget
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover, foreground = fgHover))

        # background on leaving widget
        button.bind("<Leave>", func=lambda e: button.config(
            background = colorOnLeave, foreground = fgLeave))

    '''def refresh(self):
        self.destroy()
        self.__init__()'''