#plays back audio

import pyaudio
import wave
import sys
import RPi.GPIO as GPIO
Reserve=21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Reserve, GPIO.OUT , initial= GPIO.LOW)


def main(arg1):
	CHUNK = 8192

	wf = wave.open("resources/"+arg1, 'rb')

	p = pyaudio.PyAudio()

	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
					channels=wf.getnchannels(),
					rate=wf.getframerate(),
					output=True)

	data = wf.readframes(CHUNK)
	GPIO.output(Reserve ,GPIO.HIGH)
	while data != '':
		stream.write(data)
		data = wf.readframes(CHUNK)

	GPIO.output(Reserve ,GPIO.LOW)
	stream.stop_stream()
	stream.close()

	p.terminate()

if __name__ == "__main__":
    main(sys.argv[1])
