There are two files:
1) serialFloatTerm.py
2) serialFloatGraph.py
3) eHealth_ecg_float/eHealth_ecg_float.ino 
The first just prints out the values being read off the serial port and prints them in the terminal
The second graphs the data using matplotlib
The third is the code you load onto the arduino to grab the ECG data off the sensors. (you need to have the eHealth lib installed in Arduino)


you'll need some python modules installed obviously. i dont want to assume experience with python, if you dont have the modules:
> pip install pyserial
> pip install numpy
> pip install matplotlib

(ive installed these a while ago, the module names of best practices of installing may have changed some)

to make the python files executable you may need to change permissions. 
> chmod 755 serialFloatTerm.py
> chmod 755 serialFloatGraph.py

will probably do it for it. other wise chmod a + x < filename > is overkill... 

upload the code onto your arduino. 
(make sure your serial port monitor isnt open in arduino, i find that having two processes listening on the same port doesnt work)
then run:
> python serialFloatTerm.py

and you should see the numbers start flying down your screen. 
to kill it: ctrl + c 

> python serialFloatGraph.py

voila!
if you get an errors, you probably didnt set the right com port, see line 31: port='/dev/tty.usbmodemfd121',
you need to change that to match your com port from arduino. 
OR you dont have python set up correctly (good luck with a that one) (this should work on 2.7 but im no python expert, obviously)
OR you dont have the modules installed. 
OR you have the modules installed but the paths arent correct so python cant find them. 
OR mars and venus arent aligned well enough with pluto and Voyager iii well enough anymore... 

I'll be working on cleaning up the data to get actual good looking ECG waveforms coming across the screen. 
email me at sakotturi AT gMAIL dot com if you have any questions or issues. 
