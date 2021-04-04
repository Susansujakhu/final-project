import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import font
import tkinter.filedialog
from tkinter import messagebox
from datetime import datetime


class Window(tk.Frame):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent
        self.parent.config(menu=self.makeMenu())
        self.makeWidgets()

    def makeMenu(self):
        mMain  = tk.Menu(self.parent)

        # File Section
        mFile = tk.Menu(mMain, tearoff=False)
        mMain.add_cascade(label="File", menu=mFile)
        mFile.add_command(label="New", command=self.newUser)
        # mFile.add_command(label="Open", command=self.checkView)
        # mFile.add_command(label="Save", command=self.check_saveView)
        mFile.add_separator()
        mFile.add_command(label="Exit", command=lambda: quit())

        # Help Section
        mHelp = tk.Menu(mMain, tearoff=False)
        mMain.add_cascade(label="Help", menu=mHelp)

        mHelp.add_command(label="About")

        return mMain

    def newUser(self):
        return

    def makeWidgets(self):

        
        self.name_text = StringVar()
        self.address_text = StringVar()
        style = entryStyle = labelStyle = buttonStyle = ttk.Style()
        style.configure('.', font=('Helvetica', 12))
        entryStyle.configure('TEntry',foreground = 'green')
        labelStyle.configure('TLable', )
        buttonStyle.configure('TButton',background='#232323', foreground = 'black', borderwidth=1, focusthickness=3, focuscolor='green')
        buttonStyle.map('TButton', background=[('active','green')])

        # Name
        ttk.Label(self, text="Name:").place(relx = 0.1, rely =0.1)
        ttk.Entry(self, font = ('Arial', 12), textvariable = self.name_text, style="TEntry").place(relx = 0.15, rely =0.1, width=200, height=25)

        # Address
        ttk.Label(self, text="Address:").place(relx = 0.3, rely =0.1)
        ttk.Entry(self, font = ('Arial', 12), textvariable = self.address_text).place(relx = 0.35, rely =0.1, width=200, height=25)
        

        ttk.Button(self, text= "Send", command= self.send).place(relx=0.7,rely=0.9)
        ttk.Button(self, text= "Clear", command= self).place(relx=0.8,rely=0.9)


    def send(self):
        name_text = self.name_text.get()
        address_text = self.address_text.get()
        print(name_text)
        print(address_text)

def main():
    root = tk.Tk()
    root.title('xl2web')
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d+0+0'% (width, height))
    root.state('zoomed')
    gui = Window(root)
    gui.pack(fill="both", expand=True)
   
    root.bind('<Key-Escape>', lambda event: quit())
    root.update()

    return root


if __name__ == '__main__':
    main().mainloop()