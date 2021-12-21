import time

message = """
////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////

After this message, you should see about 100 RPM values of your car being logged into the console. 
The Python-OBD debugging mode is on so you might see a lot of scary read/write hexadecimal containing 
messages. That probably means everything is going well, but debugging info before that can inform you 
if the connection to the car was successful, and if not, some info on what went wrong.

////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////
"""
print(message)
time.sleep(1)

#Code to test connection and OBD
import obd 
obd.logger.setLevel(obd.logging.DEBUG) # enables all debug information
ports = obd.scan_serial() #shows what serial ports are available to Python-OBD      
if len(ports)>1: #if more than 1 port available, it chooses the second port. this is not really needed (or helpful) i think.
    c = obd.OBD(ports[1])
else:
    c = obd.OBD(ports[0])

d = 0 
for i in range(1,100):
    r = c.query(obd.commands.RPM)#rpm values
    print("\n", r,"\n")
    d = d +1



