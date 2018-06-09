import requests
import sys

#handles get and post requests if a word is detected

def get_request(arg1):
	URL = arg1
	r = requests.get(url = URL)
	print "GET Request sent"

def post_request(arg1, arg2):
	URL = arg1
	data = arg2
	if data != 'x':
		r = requests.post(url = URL, data = data)
	else:
		r = requests.post(url = URL)
	print "POST Request sent"

if __name__ == "__main__":
	get_request(sys.argv[1])
	post_request(sys.argv[1], sys.argv[2])
