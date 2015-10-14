#import serial
#~ from serial import Serial
from configuration import Configuration
from tkinter import *

class Projector:
	def __init__(self):
		#self.port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)
		self.swtchOffDelay = 180
		self.timeOn = 0
		self.isOn = 0

	def switchOn(self):
		#self.port.write("\r\n{ProjectorON}"
		print ("Projector is ON")
		self.isOn = 1
		
	def switchOff(self):
		#self.port.write("\r\n{ProjectorOFF}"
		print ("Projector is OFF")
		self.isOn = 0
		
	def loadImage(self, path):
		print ("Loading image: " + repr(path))
		#~ image = Image.open(path)
		#~ image.show()


###############################################
##
##						DEBUG CODE
##
###############################################
#~ def testProjector():
	#~ projector = Projector()
	#~ path = '/home/lsa/Documents/DLP_Printer_soft_Freaky/gear.slice/gear0013.png'
	#~ projector.loadImage(path)
	
#~ testProjector()	
	




		
	
	