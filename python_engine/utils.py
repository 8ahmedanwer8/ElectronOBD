'''
Functions that return a list of descriptions, command names 
and units for all 96 data queries/sensor readings possible in Mode 2. This is nice
for if you need to look something up real quick. The first three functions have 
triple-quoted strings from the pyOBD doc and then string split to the data that needs 
to be extracted. First functions should return lists of 96 items, of which many are not 
even sensor readings such as "Supported PIDs" or supported by my car such as "O2_S8_WR_CURRENT". 
Last function is to do a csv export and it uses os.py for exporting to user's desktop.
'''
import pandas as pd 
import os
import datetime
def getAllDataDescription():
	allPossibleDescriptionData = """b'0100': Supported PIDs [01-20]
b'0101': Status since DTCs cleared
b'0102': DTC that triggered the freeze frame
b'0103': Fuel System Status
b'0104': Calculated Engine Load
b'0105': Engine Coolant Temperature
b'0106': Short Term Fuel Trim - Bank 1
b'0107': Long Term Fuel Trim - Bank 1
b'0108': Short Term Fuel Trim - Bank 2
b'0109': Long Term Fuel Trim - Bank 2
b'010A': Fuel Pressure
b'010B': Intake Manifold Pressure
b'010C': Engine RPM
b'010D': Vehicle Speed
b'010E': Timing Advance
b'010F': Intake Air Temp
b'0110': Air Flow Rate (MAF)
b'0111': Throttle Position
b'0112': Secondary Air Status
b'0113': O2 Sensors Present
b'0114': O2: Bank 1 - Sensor 1 Voltage
b'0115': O2: Bank 1 - Sensor 2 Voltage
b'0116': O2: Bank 1 - Sensor 3 Voltage
b'0117': O2: Bank 1 - Sensor 4 Voltage
b'0118': O2: Bank 2 - Sensor 1 Voltage
b'0119': O2: Bank 2 - Sensor 2 Voltage
b'011A': O2: Bank 2 - Sensor 3 Voltage
b'011B': O2: Bank 2 - Sensor 4 Voltage
b'011C': OBD Standards Compliance
b'011D': O2 Sensors Present (alternate)
b'011E': Auxiliary input status (power take off)
b'011F': Engine Run Time
b'0120': Supported PIDs [21-40]
b'0121': Distance Traveled with MIL on
b'0122': Fuel Rail Pressure (relative to vacuum)
b'0123': Fuel Rail Pressure (direct inject)
b'0124': 02 Sensor 1 WR Lambda Voltage
b'0125': 02 Sensor 2 WR Lambda Voltage
b'0126': 02 Sensor 3 WR Lambda Voltage
b'0127': 02 Sensor 4 WR Lambda Voltage
b'0128': 02 Sensor 5 WR Lambda Voltage
b'0129': 02 Sensor 6 WR Lambda Voltage
b'012A': 02 Sensor 7 WR Lambda Voltage
b'012B': 02 Sensor 8 WR Lambda Voltage
b'012C': Commanded EGR
b'012D': EGR Error
b'012E': Commanded Evaporative Purge
b'012F': Fuel Level Input
b'0130': Number of warm-ups since codes cleared
b'0131': Distance traveled since codes cleared
b'0132': Evaporative system vapor pressure
b'0133': Barometric Pressure
b'0134': 02 Sensor 1 WR Lambda Current
b'0135': 02 Sensor 2 WR Lambda Current
b'0136': 02 Sensor 3 WR Lambda Current
b'0137': 02 Sensor 4 WR Lambda Current
b'0138': 02 Sensor 5 WR Lambda Current
b'0139': 02 Sensor 6 WR Lambda Current
b'013A': 02 Sensor 7 WR Lambda Current
b'013B': 02 Sensor 8 WR Lambda Current
b'013C': Catalyst Temperature: Bank 1 - Sensor 1
b'013D': Catalyst Temperature: Bank 2 - Sensor 1
b'013E': Catalyst Temperature: Bank 1 - Sensor 2
b'013F': Catalyst Temperature: Bank 2 - Sensor 2
b'0140': Supported PIDs [41-60]
b'0141': Monitor status this drive cycle
b'0142': Control module voltage
b'0143': Absolute load value
b'0144': Commanded equivalence ratio
b'0145': Relative throttle position
b'0146': Ambient air temperature
b'0147': Absolute throttle position B
b'0148': Absolute throttle position C
b'0149': Accelerator pedal position D
b'014A': Accelerator pedal position E
b'014B': Accelerator pedal position F
b'014C': Commanded throttle actuator
b'014D': Time run with MIL on
b'014E': Time since trouble codes cleared
b'014F': Various Max values
b'0150': Maximum value for mass air flow sensor
b'0151': Fuel Type
b'0152': Ethanol Fuel Percent
b'0153': Absolute Evap system Vapor Pressure
b'0154': Evap system vapor pressure
b'0155': Short term secondary O2 trim - Bank 1
b'0156': Long term secondary O2 trim - Bank 1
b'0157': Short term secondary O2 trim - Bank 2
b'0158': Long term secondary O2 trim - Bank 2
b'0159': Fuel rail pressure (absolute)
b'015A': Relative accelerator pedal position
b'015B': Hybrid battery pack remaining life
b'015C': Engine oil temperature
b'015D': Fuel injection timing
b'015E': Engine fuel rate
b'015F': Designed emission requirements"""
	tempSplit = allPossibleDescriptionData.split("\n")
	descriptionsList= []
	for i in range(len(tempSplit)):
		b = tempSplit[i].split(": ")
		descriptionsList.append(b[1])
	return descriptionsList



