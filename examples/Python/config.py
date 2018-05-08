import RPi.GPIO as GPIO
import ruamel.yaml
import sys
from copy import deepcopy



def main(arg1, arg2):

	file_name = 'config.yml'
	from ruamel.yaml.util import load_yaml_guess_indent

	config, ind, bsi = load_yaml_guess_indent(open(file_name))

	elem = deepcopy(config['action'][0])
	config['action'].append(elem)
	elem['name'] = arg1
	elem['actions'][0]['keyword']= "resources/"+arg1+".pmdl"
	elem['actions'][1]['endpoint']= arg2

	
	ruamel.yaml.round_trip_dump(config, open('config.yml', 'w'), 
							indent=ind, block_seq_indent=bsi)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
    
