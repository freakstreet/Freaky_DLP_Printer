import os, sys, time
from tilt import Tilt
from shutter import Shutter
from zStepper import ZStepper
from projector import Projector
from configuration import Configuration
from safety import Safety


from Tkinter import *
#from RPIO import PWM





def startMessage():
	print "Starting Freaky soft DLP printer"
	
def listAllScenarioFiles(scenarioPath):
	print "List files from path: " + repr(scenarioPath)
	files = os.listdir(scenarioPath)
	for file in sorted(files):
		print file
	

# zPos is in mm
def setZPos(zPos):
	zDelta = zPos-z_position
	print "We must move z to " + repr(zDelta) + "mm"
	stepperMove(abs(zDelta)*steps_mm, zDelta>0,  100)
	
def stepperMove(steps, dir, speed):
	print "stepperMove : send " + repr(steps) + "steps, at " + repr(speed) + " mm/s, in " + repr(dir) + " direction"
	
def main():
	startMessage()
	
	#servo = PWM.Servo()
	servo = "STUB"
	
	# Create objects
	projo = Projector()
	z_stepper = ZStepper()
	shutter = Shutter(servo)
	tilt = Tilt(servo)
	safety = Safety()
	safety.addActivePins(z_stepper.getUsedPins())
	safety.addActivePins(shutter.getUsedPins())
	safety.addActivePins(tilt.getUsedPins())
	
	# test projo function
	projo.switchOn()
	projo.switchOff()
	
	# test Z stepper
	z_stepper.setTargetPos(199800, 1000)
	z_stepper.run()
	
	# test shutter function
	shutter.close()
	shutter.open()
	shutter.close()
	
	#test tilt function
	tilt.tiltMe()
	
	# check output pins to desactivate for safety
	print "Safety pins watched :" + repr(safety.getActivePins())

	#listAllScenarioFiles("/home/lsa/Documents/DLP_Printer_soft_Freaky/gear.slice/")
	fenetre = Tk()
	label = Label(fenetre, text="Hello World")
	label.pack()
	#fenetre.mainloop()




main()
