from flask import Flask
from flask import jsonify
import RPi.GPIO as GPIO
import audio_rec
import audio_out
import training_service
import led_test
import configuration
import subprocess as sp

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
execution_status = 0
extProc = 0

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
	configuration.insert1(hotwordName, actionTaken)
	return jsonify("Hotword create!")


@app.route('/api/add/hotword/<sampleName1>/<sampleName2>/<sampleName3>/<hotwordName>/<path:actionTaken>//<httpmethode>')
def create_hotword_2(sampleName1,sampleName2,sampleName3,hotwordName, actionTaken, httpmethode):
	training_service.main(sampleName1,sampleName2,sampleName3,hotwordName)
	configuration.insert2(hotwordName, actionTaken, httpmethode)
	return jsonify("Hotword create!")

	
@app.route('/api/add/hotword/<sampleName1>/<sampleName2>/<sampleName3>/<hotwordName>/<path:actionTaken>//<httpmethode>/<bodyData>')
def create_hotword_3(sampleName1,sampleName2,sampleName3,hotwordName, actionTaken, httpmethode, bodyData):
	training_service.main(sampleName1,sampleName2,sampleName3,hotwordName)
	configuration.insert3(hotwordName, actionTaken, httpmethode, bodyData)
	return jsonify("Hotword create!")


@app.route('/api/delete/config/hotword/<hotwordName>')
def config_delete(hotwordName):
	configuration.delete(hotwordName)
	return jsonify("Hotword deleted")	

	
@app.route('/api/detection/start')
def detection():
	#demo_threaded.main("resources/snowboy.umdl")
	global execution_status
	global extProc
	if execution_status == 0:
		extProc = sp.Popen(['python','snowboy_recognition.py', 'resources/snowboy.umdl']) # runs myPyScript.py 
		#status = sp.Popen.poll(extProc) # status should be 'None'
		execution_status = 1
		led_test.led(Listen, GPIO.HIGH)
		return jsonify("Detection started")
	else:
		return jsonify("Detection already started")


@app.route('/api/detection/terminate')
def listen_terminate():
	global execution_status
	global extProc
	if execution_status == 1:
		sp.Popen.terminate(extProc) # closes the process
		#status = sp.Popen.poll(extProc) # status should now be something other than 'None' ('1' in my testing)
		execution_status = 0
		led_test.led(Listen, GPIO.LOW)
		return jsonify("Detection terminated")
	else:
		return jsonify("No Detection to terminate")

	
if __name__ == "__main__":
	led_test.main(GPIO.LOW)
	app.run(debug=True,host="0.0.0.0")
	
