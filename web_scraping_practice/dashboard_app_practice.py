from tkinter import *


class JoshsButtons:
    """A GUI that prints a message"""

    def __init__(self, master):

        # Menu Window with cascading submenus
        menu = Menu(master)
        master.config(menu=menu)

        subMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label='File', menu=subMenu)

        # Adding subMenu items
        subMenu.add_command(label="New Project...", command=self.doNothing)
        subMenu.add_command(label="New...", command=self.doNothing)
        subMenu.add_separator()  # Creates that line that categorizes your different submenu items
        subMenu.add_command(label="Exit", command=master.destroy)

        # Status Bar
        status = Label(master, text="Preparing to do nothing...", bd=1, relief=SUNKEN,
                       anchor=W)  # anchor=W -> west side anchor
        status.pack(side=BOTTOM, fill=X)

        # Adding Master Screen Buttons
        top_frame = Frame(master)
        top_frame.pack()

        self.printButton = Button(top_frame, text='Print Message', command=self.printMessage)
        self.printButton.pack()

        self.quitButton = Button(top_frame, text='Quit Program', command=master.destroy)
        self.quitButton.pack(side=RIGHT)



    def printMessage(self):
        print("HERE'S YOUR MESSAGE")

    def doNothing(self):
        print("I am a completely useless program.")


r = Tk()
r.geometry('400x400')
j = JoshsButtons(r)
r.mainloop()