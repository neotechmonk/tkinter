from tkinter import LEFT, RIGHT, Button, Label, Tk

"""
- no window size definition 
- Buttons are packed vertically
- Root Window is an argument for each widget element 
- Setup of GUI elements is done in __init__()
- pack() deafult is vertically unless side is LEFT or RIGHT
"""
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack(side=LEFT)

        # master.quit is built in function
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(side=RIGHT)

    def greet(self):
        print("Greetings!")

root_window = Tk()
my_gui = MyFirstGUI(root_window)
root_window.mainloop()