from tkinter import *
from backend import *
def setUpHome():
    smartHome= SmartHome()
    count = 0

    while True:
        print("Available Devices: 1.Smart Plug 2.Smart Doorbell")
        choice = input("Enter the number of the device you want to add: ")
        if choice == "1":
            while True:
                consumptionRate = input("Enter the consumption of the Smart Plug between 0-150: ")
                try:
                    consumptionRate = int(consumptionRate)
                    if 0 <= consumptionRate <= 150:
                        smartPlug = SmartPlug(consumptionRate)
                        smartHome.addDevice(smartPlug)#smartHome
                        print(f"Smart Plug added with consumption rate: {consumptionRate}W")
                        break  
                    else:
                        print("Invalid input. Please enter a number between 0 and 100.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
                    
                    continue
        elif choice == "2":
            smartDoorBell = SmartDoorBell()
            smartHome.addDevice(smartDoorBell)
            print("Smart Doorbell added.")
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue
        count += 1
        if count == 5:
           break
    return smartHome

#setUpHome()
class SmartHomeSystem:

    def __init__(self,smartHome):
        self.smartHome = smartHome
        self.devices = []
        self.win = Tk()
        self.win.title("Smart Home System")
        self.win.geometry("750x650")        
        self.mainFrame = Frame(self.win, border=10, width=350, height=350)    
        self.mainFrame.configure(border=10, relief="sunken")
        self.mainFrame.grid(row=5, column=0, padx=10, pady=10)
        self.deviceWidgets = []
        self.device = StringVar()
        self.createWidgets()


    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        self.deleteAllWidgets()
        
        btnON = Button(self.mainFrame, text="Turn ON all", border=5, command=self.turnOnAll)
        btnON.configure( bg="#FFE5B4",
        fg="#013220", 
        border=5, relief="raised",
        padx=5, pady=5,
        width=20, height=1,
         font=("Arial", 10, "bold"))
        btnON.grid(row=0, column=0, padx=5, pady=5)

        btnOFF = Button(self.mainFrame, text="Turn OFF all", border=5, command=self.turnOffAll)
        btnOFF.configure(bg="#FFE5B4", 
        fg="red", border=5,
        relief="raised",
        padx=5, pady=5, width=20, height=1,
        font=("Arial", 10, "bold"))
        btnOFF.grid(row=0, column=1,sticky=E, padx=5, pady=5)

        
        setUpSM = Button(self.mainFrame, text="Add Device", border=5, command=self.addDeviceWin)
        setUpSM.configure(bg="#008080",
        fg="black",
        border=5, 
        relief="raised", 
        padx=5, pady=5, 
        width=15, height=1,
        font=("Arial", 10, "bold"))
        setUpSM.grid(row=100, column=0, padx=5, pady=5)


        extbtn = Button(self.mainFrame, text="Exit", border=5, command=self.exitWin)
        extbtn.configure(bg="#FFE5B4",
        fg="red", border=5, 
        relief="raised", 
        padx=5, pady=5, 
        width=15, height=1,
        font=("Arial", 10, "bold"))
        extbtn.grid(row=100, column=1, padx=5, pady=5)

        numDevices = self.smartHome.getNumDevices()
        for i in range(numDevices):
            device = self.smartHome.getDevicesAt(i)
            deviceLabel = Label(self.mainFrame, text=device)
            deviceLabel.configure( fg="black",  font=("Arial", 10, "bold"))
            deviceLabel.grid(row=i + 1, column=0,sticky=E ,padx=5, pady=5)
            self.deviceWidgets.append(deviceLabel)

            toggleDevice = Button(self.mainFrame, text="Toggle",
            command=lambda index=i: self.toggleDevice(index))
            toggleDevice.configure(bg="green",
            fg="white", border=5,
            relief="raised",
            width=10, height=1,)
            toggleDevice.grid(row=i + 1, column=1,padx=5, pady=5 ,sticky=E)
            self.deviceWidgets.append(toggleDevice)

            editDevice = Button(self.mainFrame, text="Edit", 
            command=lambda index=i: self.editDevice(index))
            editDevice.configure(bg="#2E5A88",
            fg="white", relief="raised",  
            width=5, height=1,border=5,
            font=("Arial", 10, "bold"))
            editDevice.grid(row=i + 1, column=2, padx=5, pady=5,sticky=E)
            self.deviceWidgets.append(editDevice)

            removeDevice = Button(self.mainFrame, text="Delete", 
            command=lambda index=i: self.removeDevice(index))
            removeDevice.configure(bg="red", 
             fg="white",border=5, 
             relief="raised",  
             width=10, height=1,
             font=("Arial", 10, "bold"))
            removeDevice.grid(row=i + 1, column=3, padx=5, pady=5,sticky=E)
            self.deviceWidgets.append(removeDevice)


    def exitWin(self):
        self.win.destroy()
        
    def editDevice(self, index):
        device = self.smartHome.getDevicesAt(index)
        editWin = Toplevel(self.win)
        editWin.title("Edit Device")
        editWin.geometry("450x250")
        editWin.configure(bg="#BDB7AB")
        self.editWin = editWin

        if isinstance(device, SmartPlug):
            self.editSmartPlug(editWin, device)
        else:
            self.editSmartDoorBell(editWin, device)

    def editSmartPlug(self, editWin, device):
        message = Label(editWin, text="Enter the new consumption rate(0-150) for the Smart Plug")
        message.grid(row=0, column=0, padx=10, pady=10)

        consumptionRate = Entry(editWin, textvariable=self.device)
        consumptionRate.grid(row=2, column=0, padx=10, pady=10)

        submit = Button(editWin, text="Submit",
        command=lambda: self.setNewConsumptionRate(device))
        submit.configure(bg="#008080",
        fg="black", border=5, relief="raised",
        padx=5, pady=5, width=10, height=1,
        font=("Arial", 10, "bold"))
        submit.grid(row=4, column=0, padx=5, pady=5)

        exitEbtn = Button(editWin, text="Exit", border=5, command=self.exitEdit)
        exitEbtn.configure(bg="#FFE5B4", 
         fg="red", 
         border=5,
         relief="raised",
         padx=5, pady=5, 
         width=10, height=1,
         font=("Arial", 10, "bold"))
        exitEbtn.grid(row=4, column=0,sticky=W, padx=5, pady=5)

    def exitEdit(self):
        self.editWin.destroy()

    def editSmartDoorBell(self, editWin, device):
        message = Label(editWin,text="Enter the new sleep mode for the Smart Doorbell (True/False)")
        message.configure(bg="#C7C6C1",
        fg="black",
        padx=5, pady=5, 
        font=("Arial", 10, "bold"))
        message.grid(row=0, column=0, padx=10, pady=10)

        sleepMode = Entry(editWin, textvariable=self.device)
        sleepMode.grid(row=2, column=0, padx=10, pady=10)

        submit = Button(editWin, text="Submit", command=lambda: self.setNewSleepMode(device))
        submit.configure(bg="#008080", 
        fg="black", 
        border=5, 
        relief="raised",
        padx=5, pady=5,
        width=10, height=1,
         font=("Arial", 10, "bold"))
        submit.grid(row=4, column=0,padx=5, pady=5)

        exitEbtn = Button(editWin, text="Exit", border=5, command=self.exitEdit)
        exitEbtn.configure(bg="#FFE5B4",         
         fg="red",
         border=5, 
         relief="raised", 
         padx=5, pady=5,
         width=10, height=1,
         font=("Arial", 10, "bold"))
        exitEbtn.grid(row=4, column=0,sticky=W, padx=5, pady=5)

    def setNewConsumptionRate(self, device):
        newRate = self.device.get()
        self.device.set("")
       
        try:
            newRate = int(newRate)
            if 0 <= newRate <= 150:
                device.setConsumptionRate(newRate)
                self.createWidgets()
                self.editWin.destroy()
            else:
                self.showRateErrorMessage("Invalid input. Please enter a number between 0 and 150.")
        except ValueError:
            self.showRateErrorMessage("Invalid input. Please enter a integer between 0 and 150.")

    def showRateErrorMessage(self, message):
        error = Label(self.editWin, text=message)
        error.configure(bg="white",
         fg="red",
         padx=5,
         pady=5, 
         font=("Arial", 11, "bold"))
        error.grid(row=3, column=0, padx=10, pady=10)

    def setNewSleepMode(self, device):
        newMode = self.device.get()
        self.device.set("")
        if newMode.lower() == 'true':
            device.setSleepMode(True)
            self.createWidgets()
            self.editWin.destroy()
        elif newMode.lower() == 'false':
            device.setSleepMode(False)
            self.createWidgets()
            self.editWin.destroy()
        else:
            self.showModeErrorMessage("Invalid input. Please enter 'True' or 'False'.")
    def showModeErrorMessage(self, message):
        error = Label(self.editWin, text=message)
        error.configure(bg="white",
         fg="red",
         padx=5,
         pady=5,
         font=("Arial", 11, "bold"))
        error.grid(row=3, column=0, padx=10, pady=10)

    def removeDevice(self, index):
        self.smartHome.removeDeviceAt(index)
        self.createWidgets()

    def deleteAllWidgets(self):
        for widget in self.deviceWidgets:
            widget.destroy()
        self.deviceWidgets = []

    def turnOnAll(self):
        self.smartHome.turnAllOn()
        self.createWidgets()

    def turnOffAll(self):
        self.smartHome.turnAllOff()
        self.createWidgets()

    def toggleDevice(self, index):
        self.smartHome.toggleSwitch(index)
        self.createWidgets()

   

    def addDeviceWin(self):
        newWin = Toplevel(self.win)
        newWin.title("Add Device")
        newWin.geometry("450x400")
        newWin.configure(bg="#BDB7AB")
        self.newWin = newWin

        message = Label(newWin, text="Select the device you want to add", )
        message.configure(bg="#C7C6C1", 
         fg="black",
         padx=5, 
         pady=5, 
         font=("Arial", 10, "bold"))
        message.grid(row=0, column=0, padx=5, pady=5)

        smartPlug = Button(newWin, text="Smart Plug", border=5, command=self.addSmartPlug)
        smartPlug.configure(bg="#008080",
         fg="white",
         border=5,
         relief="raised",
         padx=5, pady=5,
         width=10, height=1,
         font=("Arial", 10, "bold"))
        smartPlug.grid(row=1, column=0, padx=5, pady=5)

        exit = Button(newWin, text="Exit", border=5, command=self.exit)
        exit.configure(bg="#FFE5B4",
         fg="red", border=5,
         relief="raised",
         padx=5, pady=5,
         width=10, height=1,
         font=("Arial", 10, "bold"))
        exit.grid(row=6, column=0, padx=5, pady=5)

        smartDoorbell = Button(newWin, text="Smart Doorbell", command=self.smartDoorbell)
        smartDoorbell.configure(bg="#008080",
         fg="white", border=5,
         relief="raised", padx=5,
         pady=5, width=15, height=1,
         font=("Arial", 10, "bold"))
        smartDoorbell.grid(row=5, column=0, padx=5, pady=5)

    def exit(self):
        self.newWin.destroy()

    def addSmartPlug(self):
        message = Label(self.newWin,
         text="Enter the consumption rate(0-150) for the Smart Plug", )
        message.configure(bg="#C7C6C1", fg="black", 
         padx=5, pady=5, font=("Arial", 11, "bold"))
        message.grid(row=0, column=0, padx=10, pady=10)

        consumptionRate = Entry(self.newWin,width=20, textvariable=self.device)
        consumptionRate.grid(row=2, column=0, padx=5, pady=5)

        submit = Button(self.newWin, text="Submit", border=5, command=self.addConsumptionRate)
        submit.configure(bg="#008080", 
        fg="black",
        border=5, 
        relief="raised",
        padx=5, pady=5, 
        width=10, height=1,
        font=("Arial", 10, "bold"))
        submit.grid(row=4, column=0, padx=5, pady=5)

    def addConsumptionRate(self):
        consumptionRate = self.device.get()
        self.device.set("")
        try:
            consumptionRate = int(consumptionRate)
            if 0 <= consumptionRate <= 150:
                smartPlug = SmartPlug(consumptionRate)
                self.smartHome.addDevice(smartPlug)
                self.createWidgets()
                self.newWin.destroy()
            else:
                self.showErrorMessage("Invalid input. Please enter a number between 0 and 150.")
        except ValueError:
            self.showErrorMessage("Invalid input. Please enter a integer between 0 and 150.")

    def showErrorMessage(self, message):
        error = Label(self.newWin, text=message)
        error.configure(bg="white", fg="red", padx=5, pady=5, font=("Arial", 11, "bold"))
        error.grid(row=3, column=0, padx=10, pady=10)

    def smartDoorbell(self):
        smartDoorBell = SmartDoorBell()
        self.smartHome.addDevice(smartDoorBell)
        self.createWidgets()
        self.newWin.destroy()
    def addDevice(self, device):
        self.smartHome.addDevice(device)
        self.createWidgets()

   

def main():    
    
    smarthome = setUpHome()
    smarthomesystem = SmartHomeSystem(smarthome)  
    smarthomesystem.run()
     
   
    
main()

