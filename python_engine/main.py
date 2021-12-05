
# import obd 
# from obd import OBDStatus
import obd
import json
import random
import utils as o 
from threading import Thread
# from time import sleep, ctime
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
			readings.append(response.value.magnitude)
		except:
			readings.append(str(response.value))
	return readings


# def main():#worker thread gets data for us while main thread keeps checking for input from main.js to break worker thread's loop
# 	time.sleep(3) #we need this because running scripts from the terminal blocks the serial ports (to my surprise) so we wait until it stops blocking which i believe is the instant after the first lines are executed in the terminal or something
# 	connection = obd.OBD()
# 	supportedCommands,supportedCommandsNames, _, _ = getSupported(connection)
# 	sensors = supportedCommandsNames
# 	sensors.insert(0,"TIME") #adds time column
# 	data = [] #the data exported as csv at the end
# 	while True:
# 		output = getCurrentData(connection,supportedCommands) #output variable is the data collected in one iteration
# 		currentTime = time.ctime(time.time())
# 		print(json.dumps(output)) #prints it to stdout and main.js receives it
# 		data.insert(0,currentTime) #adds time rows		
# 		data.append(output)
# 		if flag != 0:
# 			o.csvExporter(sensors,data)			
# 			break
# 	return

def main():
    c = 0
    while True:
        output = []
        for _ in range(1,42):
            output.append(random.randint(1,10000000))
            # data.append(output)
        print(json.dumps(output))
        if c != 0:
            # csv_exporter(labels, data)
            break
    return
flag = 0
inputListener = Thread(target = main)
inputListener.daemon = True
inputListener.start()

while True:
    inp = input()
    if (inp):
        flag = 1






# r = connection.query(obd.commands.PIDS_B)
# print("r", type(r))
# print("r.value: ", type(r.value))
# print("r.value.magnitude", r.value.magnitude)