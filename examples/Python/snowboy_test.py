import snowboydecoder
import snowboythreaded
import sys
import signal
import yaml
import time

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

def recognized():
	print "erkannt"
#if len(sys.argv) == 1:
    #print("Error: need to specify model name")
    #print("Usage: python demo.py your.model")
    #sys.exit(-1)

def terminate():
	threaded_detector.pause_recog()

def main(arg1):
	
	models = arg1
	callbacks = [recognized]

	# capture SIGINT signal, e.g., Ctrl+C
	#signal.signal(signal.SIGINT, signal_handler)
	# Initialize ThreadedDetector object and start the detection thread
	threaded_detector = snowboythreaded.ThreadedDetector(models, sensitivity=0.5)
	threaded_detector.start()
	print('Listening... Press Ctrl+C to exit')
	# main loop
	#detector.start(detected_callback=snowboydecoder.play_audio_file,
				   #interrupt_check=interrupt_callback,
				   #sleep_time=0.03)
	threaded_detector.start_recog(detected_callback= callbacks, sleep_time=0.03)
	print "Listen"
	# Let audio initialization happen before requesting input
	time.sleep(1)

	threaded_detector.terminate()


if __name__ == "__main__":
	main(sys.argv[1])




