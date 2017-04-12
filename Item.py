from tkinter import ttk
from tkinter import *
class Item:
    def __init__(self,master):
        # construct subframe for one row
        self.itemframe = ttk.Frame(master)
        self.itemframe.grid(columnspan=8)

        self.schebox = ttk.Combobox(self.itemframe)
        self.schebox.grid(column=0,row=0,pady=2,padx=3,sticky=(N, W))

        self.schebox['state'] = 'readonly'
        self.schebox['value'] = ('Jump to link','Scroll')
        self.schebox['width'] = '10'

        self.schebox.bind('<<ComboboxSelected>>', self.sche_selected)

    def sche_selected(self,*args):
        # find the ans of the schebox and create different widget
        a = self.schebox.current()
        print(a)
        if a == 0: self.createjump()
        else: self.createscroll()


    def createjump(self):
        # firstly distroy the remaining ones
        # print(self.subframe.children)
        # destroy if any
        try:
            self.subframe.destroy()
        except:pass
        # let's add another frame!
        self.subframe = ttk.Frame(self.itemframe)
        self.subframe.grid(columnspan=7,column=1,row=0,sticky=(N, W))

        self.label1 = ttk.Label(self.subframe,text="             url:")
        self.label1.grid(column=1, row=0, pady=2, padx=3,sticky=(N, W))

        # initialize the stringvars
        self.urltext = StringVar()
        self.timetext = StringVar()

        # this is the url entry space.
        self.url = ttk.Entry(self.subframe,textvariable=self.urltext)
        self.url.grid(column=2,row=0,pady=2,padx=3,sticky=(N, W))

        self.label1 = ttk.Label(self.subframe, text="      time:")
        self.label1.grid(column=3, row=0, pady=2, padx=3,sticky=(N, W))

        # m:s eg: 1:54 means 1 minutes and 54 seconds
        self.url = ttk.Entry(self.subframe,textvariable=self.timetext)
        self.url.grid(column=4, row=0, pady=2, padx=3,sticky=(N, W))

        print(self.subframe.children)
        pass

    def createscroll(self):
        # destroy if any
        try:
            self.subframe.destroy()
        except:pass

        self.subframe = ttk.Frame(self.itemframe)
        self.subframe.grid(columnspan=7, column=1, row=0,sticky=(N, W))

        self.label1 = ttk.Label(self.subframe,text="scrollspeed:")
        self.label1.grid(column=1, row=0, pady=2, padx=3,sticky=(N, W))

        self.speedtext = StringVar()
        self.duratext = StringVar()

        # -10~10 integer value
        self.speedfield = ttk.Entry(self.subframe, textvariable=self.speedtext)
        self.speedfield.grid(column=2, row=0, pady=2, padx=3,sticky=(N, W))


        self.label2 = ttk.Label(self.subframe, text="dualtime:")
        self.label2.grid(column=3, row=0, pady=2, padx=3,sticky=(N, W))

        # m:s eg: 1:54 means 1 minutes and 54 seconds
        self.duratime = ttk.Entry(self.subframe,textvariable=self.duratext)
        self.duratime.grid(column=4, row=0, pady=2, padx=3, sticky=(N, W))
