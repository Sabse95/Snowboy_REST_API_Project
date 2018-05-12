from flask import Flask
from flask import jsonify
import RPi.GPIO as GPIO
import audio_rec
import audio_out
import training_service
import led_test
import config
#import snowboy_test

Word1=17
Word2=27
Word3=22
Listen=4
Wohnzimmer=23
Licht=24
Fernseher=25
L_on=6
F_on=5
F_lauter=26
F_leiser=16
Reserve=21

app = Flask(__name__)

@app.route('/api/led/on')
def led_on():
	led_test.main(GPIO.HIGH)
	return jsonify("LED ON")
	
@app.route('/api/led/off')
def led_off():
	led_test.main(GPIO.LOW)
	return jsonify("LED OFF")

@app.route('/api/function/fernseher/on')
def fernseher_on():
	led_test.led(F_on, GPIO.HIGH)
	return jsonify("Fernseher ON")
	
@app.route('/api/function/fernseher/off')
def fernseher_off():
	led_test.led(F_on, GPIO.LOW)
	led_test.led(F_lauter, GPIO.LOW)
	led_test.led(F_leiser, GPIO.LOW)
	return jsonify("Fernseher OFF")

@app.route('/api/function/fernseher/lauter')
def fernseher_lauter():
	led_test.led(F_lauter, GPIO.HIGH)
	led_test.led(F_leiser, GPIO.LOW)
	return jsonify("Fernseher Lauter")
	
@app.route('/api/function/fernseher/leiser')
def fernseher_leiser():
	led_test.led(F_leiser, GPIO.HIGH)
	led_test.led(F_lauter, GPIO.LOW)
	return jsonify("Fernseher Leiser")

@app.route('/api/function/licht/on')
def light_on():
	led_test.led(L_on, GPIO.HIGH)
	return jsonify("Licht ON")
	
@app.route('/api/function/licht/off')
def light_off():
	led_test.led(L_on, GPIO.LOW)
	return jsonify("Licht OFF")

@app.route('/api/get/config')
def config():

	return jsonify("Config")

@app.route('/api/record/voicesample/<commandName>')
def sample_record(commandName):
	audio_rec.main(commandName)
	return jsonify("Word ok")
	
@app.route('/api/play/voicesample/<sampleName>')
def sample_play(sampleName):
	audio_out.main(sampleName)
	return jsonify("Word play")

@app.route('/api/add/hotword/<sampleName1>/<sampleName2>/<sampleName3>/<hotwordName>/<path:actionTaken>')
def create_hotword_1(sampleName1,sampleName2,sampleName3,hotwordName, actionTaken):
	training_service.main(sampleName1,sampleName2,sampleName3,hotwordName)
	#config.insert1(hotwordName, actionTaken)
	return jsonify("Hotword create!")

#@app.route('/api/add/hotword/<sampleName1>/<sampleName2>/<sampleName3>/<hotwordName>/<path:actionTaken>/<httpmethode>')
#def create_hotword_2(sampleName1,sampleName2,sampleName3,hotwordName, actionTaken, httpmethode):
	#training_service.main(sampleName1,sampleName2,sampleName3,hotwordName)
	#bodyData = "NULL"
	#config.main(hotwordName, actionTaken, httpmethode, bodyData)
	#return jsonify("Hotword create!")
	
#@app.route('/api/add/hotword/<sampleName1>/<sampleName2>/<sampleName3>/<hotwordName>/<path:actionTaken>/<httpmethode>/<bodyData>')
#def create_hotword_3(sampleName1,sampleName2,sampleName3,hotwordName, actionTaken, httpmethode, bodyData):
	#training_service.main(sampleName1,sampleName2,sampleName3,hotwordName)
	#config.main(hotwordName, actionTaken, httpmethode, bodyData)
	#return jsonify("Hotword create!")

@app.route('/api/delete/hotword/<hotwordName>')
def config_delete(hotwordName):
	config.delete(hotwordName)
	return jsonify("Hotword deleted")	
	
@app.route('/api/detection/start')
def listen_start():
	#snowboy_test.main()
	return jsonify("Detection started")
	
@app.route('/api/detection/terminate')
def listen_terminate():
	
	return jsonify("Detection terminated")
	
if __name__ == "__main__":
	led_test.main(GPIO.LOW)
	app.run(debug=True,host="0.0.0.0")
	
