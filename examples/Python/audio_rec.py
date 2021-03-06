#records the .wav files
import pyaudio
import wave
import sys
import RPi.GPIO as GPIO
Word1 = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Word1, GPIO.OUT , initial= GPIO.LOW)

def main(arg1):

	CHUNK = 8192
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	RECORD_SECONDS = 5
	WAVE_OUTPUT_FILENAME = "resources/"+arg1

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)

	print("* recording")
	GPIO.output(Word1 ,GPIO.HIGH)

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)

	print("* done recording")
	GPIO.output(Word1 ,GPIO.LOW)

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()
	
if __name__ == "__main__":
    main(sys.argv[1])
