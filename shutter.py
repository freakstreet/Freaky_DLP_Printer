#from RPIO import PWM
from configuration import Configuration
import time

class Shutter:
	def __init__(self, servo):
		self.pin_num = Configuration.pin_shutter_pulse
		self.servo = servo
		self.state = -1
		#self.servo.setServo(self.pin_num, 1000)  	# servo pulse width 1000ms=-90deg, 2000ms = +90deg
		
	def open(self):
		print ("Opening shutter")
		self.state = 1
		#self.servo.setServo(self.pin_num, 2000)
			
	def close(self):
		print ("Closing shutter")
		self.state = 0
		#self.servo.setServo(self.pin_num, 1000)
		
	def getUsedPins(self):
		return [Configuration.pin_shutter_pulse]
		
	def getState(self):
		return self.state


###############################################
##
##						DEBUG CODE
##
###############################################
#~ def testShutter():
	#~ servo = "STUB"
	#~ print ("Init Shutter object") 
	#~ shutter = Shutter(servo)
	#~ print ("Shutter state: " + repr(shutter.getState()) )
	#~ shutter.open()
	#~ time.sleep(1)
	#~ print ("Shutter state (opened): " + repr(shutter.getState()) )
	#~ shutter.close()
	#~ time.sleep(1)
	#~ print ("Shutter state (closed): " + repr(shutter.getState()) )

#~ testShutter()	