#Temp and DO logging script version 2
#originally written May 2022 by Jessica Reemeyer
#updated Jul 2022 to move temp sensor to arduino
#previous version had temp sensor connected to rpi
#this versuion has both DO and Temp sensors connected to arduino and
#sending the readings back to the rpi over serial usb connection
#this change was made because the temp sensors were periodically not being
#detected properly by some of the Rpis (1-wire connections would stop working altogether)


import serial
import os
import glob
from time import sleep, strftime, time

def write_data(temp,DO,filename):
    file = filename + ".csv"
    with open(file, 'a') as log:
        log.write('{0},{1},{2}\n'.format(strftime('%Y-%m-%d %H:%M:%S'),str(temp),str(DO)))

def main():
    
    logDir = '/home/pi/sensor_data_logs'
    if os.path.isdir(logDir) == False:
        os.mkdir(logDir)
    
    filename=os.path.join(logDir,strftime('Temp_DO_%b_%Y'))
    
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.reset_input_buffer()
    except:
        ser = "NA"
    
    while True:
        if ser != "NA":
            if ser.in_waiting > 0:
                reading = ser.readline().decode('utf-8').rstrip()
                try:
                    DO, temp = reading.split(';')
                except:
                    DO = "NA"
                    temp = "NA"
                write_data(temp, DO, filename)
        else:
            write_data(read_temp(), "NA", filename)

if __name__ == '__main__':   
    main()

