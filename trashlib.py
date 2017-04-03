import pyttsx
import datetime
import psutil

#
# Have to install pypiwin 32 on windows 
#


def presentation():
	"""
	in progress
	"""

	sentence_1 = "I am a vocal user interface, devlopped for the reduction dimmension project"
	engine = pyttsx.init()
	engine.say(sentence_1)
	engine.runAndWait()



def get_date():
	"""
	for fun
	"""
	now = datetime.datetime.now()
	year_months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
	sentence = "Year is "+str(now.year)+", were are the "+str(now.day)+" of "+year_months[now.month-1]+" and it is "+str(now.hour)+" and "+str(now.minute)+" minutes "+str(now.second)+"seconds"

	engine = pyttsx.init()
	engine.say(sentence)
	engine.runAndWait()


def check_process():
	"""
	Check process running
	
	TODO:
		-> look just for the interting process 
	"""

	engine = pyttsx.init()
	engine.say("I detect a few process running")
	process_id_list = psutil.pids()
	for pid in process_id_list:

		process = psutil.Process(pid)
		process_status = process.status()
		process_name = process.name()
		engine.say(str(process_name)+" is "+str(process_status))
		
	engine.runAndWait()


# TEST SPACE

#for x in range(1,11):
#	engine.say(str(x) + "rabbits")

#engine.say("Rebellion are build on hope and blood")
#engine.say("and rabbits")
#engine.runAndWait()

presentation()
get_date()
check_process()


