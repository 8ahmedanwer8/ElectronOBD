import obd
import json
import utils as o 
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

def getCurrentData(self,connection,supportedCommands):
	readings = []
	for i in range(len(supportedCommands)):
		response = connection.query(supportedCommands[i])
		try:
			readings.append(response.value.magnitude)
		except:
			readings.append(str(response.value))
	return readings


def getCurrentData(connection,supportedCommands):
	readings = []
	for i in range(len(supportedCommands)):
		response = connection.query(supportedCommands[i])
		try:
			response_rounded = response.value.magnitude
			response_rounded = round(response_rounded,3) #round those long decimal places
			readings.append(response_rounded)
		except:
			readings.append(str(response.value))
	return readings


def addUnitsToCSVHeading(names,units): #function that creates nice headings with both sensor name and the unit
	output = []
	if (len(names) == len(units)):
		for i in range(len(names)):
			output.append(names[i] + " " + "(" + units[i] + ")")
	return output