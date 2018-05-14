import RPi.GPIO as GPIO
import ruamel.yaml
import sys
from copy import deepcopy

#configuration handles all operations off with the config.yml file

def insert1(arg1, arg2):
	file_name = 'config.yml'
	from ruamel.yaml.util import load_yaml_guess_indent
		
	config, ind, bsi = load_yaml_guess_indent(open(file_name))
	
	elem = deepcopy(config['action'][0])
	config['action'].append(elem)
	
	elem['name'] = arg1
	elem['actions'][0]['keyword']= "resources/"+arg1+".pmdl"
	elem['actions'][1]['endpoint']= arg2
	elem['actions'][2]['httpmethod']= "GET"
	elem['actions'][3]['bodyData']= "x"
	
	ruamel.yaml.round_trip_dump(config, open(file_name, 'w'), 
								indent=ind, block_seq_indent=bsi)

def delete(arg1):
	x = 0
	file_name = 'config.yml'
	from ruamel.yaml.util import load_yaml_guess_indent

	config, ind, bsi = load_yaml_guess_indent(open(file_name))
	while x < len(config['action']):
		if (config['action'][x]['name'] == arg1):
			del config['action'][x]
		x=x+1
	
	ruamel.yaml.round_trip_dump(config, open('config.yml', 'w'), 
							indent=ind, block_seq_indent=bsi)
	print "delete data"
	
def insert2(arg1, arg2, arg3):
	file_name = 'config.yml'
	from ruamel.yaml.util import load_yaml_guess_indent
		
	config, ind, bsi = load_yaml_guess_indent(open(file_name))
	
	elem = deepcopy(config['action'][0])
	config['action'].append(elem)
	
	elem['name'] = arg1
	elem['actions'][0]['keyword']= "resources/"+arg1+".pmdl"
	elem['actions'][1]['endpoint']= arg2
	elem['actions'][2]['httpmethod']= arg3
	elem['actions'][3]['bodyData']= "x"
	
	ruamel.yaml.round_trip_dump(config, open(file_name, 'w'), 
								indent=ind, block_seq_indent=bsi)

def insert3(arg1, arg2, arg3, arg4):
	file_name = 'config.yml'
	from ruamel.yaml.util import load_yaml_guess_indent
		
	config, ind, bsi = load_yaml_guess_indent(open(file_name))
	
	elem = deepcopy(config['action'][0])
	config['action'].append(elem)
	
	elem['name'] = arg1
	elem['actions'][0]['keyword']= "resources/"+arg1+".pmdl"
	elem['actions'][1]['endpoint']= arg2
	elem['actions'][2]['httpmethod']= arg3
	elem['actions'][3]['bodyData']= arg4
	
	ruamel.yaml.round_trip_dump(config, open(file_name, 'w'), 
								indent=ind, block_seq_indent=bsi)

def size_of_config():
	file_name = 'config.yml'
	from ruamel.yaml.util import load_yaml_guess_indent
	x = 0
	config, ind, bsi = load_yaml_guess_indent(open(file_name))
	x= len(config['action'])
	#print "Configuration size: ", x	
	return x


def read_hotwords():
	file_name = 'config.yml'
	from ruamel.yaml.util import load_yaml_guess_indent
	config, ind, bsi = load_yaml_guess_indent(open(file_name))
	i = 0
	hotwordlist = []
	while i < len(config['action']): 
		hotwordlist.append((config['action'][i]['actions'][0]['keyword']))
		i = i + 1
	return hotwordlist

	
def read_endpoint(arg1):
	file_name = 'config.yml'
	from ruamel.yaml.util import load_yaml_guess_indent
	config, ind, bsi = load_yaml_guess_indent(open(file_name))
	i = 0
	endpoint = 0
	while i < len(config['action']):
		if (config['action'][i]['name'] == arg1):
			endpoint = config['action'][i]['actions'][1]['endpoint']
		i = i + 1
	#print "endpoint:", endpoint
	return endpoint
	
		
def read_httpmethod(arg1):
	file_name = 'config.yml'
	from ruamel.yaml.util import load_yaml_guess_indent
	config, ind, bsi = load_yaml_guess_indent(open(file_name))
	i = 0
	httpmethod = 0
	while i < len(config['action']):
		if (config['action'][i]['name'] == arg1):
			httpmethod = config['action'][i]['actions'][2]['httpmethod']
		i = i + 1
	#print "httpmethod:", httpmethod
	return httpmethod
	
def read_bodyData(arg1):
	file_name = 'config.yml'
	from ruamel.yaml.util import load_yaml_guess_indent
	config, ind, bsi = load_yaml_guess_indent(open(file_name))
	i = 0
	bodyData = 0
	while i < len(config['action']):
		if (config['action'][i]['name'] == arg1):
			bodyData = config['action'][i]['actions'][3]['bodyData']
		i = i + 1
	#print "bodyData:", bodyData
	return bodyData

def name_search(arg1):
	file_name = 'config.yml'
	from ruamel.yaml.util import load_yaml_guess_indent
	config, ind, bsi = load_yaml_guess_indent(open(file_name))
	name = config['action'][arg1]['name']
	return name	

if __name__ == "__main__":
	insert1(sys.argv[1], sys.argv[2])
	delete(sys.arg[1])
	insert2(sys.argv[1], sys.argv[2], sys.argv[3])
	insert3(sys.argv[1],sys.argv[2], sys.argv[3], sys.argv[4])
	size_of_config()
	read_hotwords()
	read_endpoint(sys.argv[1])
	read_httpmethod(sys.argv[1])
	read_bodyData(sys.argv[1])
	name_search(sy.argv[1])
