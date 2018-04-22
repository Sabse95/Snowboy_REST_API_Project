"""PyAudio Example: Play a WAVE file."""

import pyaudio
import wave
import sys


def main(arg1):
	CHUNK = 8192

	wf = wave.open("resources/"+arg1, 'rb')

	p = pyaudio.PyAudio()

	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
					channels=wf.getnchannels(),
					rate=wf.getframerate(),
					output=True)

	data = wf.readframes(CHUNK)

	while data != '':
		stream.write(data)
		data = wf.readframes(CHUNK)

	stream.stop_stream()
	stream.close()

	p.terminate()

if __name__ == "__main__":
    main(sys.argv[1])
