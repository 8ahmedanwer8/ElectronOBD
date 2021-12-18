# ElectronOBD99
## What it is
ElectronOBD is a simple but modern-style desktop app that I made for displaying ECU sensor data from your car to a laptop screen in real-time with the option to export to CSV file afterwards for machine learning purposes. It is only supported on Windows for now and not packaged into an .exe file (I think it's better to run it from CMD anyway), but I was able to get the results I wanted from it and so I thought it was a good time to post it. The real magic happens thanks to the Python-OBD API (https://python-obd.readthedocs.io/en/latest/) which interfaces with your car via its OBD-II port and reads data from it. My work here was creating a comprehensive GUI to make the process more user-friendly, free and targeted towards AI. Only thing to buy is the actual OBD-II USB adapter, which should be compatible with most cars, but you can read more about that online.

## The motivation
For some uni research work I was doing, I needed a way to log and export ECU data from my KIA Forte into a nice CSV file format. All OBD softwares online seemed to have some kind of a paywall. So I decided to make my own opensource desktop app. At first I considered using an OBD-II Bluetooth adapter with OBD apps on the Playstore. But, this would not have allowed for CSV file export with Pandas and any other customization I may have wanted in the future. Data rate for bluetooth can also be slow and unreliable sometimes. That's why I used a direct-wired connection with this OBD-II USB Adapter [a link](https://amazon.ca). Finally, I found Python-OBD which is a great library that handles a serial connection between the computer and the car's ISO something.

setup, this is probably fonna suck and i iwll need to change it but here is how i set i would tell someone to set it up -> dependencies 

troubleshooting, probbaly sucks but will need to change it if this project grows -> bluetooth car off, check to see if test.py runs, try running a few times, see which message it gets stuck on. i will develop this more in the future again. i tested it out on one car and computer.





Turns out the goddamn connection doesnt work if your car has bluetooth on!!!!
