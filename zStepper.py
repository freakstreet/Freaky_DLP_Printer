import os, sys, time, threading, math
from configuration import Configuration


class ZStepper():
	def __init__(self):
		self.z_position_um = Configuration.z_init_pos
		self.target_pos_um = self.z_position_um
		self.steps_per_mm = Configuration.steps_mm
		self.nb_steps = 0
		self.idle = 1
		self.thread = ''
		self.ident = 1
		#GPIO.setup(Configuration.pin_stepper_dir,GPIO.OUT)
		#GPIO.setup(Configuration.pin_stepper_step,GPIO.OUT)
		
		## Init endstops interruption
		#GPIO.setup(Configuration.pin_endstop_max, GPIO.IN)
		#GPIO.add_event_detect(Configuration.pin_endstop_max,GPIO.FALLING)
		#GPIO.add_event_callback(Configuration.pin_endstop_max,maxEndstopHit, 1)	# last parameter is debounce time
	
	def setTargetPosMm(self, target_pos_mm, speed):
		self.setTargetPosUm(target_pos_mm*1000, speed)

	def setTargetPosUm(self, target_pos_um, speed):
		self.target_pos_um = target_pos_um
		self.nb_steps = math.ceil(self.steps_per_mm * (target_pos_um-self.z_position_um)/1000)
		#~ print (repr(target_pos_um) + " micro meter")
		#~ print (repr(self.z_position_um))
		#~ print ("SetTargetPos, nv_steps defined: " + repr(self.nb_steps))
		self.thread = threading.Thread(target=self.run)
		self.idle = 0
		self.thread.start()
		return self.thread
		#self.run()

	def run(self):
		print("start move ["  + repr(self.ident) + "-"+repr(self.nb_steps) + "]")
		#~ print ("Zpos=" + repr(self.z_position_um) + " before move")
		#GPIO.output(Configuration.pin_stepper_dir,self.nb_steps > 0)		# set stepper direction 
		while (self.nb_steps != 0):
			## do one step with motor
			#~ print ("Remaining steps: " + repr(self.nb_steps))
			#GPIO.output(Configuration.pin_stepepr_step, 1)
			time.sleep(0.00001)
			#GPIO.output(Configuration.pin_stepepr_step, 0)
			time.sleep(0.00006)
			
			delta_um = 1000.0 / self.steps_per_mm
			if self.nb_steps > 0 :
				self.nb_steps = self.nb_steps-1
				self.z_position_um += delta_um
			else :
				self.nb_steps = self.nb_steps+1
				self.z_position_um -= delta_um
			#~ print ("Zpos=" + repr(self.z_position_um))
		#~ print ("Finished moving stepper, nb_steps: " + repr(self.nb_steps))
		self.idle = 1
		self.thread = ''
		print("end move [" + repr(self.ident)+"]")
		self.ident += 1
		
	def maxEndstopHit():
		self.nb_steps = 0
		self.idle = 1

	def isMoving(self):
		return (self.idle == 0)
		
	def getUsedPins(self):
		return [Configuration.pin_stepper_dir, Configuration.pin_stepper_step]
		
	def setZeroPosition():
		self.z_position = 0
		self.target_pos_mm = 0
		
	def getZPosUm(self):
		return self.z_position_um
		
	def getZPosMm(self):
		return self.z_position_um/1000
		
	def waitMoveEnded(self):
		while (self.idle == 0):
			time.sleep(0.1)
		
		
		
###############################################
##
##						DEBUG CODE
##
###############################################
#~ def testStepper():
	#~ z_stepper = ZStepper()
	#~ th1 = z_stepper.setTargetPosMm(199.8, 1000)

	#~ while (z_stepper.isMoving()):
		#~ time.sleep(0.1)
	#~ print("Final pos is: " + repr(z_stepper.getZPosMm()))

#~ testStepper()	
	
