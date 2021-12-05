
import obd
import json
import utils as o 
import pandas as pd 
from threading import Thread
import time

def getSupported(connection):
	fullCommandsList = o.getAllCommandNames()
	fullDescList = o.getAllDataDescription()
	supportedCommands = []
	supportedCommandsNames = []
	supportedCommandsUnits = []
	supportedCommandsDesc = []
	for i in range(len(obd.commands[1])):
		# print(fullCommandsList[i], ": ", connection.supports(obd.commands[1][i]))
		if connection.supports(obd.commands[1][i]):
			supportedCommandsNames.append(fullCommandsList[i])
			supportedCommands.append(obd.commands[1][i])
			supportedCommandsUnits.append(connection.query(obd.commands[1][i]).unit)
			supportedCommandsDesc.append(fullDescList[i])

	return supportedCommands,supportedCommandsNames, supportedCommandsUnits, supportedCommandsDesc

def getCurrentData(connection,supportedCommands):
	readings = []
	for i in range(len(supportedCommands)):
		response = connection.query(supportedCommands[i])
		try:
			# respond = response.value.magnitude
			# respond = respond(respond,3) #round those long decimal places
			readings.append(response.value.magnitude)
		except:
			readings.append(str(response.value))
	return readings


def addUnitsToCSVHeading(names,units): #function that creates nice headings with both sensor name and the unit
	output = []
	if (len(names) == len(units)):
		for i in names:
			output.append(names[i] + " " + "(" + units[i] + ")")
	return output

data = [] #the data exported as csv at the end
heading = []#headings for the csv, like the titles for each column

def main():#worker thread gets data for us while main thread keeps checking for input from main.js to break worker thread's loop
	time.sleep(3) #we need this because running scripts from the terminal blocks the serial ports (to my surprise) so we wait until it stops blocking which i believe is the instant after the first lines are executed in the terminal or something
	

	# obd.logger.setLevel(obd.logging.DEBUG) # enables all debug information
	
	connection = obd.OBD()
	supportedCommands,supportedCommandsNames, supportedCommandsUnits, _ = getSupported(connection)

	supportedCommandsNames.insert(0, "TIME")
	heading.append(supportedCommandsNames)

    '''
	connection = obd.OBD()
	supportedCommands,supportedCommandsNames, supportedCommandsUnits, _ = getSupported(connection)

	headingWithoutTimeColumn = addUnitsToCSVHeading(supportedCommandsNames, supportedCommandsUnits)
	headingWithoutTimeColumn.insert(0, "TIME")
	heading.append(headingWithoutTimeColumn)

	# heading.insert(0,"TIME") #adds time column

    '''
	
	while True:
		# time.sleep(1)
		output = getCurrentData(connection,supportedCommands) #output variable is the data collected in one iteration

		currentTime = time.ctime(time.time()) #get current time
		print(json.dumps(output)) #prints it to stdout and main.js receives it
		output.insert(0,currentTime) #adds rows with the current time	

		data.append(output) #append current data to total output data array for when csv export is called
		if flag != 0:
			break
	return

flag = 0
getDataThread = Thread(target = main)
getDataThread.daemon = True
getDataThread.start()

	
while True:
	inp = input()
	if (inp):
		o.csvExporter(heading, data)
		flag = 1


# r = connection.query(obd.commands.PIDS_B)
# print("r", type(r))
# print("r.value: ", type(r.value))
# print("r.value.magnitude", r.value.magnitude)