
class Safety:
	def __init__(self):
		self.active_pins = []
		
	def addActivePins(self, pins):
		for n in pins:
			pin_to_skip = 0
			for p in self.active_pins:
				if (p == n):
					pin_to_skip = 1
			if not pin_to_skip:
				self.active_pins += [n]
	
	def getActivePins(self):
		return self.active_pins

###############################################
##
##						DEBUG CODE
##
###############################################
#~ def testSafety():
		#~ pins = [1, 4, 8, 18, 20, 9]
		#~ toAdd = [7, 11, 4, 24, 88, 9]
		#~ safe = Safety();
		#~ print ("Init :" + repr(pins))
		#~ print ("Add :" + repr(toAdd))
		#~ safe.addActivePins(pins)
		#~ safe.addActivePins(toAdd)
		#~ print ("Got :" + repr(safe.getActivePins()))
		
#~ testSafety()