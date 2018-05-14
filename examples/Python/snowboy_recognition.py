import snowboydecoder
import sys
import signal
import configuration
import callback_service

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


def main():
	models = 0
	callbacks = 0
	
	models = configuration.read_hotwords()
	callbacks = callback_service.anzahl_callbacks_waehlen()
	
	sensitivity = [0.5]*len(models)
	detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)

	print('Listening... Press Ctrl+C to exit')

	# main loop
	detector.start(detected_callback=callbacks,
				   interrupt_check=interrupt_callback,
				   sleep_time=0.03)

	detector.terminate()

if __name__ == "__main__":
	# capture SIGINT signal, e.g., Ctrl+C
	signal.signal(signal.SIGINT, signal_handler)
	main()
