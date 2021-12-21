import obd
import obdHandler as obh
import json
import utils as u
import pandas as pd 
from threading import Thread
import time

data = [] #the data exported as csv at the end
heading = []#headings for the csv, like the titles for each column

def main():#worker thread gets data for us while main thread keeps checking for input from main.js to break worker thread's loop
	time.sleep(3) #we need this because running scripts from the terminal blocks the serial ports (to my surprise) so we wait until it stops blocking which i believe is the instant after the first lines are executed in the terminal or something
	
	connection = obd.OBD()
	supportedCommands,supportedCommandsNames, supportedCommandsUnits, _ = obh.getSupported(connection)

	headingWithoutTimeColumn = obh.addUnitsToCSVHeading(supportedCommandsNames, supportedCommandsUnits)
	headingWithoutTimeColumn.insert(0, "TIME")
	heading.append(headingWithoutTimeColumn)

		
	while True:	
		# time.sleep(1)
		output = obh.getCurrentData(connection,supportedCommands) #output variable is the data collected in one iteration

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
		u.csvExporter(heading, data)
		flag = 1

