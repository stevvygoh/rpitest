from tkinter import *
from ucasts import ID12LA
import tkinter as tk
import threading


class App(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()
    
    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        text1 = Text(self.root, height=35, width=55)
        photo=PhotoImage(file="Capture.gif")
        text1.insert(END,'\n')
        text1.image_create(END, image=photo)

        text1.pack(side=LEFT)

        text2 = Text(self.root, height=20, width=50)
        scroll = Scrollbar(self.root, command=text2.yview)
        text2.configure(yscrollcommand=scroll.set)
        text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        text2.tag_configure('big', font=('Verdana', 20, 'bold'))
        text2.tag_configure('color', foreground='#476042', 
                                font=('Tempus Sans ITC', 12, 'bold'))
        text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
        text2.insert(END,'\nWilliam Shakespeare\n', 'big')
        quote = """test"""
        text2.insert(END, quote, 'color')
        text2.insert(END, 'follow-up\n', 'follow')
        text2.pack(side=LEFT)
        scroll.pack(side=RIGHT, fill=Y)

        self.root.mainloop()
    
    
app = App()

def numtest():
    reader = ID12LA()
    tag = reader.get_last_scan()
    print ("rest")

numtest()