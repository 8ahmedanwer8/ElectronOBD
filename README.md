# ElectronOBD
#### Demo: Coming soon
## What is it
ElectronOBD is a simple, but modern-style desktop app I made for displaying real-time ECU sensor data from my sedan to a laptop screen with CSV file export option for machine learning tasks. It is only supported on Windows for now and not packaged into an .exe file (I think it's better to run it from command line anyway), but I was able to get the results I wanted from it and so I thought it was a good time to post this repo. The real magic happens thanks to the Python-OBD API (https://python-obd.readthedocs.io/en/latest/) which interfaces with the car via its OBD-II port from the laptop's serial port, and retrieves data every second. My work here was creating a fullstack electron app to make the process more user-friendly, free and targeted towards AI. Only thing to buy is the actual OBD-II USB adapter, which should be compatible with most cars, but you can read more about that online.

## The motivation behind it
For some uni work I was doing, I needed a way to log and export ECU data from my KIA Forte into a nice CSV file format. All OBD softwares online seemed to have some kind of a paywall. So I decided to make my own opensource desktop app. At first I considered using an OBD-II Bluetooth adapter with OBD apps on the Playstore. But, this would not have allowed for CSV file export with Pandas and any other customization I may have wanted. Data rate for bluetooth can also be slow and unreliable sometimes. That's why I chose a direct-wired connection to my laptop with this OBD-II to USB [adapter] (https://www.amazon.ca/gp/product/B07THHVLR2/ref=ppx_yo_dt_b_asin_title_o04_s01?ie=UTF8&psc=1)(not amazon affiliate link). Finally, I found Python-OBD, which is a great library that handles low-level communication between the computer and car via the ELM-327 microcontroller inside the OBD-II adapter. The adapter itself is capable of HS-CAN and MS-CAN, but I found HS-CAN wasn't being recognized by py-OBD, but MS-CAN got the job done.

## Setup
This setup procedure will likely go through edits as I test ElectronOBD on more Windows devices, but below is what I have so far. I'm also assuming the reader is familiar with programming and downloading things, but not familar with downloading and using github projects. If any trouble, the internet should have the answers.

1) First you should install the dependencies. Install Python 3 and the Python Pandas library. Python 3 can be installed from python.org and then pandas can be installed from the command prompt by typing in ```pip install pandas```. You can also download Pandas from https://pandas.pydata.org/, but installing it with pip in the CMD is quicker.

2) The next and final dependency is Node.js. You can install Node from https://nodejs.org/en/. 

3) Now you can clone this repo and save it somewhere in your computer. Then copy the directory of where it is and paste it into CMD like this ```cd directory``` where directory is the path to the project. 

4) Now when you are in the directory in your CMD (it should say the directory name and you should be able to type whatever you want), type ```npm install```. This should install the electron dependencies
setup, this is probably fonna suck and i iwll need to change it but here is how i set i would tell someone to set it up -> dependencies 

troubleshooting, probbaly sucks but will need to change it if this project grows -> bluetooth car off, check to see if test.py runs, try running a few times, see which message it gets stuck on. i will develop this more in the future again. i tested it out on one car and computer.

want  to get it out for jetson nano but arm core compataibility will be hard but its first on the list

mention the words elm327, ISO something, miso can stuff. 

Turns out the goddamn connection doesnt work if your car has bluetooth on!!!!
