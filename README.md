# ElectronOBD99
## What it is
ElectronOBD is a simple but modern-style desktop app that I made for displaying ECU sensor data from your car to a laptop screen in real-time with the option to export to CSV file afterwards for machine learning purposes. It only supports on Windows for now and not packaged into an .exe file, but I was able to get the results I wanted from it, so I thought it was a good time to show it off. The real magic happens thanks to the Python-OBD API (https://python-obd.readthedocs.io/en/latest/) which interfaces with your car via the OBD-II port and reads data from it. My work here was creating a comprehensive GUI to make the process more user-friendly, remove the need to code anything yourself and practice full stack dev skills. 

## The motivation
For some research work I am doing, I needed a way to log and export ECU data from my KIA Forte into a nice CSV file format. 
Turns out the goddamn connection doesnt work if your car has bluetooth on!!!!
