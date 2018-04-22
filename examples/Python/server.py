from flask import Flask
from flask import jsonify
import RPi.GPIO as GPIO
import audio_rec
import audio_out
import training_service

LED =24
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT , initial= GPIO.LOW)

app = Flask(__name__)

@app.route('/api/led/on')
def led_on():
	GPIO.output(LED, GPIO.HIGH)
	return jsonify(led= GPIO.input(LED))
	
@app.route('/api/led/off')
def led_off():
	GPIO.output(LED, GPIO.LOW)
	return jsonify(led= GPIO.input(LED))
	
@app.route('/api/led/toogle')
def led_toggle():
	GPIO.output(LED, not GPIO.input(LED))
	return jsonify(led= GPIO.input(LED))
	
@app.route('/api/add/voicesample/<commandName>')
def sample_record(commandName):
	audio_rec.main(commandName)
	return jsonify("Word ok")
	
@app.route('/api/play/voicesample/<sampleName>')
def sample_play(sampleName):
	audio_out.main(commandName)
	return jsonify("Word play")
	
@app.route('/api/add/hotword/<sampleName1>/<sampleName2>/<sampleName3>/<hotwordName>/<actionTaken>')
def create_hotword(sampleName1,sampleName2,sampleName3,hotwordName, actionTaken):
	training_service.main(sampleName1,sampleName2,sampleName3,hotwordName)
	return jsonify("Hotword create!")
	
if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0")
