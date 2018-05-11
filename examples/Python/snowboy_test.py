import snowboydecoder
import sys
import signal
import requests


# Demo code for listening to two hotwords at the same time
interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

def recognised():
	endpoint = "http://192.168.8.131:5000/api/led/on"
	response = requests.get(endpoint)
	if response.ok:
		print "Started Light"
	else:
		print "Request failed."
		print response.text

def main(arg1):
	
	models = arg1
	callbacks= [recognised]
	

	sensitivity = [0.5]*len(models)
	detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
	callbacks = [lambda: snowboydecoder.play_audio_file(snowboydecoder.DETECT_DING)]
	print('Listening... Press Ctrl+C to exit')
	# main loop
	# make sure you have the same numbers of callbacks and models
	detector.start(detected_callback=callbacks,
				   interrupt_check=interrupt_callback,
				   sleep_time=0.03)

	detector.terminate()

				

if __name__ == "__main__":
    # capture SIGINT signal, e.g., Ctrl+C
	#signal.signal(signal.SIGINT, signal_handler)
    main(sys.argv[1])





