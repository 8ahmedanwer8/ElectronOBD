import json
commandNames = []
commandNameDesc = []
commandNameUnits = []
for i in range(1,42):
	commandNames.append('FUEL_PRESSURE')
for i in range(1,42):
	commandNameDesc.append(f'Fuel Pressure {i}')
for i in range(1,42):
	commandNameUnits.append('kilopascal ' + str(i))
output = [commandNames, commandNameDesc, commandNameUnits]
print(json.dumps(output))