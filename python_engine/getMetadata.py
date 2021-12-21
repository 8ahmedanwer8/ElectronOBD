import obd
import obdHandler as obh
import json

connection = obd.OBD()
_,supportedCommandsNames, supportCommandsUnits, supportedCommandsDesc = obh.getSupported(connection)

output = [supportedCommandsNames, supportedCommandsDesc, supportCommandsUnits]

print(json.dumps(output))






