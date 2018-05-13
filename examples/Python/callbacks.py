import sys
import configuration
import request_service


def callback_1():
	
	print "Callback1"

def callback_2():
	print "Callback2"
	
def callback_3():
	print "Callback3"
	
def callback_4():
	print "Callback4"
	
def callback_5():
	print "Callback5"
	
def callback_6():
	print "Callback6"
	
def callback_7():
	print "Callback7"
	
def callback_8():
	print "Callback8"
	
def callback_9():
	print "Callback9"
	
def callback_10():
	print "Callback10"
	
def callback_11():
	print "Callback11"
	
def callback_12():
	print "Callback12"

def callback_13():
	print "Callback13"

def callback_14():
	print "Callback14"
	
def callback_15():
	print "Callback15"
	
def callback_16():
	print "Callback16"
	
def callback_17():
	print "Callback17"
	
def callback_18():
	print "Callback18"
	
def callback_19():
	print "Callback19"
	
def callback_20():
	print "Callback20"

def anzahl_callbacks_waehlen():
	
	status= configuration.size_of_config()
	
	if status == 1:
		return callbacks = [callback_1]
	elif status == 2:
		return callbacks = [callback_1, callback_2]
	elif status == 3:
		return callbacks = [callback_1, callback_2, callback_3]
	elif status == 4:
		return callbacks = [callback_1, callback_2, callback_3, callback_4]
	elif status == 5:
		return callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5]
	elif status == 6:
		return callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6]
	elif status == 7:
		return callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7]
	elif status == 8:
		return callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8]
	elif status == 9:
		return callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9]
	elif status == 10:
		return callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10]
	elif status == 11:
		return callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11]
	elif status == 12:
		return callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12]
	elif status == 13:
		return callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12, callback_13]
	elif status == 14:
		return callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12, callback_13, callback_14]
	elif status == 15:
		return callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12, callback_13, callback_14, callback_15]
	elif status == 16:
		return callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12, callback_13, callback_14, callback_15, callback_16]
	elif status == 17:
		return callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12, callback_13, callback_14, callback_15, callback_16, callback_17]
	elif status == 18:
		return callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12, callback_13, callback_14, callback_15, callback_16, callback_17, callback_18]
	elif status == 19:
		return callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12, callback_13, callback_14, callback_15, callback_16, callback_17, callback_18, callback_19]
	elif status == 20:	
		return callbacks = [callback_1, callback_2, callback_3, callback_4, callback_5, callback_6, callback_7, callback_8, callback_9, callback_10,
							callback_11, callback_12, callback_13, callback_14, callback_15, callback_16, callback_17, callback_18, callback_19, callback_20]

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
	
