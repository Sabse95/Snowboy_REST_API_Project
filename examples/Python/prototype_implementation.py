import snowboythreaded
import snowboydecoder
import sys
import signal
import yaml
import time

stop_program = False

# open config file to read the data
with open("configuration.yml", 'r') as stream:
    cfg = yaml.load(stream)

interrupted = False
menu = 0
recognized = 0
echo = 0
room = []
device = []

#Lists for the speech models
myRooms = []
myDevices =[]
myFunctions = []

#Lists for Console output
myRoomEcho= []
myDeviceEcho = []
myFunctionEcho = []


# function for reading the room speechmodels
def roomlist_create():
    i = 0
    roomlist = []
    while i < len(cfg['configuration']): 
        roomlist.append((cfg['configuration'][i]['keywords'][0]['keyword']))
        i = i + 1
    return roomlist

# function for reading the device speechmodels
def devicelist_create(room):
    i = 0
    j = 0
    x = 0
    devicelist = []
    while x < len(cfg['configuration']):
        if (cfg['configuration'][x]['name'] == room):
            while j < len(cfg['configuration'][x]['keywords'][0]['actions']['sublevel']):
                i = 0
                while i < len(cfg['configuration'][x]['keywords'][0]['actions']['sublevel'][j]['keywords']): 
                    devicelist.append((cfg['configuration'][x]['keywords'][0]['actions']['sublevel'][j]['keywords'][i]['keyword']))
                    i = i + 1
                j = j + 1
        x = x + 1
    return devicelist

# function for reading the function speechmodels
def functionlist_create(room, device):
    i = 0
    x = 0
    y = 0
    functionlist = []
    while x < len(cfg['configuration']):
        if (cfg['configuration'][x]['name'] == room):
            while y < len(cfg['configuration'][x]['keywords'][0]['actions']['sublevel']):
                if (cfg['configuration'][x]['keywords'][0]['actions']['sublevel'][y]['name'] == device):
                    while i < len(cfg['configuration'][x]['keywords'][0]['actions']['sublevel'][y]['keywords'][0]['actions']['sublevel']): 
                        functionlist.append((cfg['configuration'][x]['keywords'][0]['actions']['sublevel'][y]['keywords'][0]['actions']['sublevel'][i]['keywords'][0]['keyword']))
                        i = i + 1
                y = y + 1
        x = x + 1
    return functionlist

# function for reading the room feedback for console output
def room_echo(room):
    i = 0
    echolist = []
    while i < len(cfg['configuration']): 
        if (cfg['configuration'][i]['name'] == room):
            echolist.append(cfg['configuration'][i]['keywords'][0]['actions']['echo'])
        i = i + 1
    return echolist

# function for reading the device feedback for console output
def device_echo(room, device):
    i = 0
    j = 0
    x = 0
    echolist = []
    while x < len(cfg['configuration']):
        if (cfg['configuration'][x]['name'] == room):
            while j < len(cfg['configuration'][x]['keywords'][0]['actions']['sublevel']):
                if (cfg['configuration'][x]['keywords'][0]['actions']['sublevel'][j]['name'] == device):
                    echolist.append((cfg['configuration'][x]['keywords'][0]['actions']['sublevel'][j]['keywords'][i]['actions']['echo']))
                j = j + 1
        x = x + 1
    return echolist

# function for reading the function feedback for console output
def function_echo(room, device, function):
    i = 0
    x = 0
    y = 0
    echolist = []
    while x < len(cfg['configuration']):
        if (cfg['configuration'][x]['name'] == room):
            while y < len(cfg['configuration'][x]['keywords'][0]['actions']['sublevel']):
                if (cfg['configuration'][x]['keywords'][0]['actions']['sublevel'][y]['name'] == device):
                    while i < len(cfg['configuration'][x]['keywords'][0]['actions']['sublevel'][y]['keywords'][0]['actions']['sublevel']):
                        if(cfg['configuration'][x]['keywords'][0]['actions']['sublevel'][y]['keywords'][0]['actions']['sublevel'][i]['name'] == function):
                            echolist.append((cfg['configuration'][x]['keywords'][0]['actions']['sublevel'][y]['keywords'][0]['actions']['sublevel'][i]['keywords'][0]['actions']['echo']))
                        i = i + 1
                y = y + 1
        x = x + 1
    return echolist

# function for searching a room name in the config file
def room_name_search(number):
	liste = cfg['configuration'][number]['name']
	return liste

# function for searching a device name in the config file    
def device_name_search(room, number):
    x = 0
    while x < len(cfg['configuration']):
        if (cfg['configuration'][x]['name'] == room):
            device = cfg['configuration'][x]['keywords'][0]['actions']['sublevel'][number]['name']
        x = x + 1
    return device
    
