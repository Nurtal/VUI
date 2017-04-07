import pyttsx
import datetime
import psutil
import os
import time

#
# Have to install pypiwin 32 on windows 
# Require linux poppler-utils to read pdf
# => Some ideas:
#	- read publication
#	- read emails
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


def read_file(file_name):
	"""
	-> read content of file 
	"""

	engine = pyttsx.init()
	input_file = open(file_name, "r")
	for line in input_file:
		line = line.split("\n")
		line = line[0]

		engine.say(line)
		
	input_file.close()
	engine.runAndWait()


def read_pdf(article):
	"""
	-> require linux poppler-utils
	"""

	# Convert pdf to Text
	os.system("pdftotext "+str(article)+" reading_stuff.txt")

	# Reformat text
	# -> one line = one sentence
	read_file = open("reading_stuff.txt", "r")
	text_in_string = ""
	for line in read_file:
		text_in_string += line
	read_file.close()

	text_in_paragraph = text_in_string.split("\n\n")
	text_in_string = ""
	
	engine = pyttsx.init()
	for paragraph in text_in_paragraph:
		paragraph = paragraph.replace("\n", " ")
		illegal_char = []
		authorized_char = [" ", ",", "(", ")", "\n", "-", "+", "."]
		for character in paragraph:
			if(not character.isalpha() and not character.isdigit() and character not in authorized_char):
				illegal_char.append(character)
		for character in illegal_char:
			paragraph = paragraph.replace(character, " ")
		engine.say(paragraph)
	engine.runAndWait()
	



# TEST SPACE

#for x in range(1,11):
#	engine.say(str(x) + "rabbits")

#engine.say("Rebellion are build on hope and blood")
#engine.say("and rabbits")
#engine.runAndWait()

#presentation()
#get_date()
#check_process()
#read_file("data.txt")


read_pdf("Boruta.pdf")

