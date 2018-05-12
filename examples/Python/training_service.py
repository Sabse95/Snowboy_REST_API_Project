import sys
import base64
import requests


def get_wave(fname):
    with open(fname) as infile:
        return base64.b64encode(infile.read())


def main(arg1, arg2, arg3, arg4):

	endpoint = "https://snowboy.kitt.ai/api/v1/train/"


	############# MODIFY THE FOLLOWING #############
	token = "68077f151b4f7da54af8516d4e034abf77b6591a"
	hotword_name = arg4
	language = "dt"
	age_group = "20_29"
	gender = "F"
	microphone = "usb microphone"
	############### END OF MODIFY ##################

	#if __name__ == "__main__":
		#try:
			#[_, wav1, wav2, wav3, out] = sys.argv
		#except ValueError:
			#print "Usage: wave_file1.wav wave_file2.wav wave_file3.wav out_model_name.pmdl"
			#sys.exit()

	data = {
		"name": hotword_name,
		"language": language,
		"age_group": age_group,
		"gender": gender,
		"microphone": microphone,
		"token": token,
		"voice_samples": [
			{"wave": get_wave("resources/"+arg1)},
			{"wave": get_wave("resources/"+arg2)},
			{"wave": get_wave("resources/"+arg3)}
		]
	}

	response = requests.post(endpoint, json=data)
	if response.ok:
		with open("resources/"+arg4+".pmdl", "w") as outfile:
			outfile.write(response.content)
		print "Saved model to '%s'." % arg4
	else:
		print "Request failed."
		print response.text

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