# function for searching a function name in the config file 
def function_name_search(room, device, number):
    x = 0
    y = 0
    while x < len(cfg['configuration']):
        if (cfg['configuration'][x]['name'] == room):
            while y < len(cfg['configuration'][x]['keywords'][0]['actions']['sublevel']):
                if (cfg['configuration'][x]['keywords'][0]['actions']['sublevel'][y]['name'] == device):
					function = cfg['configuration'][x]['keywords'][0]['actions']['sublevel'][y]['keywords'][0]['actions']['sublevel'][number]['name']
                y = y + 1
        x = x + 1
    return function

# function for printing a list
def list_print(list):
    i = 0
    while i < len(list): 
        print(list[i])
        i = i + 1

# Snowboy init functions
def signal_handler(signal, frame):
    global interrupted
    interrupted = True  

def interrupt_callback():
    global interrupted
    return interrupted

# callbackfunctions for the detected room, in this version at least 4 rooms could be recognized
def room_recognized_1():
		global recognized 
		global models2
		global myRoomEcho
		global myDevices
		global room
		zahl = 0
		room= room_name_search(zahl)
		myRoomEcho = room_echo(room)
		myDevices = devicelist_create(room)
		models2 = myDevices
		recognized = 1

def room_recognized_2():
		global recognized 
		global models2
		global myRoomEcho
		global myDevices
		global room
		zahl = 1
		room = room_name_search(zahl)
		myRoomEcho = room_echo(room)
		myDevices = devicelist_create(room)
		models2 = myDevices
		recognized = 1
		
def room_recognized_3():
		global recognized 
		global models2
		global myRoomEcho
		global myDevices
		global room
		zahl = 2
		room = room_name_search(zahl)
		myRoomEcho = room_echo(room)
		myDevices = devicelist_create(room)
		models2 = myDevices
		recognized = 1
		
def room_recognized_4():
		global recognized 
		global models2
		global myRoomEcho
		global myDevices
		global room
		zahl = 3
		room = room_name_search(zahl)
		myRoomEcho = room_echo(room)
		myDevices = devicelist_create(room)
		models2 = myDevices
		recognized = 1

# callbackfunctions for the detected devices, in this version at least 4 devices could be recognized
def device_recognized_1():
		global recognized 
		global models3
		global myDeviceEcho
		global myFunctions
		global room
		global device
		zahl = 0
		device = device_name_search(room,zahl)
		myDeviceEcho = device_echo(room,device)
		myFunctions = functionlist_create(room,device)
		models3 = myFunctions
		recognized = 1

def device_recognized_2():
		global recognized 
		global models3
		global myDeviceEcho
		global myFunctions
		global room
		global device
		zahl = 1
		device = device_name_search(room,zahl)
		myDeviceEcho = device_echo(room,device)
		myFunctions = functionlist_create(room,device)
		models3 = myFunctions
		recognized = 1

def device_recognized_3():
		global recognized 
		global models3
		global myDeviceEcho
		global myFunctions
		global room
		global device
		zahl = 2
		device = device_name_search(room,zahl)
		myDeviceEcho = device_echo(room,device)
		myFunctions = functionlist_create(room,device)
		models3 = myFunctions
		recognized = 1
		
def device_recognized_4():
		global recognized 
		global models3
		global myDeviceEcho
		global myFunctions
		global room
		global device
		zahl = 3
		device = device_name_search(room,zahl)
		myDeviceEcho = device_echo(room,device)
		myFunctions = functionlist_create(room,device)
		models3 = myFunctions
		recognized = 1

# callbackfunctions for the detected functions/actions, in this version at least 4 functions could be recognized
def action_recognized_1():
		global recognized
		global models
		global myFunctionEcho
		global myRooms
		global room
		global device
		zahl = 0
		function = function_name_search(room,device,zahl)
		myFunctionEcho = function_echo(room,device,function)
		myRooms = roomlist_create()
		models = myRooms
		recognized = 1

def action_recognized_2():
		global recognized
		global models
		global myFunctionEcho
		global myRooms
		global room
		global device
		zahl = 1
		function = function_name_search(room,device,zahl)
		myFunctionEcho = function_echo(room,device,function)
		myRooms = roomlist_create()
		models = myRooms
		recognized = 1
		
def action_recognized_3():
		global recognized
		global models
		global myFunctionEcho
		global myRooms
		global room
		global device
		zahl = 2
		function = function_name_search(room,device,zahl)
		myFunctionEcho = function_echo(room,device,function)
		myRooms = roomlist_create()
		models = myRooms
		recognized = 1
		
