import pickle
import os.path
from tkinter import * # Import tkinter
import tkinter.messagebox   

    
class Address:
    def __init__(self, name, PatientID, Clinic, ApptTime, RFID):
        self.name = name
        self.PatientID = PatientID
        self.Clinic = Clinic
        self.ApptTime = ApptTime
        self.RFID = RFID

class RFIDPatientDetails:
    def __init__(self):      
        window = Tk() # Create a window
        window.title("Patient Details") # Set title
             
        self.nameVar = StringVar()
        self.PatientIDVar = StringVar()
        self.ClinicVar = StringVar()
        self.ApptTimeVar = StringVar()
        self.RFIDVar = StringVar()
                             
        frame1 = Frame(window)
        frame1.pack()
        
       
        Label(frame1, text = "Name").grid(row = 1, 
            column = 1, sticky = N+S+E+W)
        Entry(frame1, textvariable = self.nameVar, 
            width = 30).grid(row = 1, column = 2)
        Label(frame1, text = "PatientID").grid(row = 2, 
            column = 1, sticky = N+S+E+W)
        Entry(frame1, textvariable = self.PatientIDVar, 
            width = 30).grid(row = 2, column = 2)
        Label(frame1, text = "Clinic", width = 5).grid(row = 1, 
            column = 3, sticky = N+S+E+W)
        Entry(frame1, textvariable = self.ClinicVar, 
            width = 30).grid(row = 2,
            column = 4)
        Label(frame1, text = "ApptTime").grid(row = 2, 
            column = 3, sticky = N+S+E+W)
        Entry(frame1, textvariable = self.ApptTimeVar, 
            width = 30).grid(row = 1, column = 4)
        Label(frame1, text = "RFID").grid(row = 3, 
            column = 3, sticky = N+S+E+W)
        Entry(frame1, textvariable = self.RFIDVar, 
            width = 30).grid(row = 3, column = 4)
        
        frame2 = Frame(window)
        frame2.pack()
        photo = PhotoImage(file= "MapAgora.gif")
        Label(frame2, image=photo).grid(row=3,column= 1, sticky=N+S+E+W)
        

        frame4 = Frame(window)
        frame4.pack()
        Button(frame4, text = "Add", 
            command = self.processAdd).grid(row = 1, column = 1)
        btFirst = Button(frame4, text = "First", 
            command = self.processFirst).grid(row = 1, column = 2)
        btNext = Button(frame4, text = "Next", 
            command = self.processNext).grid(row = 1, column = 3)
        btPrevious = Button(frame4, text = "Previous", command = 
            self.processPrevious).grid(row = 1, column = 4)  
        btLast = Button(frame4, text = "Scan", 
            command = self.processLast).grid(row = 1, column = 5)
		
          
        self.addressList = self.loadAddress()
        self.current = 0
      
        if len(self.addressList) > 0:
            self.setAddress()

        window.mainloop() # Create an event loop
        
    def saveAddress(self):
        outfile = open("PatientInfo.txt", "wb")
        pickle.dump(self.addressList, outfile)
        tkinter.messagebox.showinfo(
            "Address saved", "A new address is saved")
        outfile.close()
    
    def loadAddress(self):
        if not os.path.isfile("PatientInfo.txt"):
            return [] # Return an empty list

        try:
            infile = open("PatientInfo.txt", "rb")
            addressList = pickle.load(infile)
        except EOFError:
            addressList = []
            
        infile.close()
        return addressList
            
    def processAdd(self):
        address = Address(self.nameVar.get(), 
            self.PatientIDVar.get(), self.ClinicVar.get(), 
            self.ApptTimeVar.get(), self.RFIDVar.get())
        self.addressList.append(address)
        self.saveAddress()
        
    def processFirst(self):
        self.current = 0
        self.setAddress()
    
    def processNext(self):
        if self.current < len(self.addressList) - 1:
            self.current += 1
            self.setAddress()
    
    def processPrevious(self):
        pass # Left as exercise
    
    def processLast(self):
        if self.RFIDVar.get == 12345:
            self.RFIDVar.set('test')
    def setAddress(self):
        self.nameVar.set(self.addressList[self.current].name)
        self.PatientIDVar.set(self.addressList[self.current].PatientID)
        self.ClinicVar.set(self.addressList[self.current].Clinic)
        self.ApptTimeVar.set(self.addressList[self.current].ApptTime)
        self.RFIDVar.set(self.addressList[self.current].RFID)

RFIDPatientDetails() # Create GUI
