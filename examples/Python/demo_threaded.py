import snowboythreaded
import sys
import signal
import time

stop_program = False
menu = 0
erkannt = 0

# This a demo that shows running Snowboy in another thread


def signal_handler(signal, frame):
    global stop_program
    stop_program = True

def printfunktion():
	global erkannt
	erkannt = 1
	print("Hello World")
	

def printfunktion2():
	global erkannt 
	erkannt = 1
	print("Sabse")
	
def printfunktion3():
	global erkannt
	erkannt = 1
	print("Snowboy")

#~ if len(sys.argv) == 1:
    #~ print("Error: need to specify model name")
    #~ print("Usage: python demo4.py your.model")
    #~ sys.exit(-1)

#model = sys.argv[1]
model = ['resources/Wohnzimmer.pmdl']
models2 = ['resources/snowboy.umdl']
models3 = ['resources/Esszimmer.pmdl']

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)
callbacks = [printfunktion]
# Initialize ThreadedDetector object and start the detection thread
threaded_detector = snowboythreaded.ThreadedDetector(model, sensitivity=0.5)
threaded_detector.start()

print('Listening... Press Ctrl+C to exit')

# main loop
threaded_detector.start_recog(detected_callback= callbacks,sleep_time=0.03)

# Let audio initialization happen before requesting input
time.sleep(1)

# Do a simple task separate from the detection - addition of numbers
while not stop_program:
	if menu == 0:
		time.sleep(1)
		print("Listening to Rooms")
		if erkannt == 1:
			threaded_detector.pause_recog()
			threaded_detector.change_models(models2)
			callbacks = [printfunktion2]
			threaded_detector.start_recog(detected_callback= callbacks,sleep_time=0.03)
			erkannt = 0
			menu = 1
	elif menu == 1:
		time.sleep(1)
		print("Listening to devices")
		if erkannt == 1:
			threaded_detector.pause_recog()
			threaded_detector.change_models(models3)
			callbacks = [printfunktion3]
			threaded_detector.start_recog(detected_callback= callbacks,sleep_time=0.03)
			erkannt = 0
			menu = 2
	elif menu == 2:
		time.sleep(1)
		print("Listening to actions")
		if erkannt == 1:
			threaded_detector.pause_recog()
			threaded_detector.change_models(model)
			callbacks = [printfunktion]
			threaded_detector.start_recog(detected_callback= callbacks,sleep_time=0.03)
			erkannt = 0
			menu = 0
	


threaded_detector.terminate()
