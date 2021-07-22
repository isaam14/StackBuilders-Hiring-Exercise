
import random
from exercise import Plate
from exercise import PyPpredictor
from datetime import timedelta
from datetime import datetime


def testPicoyPlacaPredictor(plate, date, time):
	#Function to test the Pico y Placa Predictor
	#plate is type Plate
	#date is a String ('HH:MM')
	#time is a String ('dd/mm/YYYY')
	if PyPpredictor(plate, date, time):
		print("The vehicle with the plate {pn} can ".format(pn=plate.number)
			+ "be on the road at this date and time: {dt} {tm}".format(dt=date, tm=time))
	else:
		print("The vehicle with the plate {pn} should ".format(pn=plate.number)
			+ "not be on the road at this date and time! {dt} {tm}".format(dt=date, tm=time))


## RANDOM TEST

print("--------------RANDOM TEST----------------")

# Random date and time:
d1 = datetime.strptime('1/1/2017 0:00', '%d/%m/%Y %H:%M')
d2 = datetime.strptime('1/09/2019 0:00', '%d/%m/%Y %H:%M')
delta = d2 - d1
int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
random_sec = random.randrange(int_delta)
dateandtime = d1 + timedelta(seconds=random_sec)
strdateandtime = datetime.strftime(dateandtime,'%d/%m/%Y %H:%M')
print("The date and time for this test are {dt}".format(dt=strdateandtime))
print("(It's a {wd})".format(wd=datetime.strftime(dateandtime,'%A')))
[testdate,testtime] = strdateandtime.split(" ")

# Car plate:
Cplate=Plate('PBQ-014{randomnb}'.format(randomnb=str(random.randint(0,9))))
print('-----Ramdom test for cars:')
testPicoyPlacaPredictor(Cplate, testdate, testtime)

# Motorcycle pate:
Mplate=Plate('IB-22{randomnb}Z'.format(randomnb=str(random.randint(0,9))))
print('-----Ramdom test for Motorcycles:')
testPicoyPlacaPredictor(Mplate, testdate, testtime)



##INTERACTIVE TEST 

print("\n--------------INTERACTIVE TEST----------------")

print("""Please enter a plate number in the format 'AAA-dddd' 
      for cars or AA-dddA for motorcycles, where A is a 
      letter and d is a digit.""")
inputnbplate = input()
print("""Please enter a date in the format 'dd/mm/YYYY' """)
inputdate = input()
print("""Please enter a time in the format 'HH:MM' """)
inputtime = input()
inputplate = Plate(inputnbplate)
testPicoyPlacaPredictor(inputplate, inputdate, inputtime)