from tkinter import LEFT, RIGHT, Button, Label, Tk, W

"""
- grid vs pack for better layout control
- never use both pack and grid inside the same window. App will hang indefinitely
- default orientation is widgets is centre vertically and center horizontally. 
-- This is changed with sticky=X
-- sticky=W+E ==> stretched to fill the whole cell horizontally
-- NE, SW ==> corners
- place() can be used to to specific absolute positioning and sizing - less preferred

"""
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        #self.label.pack()
        self.label.grid(columnspan=2, sticky=W)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        # self.greet_button.pack(side=LEFT)
        self.greet_button.grid(row=1)
        

        # master.quit is built in function
        self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.pack(side=RIGHT)
        self.close_button.grid(row=1, column=1)

    def greet(self):
        print("Greetings!")

root_window = Tk()
my_gui = MyFirstGUI(root_window)
root_window.mainloop()