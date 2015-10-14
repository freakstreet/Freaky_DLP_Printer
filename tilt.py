import threading, time
#from RPIO import PWM
from configuration import Configuration

class Tilt():
	def __init__(self, servo):
		threading.Thread.__init__(self)
		self.pin_num = Configuration.pin_tilt_pulse
		self.servo = servo
		#self.servo.setServo(pin_num, 1000)  	# servo pulse width 1000ms=-90deg, 2000ms = +90deg
		self.idle = 1
		self.run()
		
	def tiltMe(self):
		self.idle = 0
		self.run()

	def run(self):
		while not self.idle:
			#~ print ("Start tilting")
			#self.servo.setServo(self.pin_num, 2000)
			time.sleep(0.5)	# wait half a second
			#self.servo.setServo(self.pin_num, 1000)
			#~ print ("Finished tilt sequence")
			self.idle = 1


	def stop(self):
		self.idle = 1
		
	def getUsedPins(self):
		return [Configuration.pin_tilt_pulse]
		
		
###############################################
##
##						DEBUG CODE
##
###############################################
#~ def testTilt():
	#~ tilt = Tilt('stub')
	#~ while (1):
		#~ tilt.tiltMe()
		#~ print("wait 3 sec loop")
		#~ time.sleep(3)
		
#~ testTilt()