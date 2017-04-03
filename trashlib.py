import pyttsx
import datetime

#
# Have to install pypiwin 32 on windows 
#



def get_date():
	"""
	for fun
	"""
	now = datetime.datetime.now()
	year_months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
	sentence = "Year is "+str(now.year)+", were are the "+str(now.day)+" of "+year_months[now.month-1]+" and it is "+str(now.hour)+" and "+str(now.minute)+", "+str(now.second)+"seconds"

	engine = pyttsx.init()
	engine.say(sentence)
	engine.runAndWait()


# TEST SPACE
#engine = pyttsx.init()

#for x in range(1,11):
#	engine.say(str(x) + "rabbits")

#engine.say("Rebellion are build on hope and blood")
#engine.say("and rabbits")
#engine.runAndWait()

get_date()
