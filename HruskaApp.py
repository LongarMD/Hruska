import tkinter as tk

class Hruska(object):
    def __init__(self, master, **kwargs):
        self.master=master

root=tk.Tk()
root.overrideredirect(1)
app=Hruska(root)
root.mainloop()
