from Tkinter import *
from ucasts import ID12LA
import Tkinter as tk
import threading
import RPi.GPIO as GPIO
 
class App(threading.Thread):
       
    def __init__(self):
	threading.Thread.__init__(self)
	
	
	#Main Window
        self.start()
	self.root = tk.Tk()
	self.root.wm_title("Republic Poly Direction Kiosk")
        self.root.protocol("WM_DELETE_WINDOW", self.callback)

        #Variables
	self.RFID = StringVar()
	self.Clinic = PhotoImage()
	
	#LeftFrame for RP logo
	leftFrame = Frame(self.root, width=200, height =200)
	leftFrame.grid(row=0, column=0)
	Label(leftFrame, text = "Welcome to RP Direction Kiosk").grid(row=0, column=0,)
	imageRP = PhotoImage(file='RPlogo.gif')
	Label(leftFrame, image=imageRP).grid(row=1, column=0)
	Label(leftFrame, text = "Please Scan Tag").grid(row=2, column=0)
	Entry(leftFrame, textvariable = self.RFID, width=13).grid(row=3,column=0)
	
    	#RightFrame for Map/Route
	rightFrame = Frame(self.root, width=200, height =200)
	rightFrame.grid(row=0, column=1)
	Label(rightFrame, text = "test").grid(row=0, column=1)
	self.Clinic = PhotoImage(file='Clinic.gif')
	Label(self.root, image=self.Clinic).grid(row=0, column=1)
	
	
	self.root.mainloop()

    def callback(self):
        self.root.quit()

    def run(self):
        reader = ID12LA()
	def scan():
		while True:
			
			tag = reader.wait_for_scan()
			print ("Scanned %s") % (tag,)
			self.RFID.set(tag)
		
			if tag=="6F005C86AF":
				print("Clinic A")
				self.Clinic=PhotoImage(file='ClinicA.gif')
				Label(self.root, image=self.Clinic).grid(row=0, column=1)
				
			elif tag=="6F005CB7BC":
				print("Clinic B")
				self.Clinic=PhotoImage(file='ClinicB.gif')
				Label(self.root, image=self.Clinic).grid(row=0, column=1)
				
			else:
				print("error")
				self.Clinic=PhotoImage(file='RPlogo.gif')
				Label(self.root, image=self.Clinic).grid(row=0, column=1)
	scan()
app = App()

    