def getAllCommandNames():
	allPossibleDataCommands = '''PIDS_A 
STATUS 
FREEZE_DTC 
FUEL_STATUS 
ENGINE_LOAD 
COOLANT_TEMP 
SHORT_FUEL_TRIM_1 
LONG_FUEL_TRIM_1 
SHORT_FUEL_TRIM_2 
LONG_FUEL_TRIM_2 
FUEL_PRESSURE 
INTAKE_PRESSURE 
RPM 
SPEED 
TIMING_ADVANCE 
INTAKE_TEMP 
MAF 
THROTTLE_POS 
AIR_STATUS 
O2_SENSORS 
O2_B1S1 
O2_B1S2 
O2_B1S3 
O2_B1S4 
O2_B2S1 
O2_B2S2 
O2_B2S3 
O2_B2S4 
OBD_COMPLIANCE 
O2_SENSORS_ALT 
AUX_INPUT_STATUS 
RUN_TIME 
PIDS_B 
DISTANCE_W_MIL 
FUEL_RAIL_PRESSURE_VAC 
FUEL_RAIL_PRESSURE_DIRECT 
O2_S1_WR_VOLTAGE 
O2_S2_WR_VOLTAGE 
O2_S3_WR_VOLTAGE 
O2_S4_WR_VOLTAGE 
O2_S5_WR_VOLTAGE 
O2_S6_WR_VOLTAGE 
O2_S7_WR_VOLTAGE 
O2_S8_WR_VOLTAGE 
COMMANDED_EGR 
EGR_ERROR 
EVAPORATIVE_PURGE 
FUEL_LEVEL 
WARMUPS_SINCE_DTC_CLEAR 
DISTANCE_SINCE_DTC_CLEAR 
EVAP_VAPOR_PRESSURE 
BAROMETRIC_PRESSURE 
O2_S1_WR_CURRENT 
O2_S2_WR_CURRENT 
O2_S3_WR_CURRENT 
O2_S4_WR_CURRENT 
O2_S5_WR_CURRENT 
O2_S6_WR_CURRENT 
O2_S7_WR_CURRENT 
O2_S8_WR_CURRENT 
CATALYST_TEMP_B1S1 
CATALYST_TEMP_B2S1 
CATALYST_TEMP_B1S2 
CATALYST_TEMP_B2S2 
PIDS_C 
STATUS_DRIVE_CYCLE 
CONTROL_MODULE_VOLTAGE 
ABSOLUTE_LOAD 
COMMANDED_EQUIV_RATIO 
RELATIVE_THROTTLE_POS 
AMBIANT_AIR_TEMP 
THROTTLE_POS_B 
THROTTLE_POS_C 
ACCELERATOR_POS_D 
ACCELERATOR_POS_E 
ACCELERATOR_POS_F 
THROTTLE_ACTUATOR 
RUN_TIME_MIL 
TIME_SINCE_DTC_CLEARED 
unsupported 
MAX_MAF 
FUEL_TYPE 
ETHANOL_PERCENT 
EVAP_VAPOR_PRESSURE_ABS 
EVAP_VAPOR_PRESSURE_ALT 
SHORT_O2_TRIM_B1 
LONG_O2_TRIM_B1 
SHORT_O2_TRIM_B2 
LONG_O2_TRIM_B2 
FUEL_RAIL_PRESSURE_ABS 
RELATIVE_ACCEL_POS 
HYBRID_BATTERY_REMAINING 
OIL_TEMP 
FUEL_INJECT_TIMING 
FUEL_RATE 
unsupported'''
	tempSplit = allPossibleDataCommands.split("\n")
	commandsList= tempSplit
	return commandsList


