
class Configuration:
	## ------------ Z axis parameters ----------------

	#Steps by milimeter
	steps_mm = 416
	# Z pos value in micrometers
	z_init_pos = 50000
	
	## ------------ Stepper IO configuration --------------
	pin_stepper_dir = 16
	pin_stepper_step = 19
	pin_endstop_max = 4
	pin_endstop_min = 14
	
	## ------------ Shutter configuration -------------
	pin_shutter_pulse = 22
	
	##------------- Tilt configuration -----------------
	pin_tilt_pulse = 23

	##-------------Printing parameters--------------
	layer_height = 100					# layer height, in µm
	curing_time = 2					# curing time in seconds
	curing_time_first_layers = 3			# curing time for first layers
	curing_first_layers_count = 5			# layers nb to be considerated as first layers
	curing_time_intervall_layer_delay	= 1	# delay between layers, time for shifting and tilting
	tilt_active	= 1						# = 1 activated, =0 not activated
	z_shift	= 1						# =1 if shifting, =0 no shifting
	z_shift_distance = 5					# Z axis shifting length before next layer, in mm
	z_shift_speed = 50					# Z axis shifting speed, in mm/sec