import sys
import configuration
import request_service

#callbackservice includes callback funktions for 20 hotwords

def callback_1():
	nummer = 0
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer

def callback_2():
	nummer = 1
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer
	
def callback_3():
	nummer = 2
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer
	
def callback_4():
	nummer = 3
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer
	
def callback_5():
	nummer = 4
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer
	
def callback_6():
	nummer = 5
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer
	
def callback_7():
	nummer = 6
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer
	
def callback_8():
	nummer = 7
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer
	
def callback_9():
	nummer = 8
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer
	
def callback_10():
	nummer = 9
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer
	
def callback_11():
	nummer = 10
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer
	
def callback_12():
	nummer = 11
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer

def callback_13():
	nummer = 12
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer

def callback_14():
	nummer = 13
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer
	
def callback_15():
	nummer = 14
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer
	
def callback_16():
	nummer = 15
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer
	
def callback_17():
	nummer = 16
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer
	
def callback_18():
	nummer = 17
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer
	
def callback_19():
	nummer = 18
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer
	
def callback_20():
	nummer = 19
	name = configuration.name_search(nummer)
	print "Hotword found: ", name
	methode = configuration.read_httpmethod(name)
	data = configuration.read_bodyData(name)
	url = configuration.read_endpoint(name)
	if methode == "GET":
		request_service.get_request(url)
	elif methode == "get":
		request_service.get_request(url)
	elif methode == "POST":
		request_service.post_request(url, data)
	elif methode == "post":
		request_service.post_request(url, data)
	#print "Callback", nummer

def anzahl_callbacks_waehlen():
	
	status= configuration.size_of_config()
	
	if status == 1:
		callbacks = [callback_1]
		return callbacks
	elif status == 2:
		callbacks = [callback_1, callback_2]
		return callbacks
	elif status == 3:
		callbacks = [callback_1, callback_2, callback_3]
		return callbacks
	elif status == 4:
		callbacks = [callback_1, callback_2, callback_3, callback_4]
		return callbacks
	elif status == 5:
		callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5]
		return callbacks
	elif status == 6:
		callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6]
		return callbacks
	elif status == 7:
		callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7]
		return callbacks
	elif status == 8:
		callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8]
		return callbacks
	elif status == 9:
		callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9]
		return callbacks
	elif status == 10:
		callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10]
		return callbacks
	elif status == 11:
		callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11]
		return callbacks
	elif status == 12:
		callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12]
		return callbacks
	elif status == 13:
		callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12, callback_13]
		return callbacks
	elif status == 14:
		callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12, callback_13, callback_14]
		return callbacks
	elif status == 15:
		callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12, callback_13, callback_14, callback_15]
		return callbacks
	elif status == 16:
		callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12, callback_13, callback_14, callback_15, callback_16]
		return callbacks
	elif status == 17:
		callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12, callback_13, callback_14, callback_15, callback_16, callback_17]
		return callbacks
	elif status == 18:
		callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12, callback_13, callback_14, callback_15, callback_16, callback_17, callback_18]
		return callbacks
	elif status == 19:
		callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12, callback_13, callback_14, callback_15, callback_16, callback_17, callback_18, callback_19]
		return callbacks
	elif status == 20:	
		callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12, callback_13, callback_14, callback_15, callback_16, callback_17, callback_18, callback_19, callback_20]
		return callbacks

if __name__ == "__main__":
	callback_1()
	callback_2()
	callback_3()
	callback_4()
	callback_5()
	callback_6()
	callback_7()
	callback_8()
	callback_9()
	callback_10()
	callback_11()
	callback_12()
	callback_13()
	callback_14()
	callback_15()
	callback_16()
	callback_17()
	callback_18()
	callback_19()
	callback_20()
	