def getAllDataUnits():
	allPossibleUnits = '''bitarray
special
special
(string, string)
Unit.percent
Unit.celsius
Unit.percent
Unit.percent
Unit.percent
Unit.percent
Unit.kilopascal
Unit.kilopascal
Unit.rpm
Unit.kph
Unit.degree
Unit.celsius
Unit.grams_per_second
Unit.percent
string
special
Unit.volt
Unit.volt
Unit.volt
Unit.volt
Unit.volt
Unit.volt
Unit.volt
Unit.volt
string
special
boolean
Unit.second
bitarray
Unit.kilometer
Unit.kilopascal
Unit.kilopascal
Unit.volt
Unit.volt
Unit.volt
Unit.volt
Unit.volt
Unit.volt
Unit.volt
Unit.volt
Unit.percent
Unit.percent
Unit.percent
Unit.percent
Unit.count
Unit.kilometer
Unit.pascal
Unit.kilopascal
Unit.milliampere
Unit.milliampere
Unit.milliampere
Unit.milliampere
Unit.milliampere
Unit.milliampere
Unit.milliampere
Unit.milliampere
Unit.celsius
Unit.celsius
Unit.celsius
Unit.celsius
bitarray
special
Unit.volt
Unit.percent
Unit.ratio
Unit.percent
Unit.celsius
Unit.percent
Unit.percent
Unit.percent
Unit.percent
Unit.percent
Unit.percent
Unit.minute
Unit.minute

Unit.grams_per_second
string
Unit.percent
Unit.kilopascal
Unit.pascal
Unit.percent
Unit.percent
Unit.percent
Unit.percent
Unit.kilopascal
Unit.percent
Unit.percent
Unit.celsius
Unit.degree
Unit.liters_per_hour
'''
	tempSplit = allPossibleUnits.split("\n")

	tempSplit3 = []
	for i in range(len(tempSplit)):
		tempSplit2 = tempSplit[i].split(".")
		tempSplit3.append(tempSplit2)
	unitsList = []

	for k in range(len(tempSplit3)):
		if len(tempSplit3[k]) == 2:
			unitsList.append(tempSplit3[k][1])
		if len(tempSplit3[k]) == 1:
			unitsList.append(tempSplit3[k][0])
		if len(tempSplit3[k]) == 0:
			unitsList.append('')
	return unitsList

def printAllCommandDeclarations(commandsList): #first instantiate commandsList then pass it into this function
	for i in range(len(commandsList)):
		print(f"{commandsList[i]} = connection.query(obd.commands.{commandsList[i]})")

def csvExporter(labels, data):
	dictionary = dict(zip(labels[0], zip(*data)))
	df = pd.DataFrame(dictionary)

	x = datetime.datetime.now()
	today = x.strftime("%x")
	time = x.strftime("%X")
	today = today.replace('/','-')
	time = time.replace(':','-')
	date = today+"-"+time

	desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
	# desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') //for linux
	df.to_csv(f'{desktop_path}/ElectronOBD {date}.csv', encoding='utf-8')
	return df
