

# import obd 
# from obd import OBDStatus
import obd
import json
# import obdHandler as obdh
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



connection = obd.OBD()
_,supportedCommandsNames, supportCommandsUnits, supportedCommandsDesc = getSupported(connection)

# supportedCommandsNames = supportedCommandsDesc
# supportCommandsUnits = supportedCommandsDesc
output = [supportedCommandsNames, supportedCommandsDesc, supportCommandsUnits]


print(json.dumps(output))






# r = connection.query(obd.commands.PIDS_B)
# print("r", type(r))
# print("r.value: ", type(r.value))
# print("r.value.magnitude", r.value.magnitude)