import obd
from obd import OBDStatus
from time import time, ctime
import utils as o 
import pandas as pd 


class obd_handler():
	# def __init__(self,connection):
	# 	self.connection = connection
	# 	if connection.status() == OBDStatus.NOT_CONNECTED:
	# 		print("Message: Not connected")
	# 	if connection.status() == OBDStatus.ELM_CONNECTED:
	# 		print("Message: ELM connected, successful comms with ELM327 Adapter")
	# 	if connection.status() == OBDStatus.OBD_CONNECTED:
	# 		print("Message: ELM connected, successful comms with ELM327 Adapter and connected to car. Ignition off.")
	# 	if connection.status() == OBDStatus.CAR_CONNECTED:
	# 		print("Message: Successful comms with ELM327 and ignition is on.")


	def getSupported(self, connection):
		fullCommandsList = o.getAllCommandNames()
		fullDescList = o.getAllDataDescription()
		supportedCommands = []
		supportedCommandsNames = []
		supportedCommandsUnits = []
		supportedCommandsDesc = []
		for i in range(len(obd.commands[1])):
			print(fullCommandsList[i], ": ", connection.supports(obd.commands[1][i]))
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

def main():
	connection = obd.OBD()
	# d=0	

	obj = obd_handler()
	supportedCommads, supportedCommands, supportCommandsUnits, desc = obj.getSupported(connection)

	# sensors = supportedCommands
	# sensors.insert(0,"TIME") #adds time column

	# total_array = []

	# while d <3:
	# 	darry = obj.getCurrentData(connection,supportedCommads)
	# 	currentTime = ctime(time())
	# 	print("\n")
	# 	print(darry)
	# 	print("\n")
	# 	darry.insert(0,currentTime) #adds time rows
	# 	total_array.append(darry)
	# 	d+=1

	# o.csvExporter(sensors,total_array)
if __name__ == "__main__":
	main()
main()