def action_recognized_4():
		global recognized
		global models
		global myFunctionEcho
		global myRooms
		global room
		global device
		zahl = 3
		function = function_name_search(room,device,zahl)
		myFunctionEcho = function_echo(room,device,function)
		myRooms = roomlist_create()
		models = myRooms
		recognized = 1
	


# Initialize the speech model list 
myRooms = roomlist_create()
models  = myRooms
models2 = []
models3 = []

#Initialize callback functions depending on the different room speech models
if len(models) == 1:
	callbacks = [room_recognized_1]
elif len(models) == 2:
	callbacks = [room_recognized_1, room_recognized_2]
elif len(models) == 3:
	callbacks = [room_recognized_1, room_recognized_2, room_recognized_3]
elif len(models) == 4:
	callbacks = [room_recognized_1, room_recognized_2, room_recognized_3, room_recognized_4]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)	
# Initialize ThreadedDetector object and start the detection thread
threaded_detector = snowboythreaded.ThreadedDetector(models, sensitivity=0.5)
threaded_detector.start()

print('Listening... Press Ctrl+C to exit')

# main loop
threaded_detector.start_recog(detected_callback= callbacks,sleep_time=0.03)

# Let audio initialization happen before requesting input
time.sleep(1)

print("Diese Raeume koennen ausgewaehlt werden:")
print(models)
# main task
try:
	while not stop_program:
		if menu == 0:
			time.sleep(1)
			if echo == 1:
				print(myFunctionEcho)
				echo = 0
				print("Listening to Rooms:")
				print("Diese Raeume koennen ausgewaehlt werden:")
				print(myRooms)
			if recognized == 1:
				#pause recognition and cahnge the models
				threaded_detector.pause_recog()
				threaded_detector.change_models(models2)
				#Initialize callback functions depending on the different device speech models
				if len(models2) == 1:
					callbacks = [device_recognized_1]
				elif len(models2) == 2:
					callbacks = [device_recognized_1, device_recognized_2]
				elif len(models2) == 3:
					callbacks = [device_recognized_1, device_recognized_2, device_recognized_3]
				elif len(models2) == 4:
					callbacks = [device_recognized_1, device_recognized_2, device_recognized_3, device_recognized_4]
				# start recognition again
				threaded_detector.start_recog(detected_callback= callbacks,sleep_time=0.03)
				recognized = 0
				menu = 1
				echo = 1
		elif menu == 1:
			time.sleep(1)
			if echo == 1:
				print(myRoomEcho)
				echo = 0
				print("Listening to devices")
				print("Diese Devices koennen ausgewaehlt werden:")
				print(myDevices)
			if recognized == 1:
				#pause recognition and cahnge the models
				threaded_detector.pause_recog()
				threaded_detector.change_models(models3)
				#Initialize callback functions depending on the different function speech models
				if len(models3) == 1:
					callbacks = [action_recognized_1]
				elif len(models3) == 2:
					callbacks = [action_recognized_1, action_recognized_2]
				elif len(models3) == 3:
					callbacks = [action_recognized_1, action_recognized_2, action_recognized_3]
				elif len(models3) == 4:
					callbacks = [action_recognized_1, action_recognized_2, action_recognized_3, action_recognized_4]
				# start recognition again
				threaded_detector.start_recog(detected_callback= callbacks,sleep_time=0.03)
				recognized = 0
				menu = 2
				echo = 1
		elif menu == 2:
			time.sleep(1)
			if echo == 1:
				print(myDeviceEcho)
				echo = 0
				print("Listening to actions")
				print("Diese Funktionen koennen ausgewaehlt werden:")
				print(myFunctions)
			if recognized == 1:
				#pause recognition and cahnge the models
				threaded_detector.pause_recog()
				threaded_detector.change_models(models)
				#Initialize callback functions depending on the different room speech models
				if len(models) == 1:
					callbacks = [room_recognized_1]
				elif len(models) == 2:
					callbacks = [room_recognized_1, room_recognized_2]
				elif len(models) == 3:
					callbacks = [room_recognized_1, room_recognized_2, room_recognized_3]
				elif len(models) == 4:
					callbacks = [room_recognized_1, room_recognized_2, room_recognized_3, room_recognized_4]
				# start recognition again
				threaded_detector.start_recog(detected_callback= callbacks,sleep_time=0.03)
				recognized = 0
				menu = 0
				echo = 1
except KeyboardInterrupt:
	print("Stop")
	
threaded_detector.terminate()

