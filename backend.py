class SmartPlug:

    def __init__(self, consumptionRate):
        self.switchedOn = False
        self.consumptionRate = consumptionRate 

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getSwitchedOn(self):
        return self.switchedOn

    def setConsumptionRate(self, newRate):
        try:
            newRate = int(newRate)
            if 0 <= newRate <= 150:
                self.consumptionRate = newRate
            else:
                print("Invalid input.Please enter a number between 0 and 150.")
        except ValueError:
            print("Invalid input.Please enter an integer.")

    def getConsumptionRate(self):
        return f"The consumption rate is:{self.consumptionRate} watts"

    def __str__(self):
        return f"Smart Plug:{'On' if self.switchedOn else 'Off'}, Consumption Rate:{self.consumptionRate} watts"

class SmartDoorBell:

    def __init__(self):
        self.sleepMode = False
        self.switchedOn = False

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def setSleepMode(self, newMode):
        try:
            newRate = str(newMode)
            if newMode == True or newMode == False:
                self.sleepMode = newMode
            else:
                print("Invalid input. Please enter True or False.")
        except ValueError:
            print("Invalid input. Please enter True or False.")

       

    def getSleepMode(self):
        return self.sleepMode

    def getSwitchedOn(self):  
                return self.switchedOn

    def __str__(self):  
        return f"Smart Doorbell:  {'On' if self.switchedOn else 'Off'}, Sleep Mode: {'On' if self.sleepMode else 'Off'}"


class SmartHome():
    def __init__(self,consumptionRate=0):
        self.smartPlug = SmartPlug(consumptionRate)  
        self.smartDoorbell = SmartDoorBell()  
        self.devices = []

    def getDevices(self):
        return self.devices

    def getDevicesAt(self, index):
        return self.devices[index]

    def addDevice(self, device):
        self.devices.append(device)

    def removeDeviceAt(self, index):
        del self.devices[index]


    def toggleSwitch(self, index):  
        return self.devices[index].toggleSwitch()

    def turnAllOff(self):
        for device in self.devices:
            if device.getSwitchedOn(): # Check if the device is switched on
                device.toggleSwitch()

    def turnAllOn(self):
        for device in self.devices:
            if not device.getSwitchedOn():  # Check if the device is switched off
                device.toggleSwitch()


    def getNumDevices(self):
        return len(self.devices)

    def __str__(self):
        output = "SmartHome has :"
        for device in self.devices:
            output += f"\n{device} "
        return output

def testSmartPlug():
    plug = SmartPlug(45)
    plug.toggleSwitch()
    print(plug.getSwitchedOn())
    print(plug.getConsumptionRate())
    plug.setConsumptionRate(100)
    print(plug.getConsumptionRate())
    print(plug)
  
#testSmartPlug()

def testSmartDoorBell():
    bell = SmartDoorBell()
    bell.toggleSwitch()
    print(bell.getSwitchedOn())
    print("sleep mode is :",bell.getSleepMode())
    bell.setSleepMode(True)
    print("sleep mode is :",bell.getSleepMode())
    print(bell)

#testSmartDoorBell()


def testSmartHome():
    home = SmartHome()
    plug = SmartPlug(100)
    bell = SmartDoorBell()
    home.addDevice(plug)
    home.addDevice(bell)
    bell.setSleepMode(True)
    plug.setConsumptionRate(23)
    print(home)
    
    
testSmartHome()












