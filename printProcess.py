import time, os
from tilt import Tilt
from shutter import Shutter
from zStepper import ZStepper
from projector import Projector
from configuration import Configuration
from safety import Safety
from time import gmtime, strftime
from datetime import datetime

simulation = 1

class printProcess():
	def __init__(self):
		working_path = ''
		count_layers = 0
		self.servo = ""
		self.z_stepper = ""
		self.tilt = ""
		self.safety = ""
		self.projo = ""
		
	def printPrintingCinfig(self):
		print("PRINTING CONFIG :")
		print("Z init pos: " + repr(Configuration.z_init_pos/1000) + "mm")

		
	def initComponents(self):
		#~ servo = PWM.Servo()
		self.servo = "STUB"

		# Create objects
		self.projo = Projector()
		self.z_stepper = ZStepper()
		self.shutter = Shutter(self.servo)
		self.tilt = Tilt(self.servo)
		self.safety = Safety()
		self.safety.addActivePins(self.z_stepper.getUsedPins())
		self.safety.addActivePins(self.shutter.getUsedPins())
		self.safety.addActivePins(self.tilt.getUsedPins())
		
	def millis_interval(self, start, end):
		#~ """start and end are datetime instances"""
		diff = end - start
		return diff*1000
		
	def printTimeHMSMs(self):
		return "["+datetime.utcnow().strftime('%H:%M:%S.%f')[:-3]+"]"
		
	def printScenario(self, path):
		self.printPrintingCinfig()
		files = os.listdir(path)
		layer_actual = 1
		
		#~ initial configuration
		#~ shutter.close()	
		closedTime = time.time()
		#~ set to Z+ position Configuration.z_shift_distance
		print (self.printTimeHMSMs() + "     Lowering Z axis to " + repr(Configuration.z_shift_distance)+ "mm")
		self.z_stepper.setTargetPosUm(Configuration.z_shift_distance, Configuration.z_shift_speed)
		#~ load first picture
		
		#~ start operation for each layer
		print ("-----------------------------------------------------------------------------------------------")
		for file in sorted(files):
			#~ ---------------- LOADING IMAGE PHASE
			print (self.printTimeHMSMs() + "     Loading image: " + repr(file))
			#~ ---------------- LOWER Z AXIS + 1 LAYER HEIGHT
			self.z_stepper.waitMoveEnded()
			self.z_stepper.setTargetPosUm(layer_actual*Configuration.layer_height, Configuration.z_shift_speed)
			self.z_stepper.waitMoveEnded()
			print (self.printTimeHMSMs() + "     Z lowered at " + ("%.3f" %self.z_stepper.getZPosMm()) + "mm")
			
			
			while (self.millis_interval(closedTime, time.time()) < (Configuration.curing_time_intervall_layer_delay*1000)) :
				time.sleep(0.05)
			
			#~ ---------------- OPENING SHUTTER --> T0 CURING 
			#~ opening shutter
			#~ shutter.open()
			print (self.printTimeHMSMs() + "     Shutter opened, start curing layer #" + repr(layer_actual))
			
			#~ ---------------- CURING PHASE
			if layer_actual <= Configuration.curing_first_layers_count:
				print (self.printTimeHMSMs() + "     Wait " + repr( Configuration.curing_time_first_layers) + "s")
				time.sleep(Configuration.curing_time_first_layers)
			else:
				print (self.printTimeHMSMs() + "     Wait " + repr( Configuration.curing_time) + "s")
				time.sleep(Configuration.curing_time)
			
			#~ ---------------- CLOSING SHUTTER --> T CURING 
			#~ closing shutter
			#~ shutter.close()	
			closedTime = time.time()
			print (self.printTimeHMSMs() + "     Shutter closed")
			
			#~ ---------------- TILTING AND Z INCREMENT PHASE			
			print (self.printTimeHMSMs() + "     Start tilting")
			self.tilt.tiltMe()
			print (self.printTimeHMSMs() + "     Tilt done")
			
			#~ ---------------- RAISE Z AXIS
			raise_z = self.z_stepper.getZPosUm() + Configuration.z_shift_distance*1000
			self.z_stepper.setTargetPosUm(raise_z, Configuration.z_shift_speed)
			print (self.printTimeHMSMs() + "     Z raising at " +  ("%.3f" %(raise_z/1000)) + "mm")
									
			layer_actual += 1
			print ("-----------------------------------------------------------------------------------------------")
			
			
			
			
###############################################
##
##						DEBUG CODE
##
###############################################			
def startTest():
	path = "/home/lsa/Documents/DLP_Printer_soft_Freaky/extract/"
	proc = printProcess()
	proc.initComponents()
	proc.printScenario(path)
	
startTest()