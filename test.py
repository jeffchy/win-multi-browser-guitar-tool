import webbrowser
import win32api
import os
from time import sleep
from selenium import webdriver

from tkinter import *
from tkinter import ttk
import Item
from ScheduleView import *

# browser = webdriver.Edge()
# browser = webdriver.Firefox()
# browser.get('http://www.baidu.com')

# put the driver in the dir of [dist]

# browser = webdriver.Chrome()
# #browser = webdriver.Firefox()
# browser.get('https://www.baidu.com/s?cl=3&tn=baidutop10&fr=top1000&wd=%E6%B0%91%E7%94%9F%E5%85%9A%E5%9C%A8%E5%8F%B0%E6%B9%BE%E6%88%90%E7%AB%8B&rsv_idx=2')
#
# js="var q=document.body.scrollTop = 0"
# browser.execute_script(js)
# sleep(3)
#
# js="var q=document.body.scrollTop = 100"
# browser.execute_script(js)


class MainView:
    def __init__(self,master):
        # form the main frame
        self.mainframe = ttk.Frame(master, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        # widgets
        self.info1 = ttk.Label(self.mainframe,text="Your Browser is:")
        self.info1.grid(column=0,row=0,padx=5)


        # choose the browser
        self.browsercontent = StringVar()

        self.browserchoose = ttk.Combobox(self.mainframe, textvariable=self.browsercontent)
        self.browserchoose.grid(pady=3, padx=3, column=1,row=0)

        self.browserchoose['values'] = ('Chrome', 'Edge', 'Firefox')
        self.browserchoose['state'] = 'readonly'
        self.browserchoose['width'] = '7'


        # widgets - scrollable listbox
        self.schelist = Listbox(self.mainframe,height=8)
        self.schelist.grid(column=0,row=1,columnspan=2,rowspan=2,sticky=(N,W,E,S),pady=5)

        self.scroll = ttk.Scrollbar(self.mainframe,orient=VERTICAL,command=self.schelist.yview)
        self.scroll.grid(column=2,row=1,rowspan=2,sticky=(N,S,W),pady=5)

        self.schelist['yscrollcommand'] = self.scroll.set

        # add addsche and delsche button
        self.addsche = ttk.Button(self.mainframe,text='Add',command=self.addNewSche)
        self.delsche = ttk.Button(self.mainframe, text='Del', command=self.delSche)
        self.addsche.grid(column=0,row=3,padx=3, pady=1)
        self.delsche.grid(column=1,row=3,padx=3, pady=1)


        # for child in mainframe.winfo_children():
        #     if type(child) == type(scroll):print("yes")
        #     else:child.grid_configure(padx=5, pady=5)  # add padding for each child

        self.info2 = ttk.Label(self.mainframe, text="Schedule Info")
        self.info2.grid(column=3, row=0, padx=5)

        self.scheinfo = Text(self.mainframe,width=15,height=6)
        self.scheinfo.grid(column=3, row=1, padx=5,pady=5,sticky=(N,E))
        self.scheinfo['state']="disabled"

        self.connecttext = StringVar()

        self.connectinfo = ttk.Label(self.mainframe,textvariable=self.connecttext)
        self.connectinfo.grid(column=3, row=2, padx=5, pady=5, sticky=(N, W))
        self.connecttext.set("Not connected...\nchoose or create\nyour schedule")

        self.gobrowser = ttk.Button(self.mainframe,text='GO',command=self.goBrowser)
        self.gobrowser.grid(column=3,row=3,padx=3,pady=1)

        # self.gobrowser.destroy()


    def addNewSche(self):
        self.connecttext.set('addnew')
        print("add new sche")
        # start another window
        scheduleView = Tk()
        temp = ScheduleView(scheduleView)
        scheduleView.mainloop()



    def delSche(self):
        self.connecttext.set('del')
        print("del sche")

    def goBrowser(self):
        print("gobrowser")











mainview = Tk()
app = MainView(mainview)
mainview.mainloop()







# class App:
#
#     def __init__(self,master):
#
#         frame = Frame(master,width=512,height=512) # create a frame under master
#         frame.pack()
#
#         # add top-menu
#         # helpMenu = Menu(master)
#         # helpMenu.add_command(label="Help",command=self.help)
#         # aboutMenu = Menu(master)
#         # aboutMenu.add_command(label="About", command=self.about)
#
#         # menubar = Menu(master)
#         # helpmenu = Menu(menubar,tearoff=0)
#         # helpmenu.add_cascade(label="Help", menu = helpmenu, command=self.help)
#         # aboutmenu = Menu(menubar, tearoff=0)
#         # aboutmenu.add_cascade(label="About", menu = helpmenu, command=self.about)
#
#         menubar = Menu(master)
#         menubar.add_command(label="Help", command=self.help)
#         menubar.add_command(label="About", command=self.about)
#
#         master.config(menu=menubar)
#         self.button = Button(
#             frame, text="QUIT",fg="red",command=frame.quit
#         ) # create buttons
#
#         self.button.pack(side=LEFT)
#         # pack it into
#
#         self.hi_there=Button(frame, text="Hello",command=self.say_hi)
#
#         self.hi_there.pack(side=LEFT)
#
#     def say_hi(self):
#         print("hello")
#
#     def about(self):
#         print("about")
#     def help(self):
#         print("help")


































