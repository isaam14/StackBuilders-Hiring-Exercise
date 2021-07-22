
from datetime import datetime

class Plate:
    def __init__(self, number):
    	#The plate number is a String composed of letters,
    	# a hyphen and digits
        self.number = number

    def is_car(self):
    	#This function determines whether the plate
    	# belongs to a car or to a motorcycle
    	return self.number[-1].isdigit()

    def get_last_digit(self):
    	#Returns the last digit of the plate
    	if self.is_car():
    		return self.number[-1]
    	else:
    		return self.number[-2]


def is_Pico_hours(time):
	#Determines whether the input time corresponds
	# to a Pico hour (between 7:00am - 9:30am or
	# 16:00pm - 19:30).
	#The time input is a String ('HH:MM').
	inttime=int(time.replace(':', ''))
	return (700<=inttime<=930) or (1600<=inttime<=1930)


def PyPpredictor(plate, date, time):
	#Determines whether the vehicle can be on the
	# road or not, according to the past rules of
	# Pico y Placa (from May 2018).
	#It doesn't take in count the national holidays.
	#plate is type Plate
	#date is a String ('HH:MM')
	#time is a String ('dd/mm/YYYY')
	lastdigit=plate.get_last_digit()
	weekday=datetime.strptime(date,'%d/%m/%Y').weekday()
	if is_Pico_hours(time) and weekday!=5 and weekday!=6:
		if (weekday==0 and lastdigit in ['1','2'] or 
			weekday==1 and lastdigit in ['3','4'] or 
			weekday==2 and lastdigit in ['5','6'] or 
			weekday==3 and lastdigit in ['7','8'] or 
			weekday==4 and lastdigit in ['9','0']):
			return False
		else:
			return True
	else:
		return True
