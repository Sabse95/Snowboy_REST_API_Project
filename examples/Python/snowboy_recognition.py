# Python Module for starting the Word recognition
import snowboydecoder
import sys
import signal
import configuration
import callback_service
import led_test
import RPi.GPIO as GPIO

interrupted = False
Listen=4


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


def main():
	models = 0
	callbacks = 0
	
	#read models from configfile
	models = configuration.read_hotwords()
	#read the callback functions from callback_services a maximum of 20 words is possible without changing the callback_service.py file
	callbacks = callback_service.anzahl_callbacks_waehlen()
	
	sensitivity = [0.5]*len(models)
	detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
	#turn on the LISTEN LED
	led_test.led(Listen, GPIO.HIGH)
	print('Listening... Press Ctrl+C to exit')

	# main loop
	#start the detection
	detector.start(detected_callback=callbacks,
				   interrupt_check=interrupt_callback,
				   sleep_time=0.03)

	detector.terminate()

if __name__ == "__main__":
	# capture SIGINT signal, e.g., Ctrl+C
	signal.signal(signal.SIGINT, signal_handler)
	main()
