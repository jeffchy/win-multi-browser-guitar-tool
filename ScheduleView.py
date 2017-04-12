from tkinter import ttk
from Item import *
from tkinter import *

class ScheduleView:
    def __init__(self,master):
        self.scheframe = ttk.Frame(master, padding="3 3 12 12")
        self.scheframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.rowcounter = 0
        self.colcounter = 0
        self.createItems()
        self.createItems()
        self.createItems()
        self.createItems()
        self.createItems()
        self.createItems()
        self.createItems()
        self.createItems()
        self.createItems()
        self.createItems()
        self.createItems()
        self.createItems()

        self.preview = ttk.Button(self.scheframe, text='Preview', command=self.preview)
        self.preview.grid(column=2,row=12,padx=3, pady=1)

        self.savesche = ttk.Button(self.scheframe, text='Savesche', command=self.savesche)
        self.savesche.grid(column=4,row=12, padx=3, pady=1)

    def createItems(self):
        Item1 = Item(self.scheframe)

    def preview(self):
        pass

    def savesche(self):
        pass