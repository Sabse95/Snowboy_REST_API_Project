import RPi.GPIO as GPIO


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

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Word1, GPIO.OUT , initial= GPIO.LOW)
GPIO.setup(Word2, GPIO.OUT , initial= GPIO.LOW)
GPIO.setup(Word3, GPIO.OUT , initial= GPIO.LOW)
GPIO.setup(Listen, GPIO.OUT , initial= GPIO.LOW)
GPIO.setup(Wohnzimmer, GPIO.OUT , initial= GPIO.LOW)
GPIO.setup(Licht, GPIO.OUT , initial= GPIO.LOW)
GPIO.setup(Fernseher, GPIO.OUT , initial= GPIO.LOW)
GPIO.setup(L_on, GPIO.OUT , initial= GPIO.LOW)
GPIO.setup(F_on, GPIO.OUT , initial= GPIO.LOW)
GPIO.setup(F_lauter, GPIO.OUT , initial= GPIO.LOW)
GPIO.setup(F_leiser, GPIO.OUT , initial= GPIO.LOW)
GPIO.setup(Reserve, GPIO.OUT , initial= GPIO.LOW)


def main(arg1):
	
	GPIO.output(Word1 ,arg1)
	GPIO.output(Word2,arg1)
	GPIO.output(Word3, arg1)
	GPIO.output(Listen ,arg1)
	GPIO.output(Wohnzimmer,arg1)
	GPIO.output(Licht, arg1)
	GPIO.output(Fernseher ,arg1)
	GPIO.output(L_on,arg1)
	GPIO.output(F_on, arg1)
	GPIO.output(F_lauter ,arg1)
	GPIO.output(F_leiser,arg1)
	GPIO.output(Reserve, arg1)




if __name__ == "__main__":
    main(sys.argv[1])
