import RPi.GPIO as GPIO
import ruamel.yaml
import sys
from copy import deepcopy



def insert(arg1, arg2, arg3, arg4):

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

	
	ruamel.yaml.round_trip_dump(config, open('config.yml', 'w'), 
							indent=ind, block_seq_indent=bsi)

def delete(arg1):
	x = 0
	file_name = 'config.yml'
	from ruamel.yaml.util import load_yaml_guess_indent

	config, ind, bsi = load_yaml_guess_indent(open(file_name))
	while x < len(config['action']):
		if (config['action']['name'] == arg1):
			del config['action']['name']
		x=x+1
	
	ruamel.yaml.round_trip_dump(config, open('config.yml', 'w'), 
							indent=ind, block_seq_indent=bsi)
	
	print "delete data"


if __name__ == "__main__":
    insert(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    delete(sys.argv[1])
    
