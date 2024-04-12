# Detecting endangered fish with an underwater lense 🐟
This reposity describes the materials and methods used to build an underwater camera equipped with water quality sensors (temperature and dissolved oxygen) using Raspberry Pi and Arduino. The set ups described below were tested and deployed in the Old Ausable Channel (OAC) in Lambton Shores, Ontario 🇨🇦. The OAC is a narrow, low flow freshwater stream near the south shore of Lake Huron. Due to its natural history the OAC contains a high level of freshwater fish diversity and is home to multiple fish species-at-risk. 

The endangered Lake Chubsucker (*Erimyzon sucetta*) calls the OAC home and we were able to use these cameras to capture them across the channel. As seen here in this example still of two adult Lake Chubsucker:
<img src="https://user-images.githubusercontent.com/46727953/217915085-d2625f1f-6942-4adc-a481-6d837d14668a.png" width="600"/>

## Materials Needed
- [Raspberry Pi Zero W] (https://www.raspberrypi.com/products/raspberry-pi-zero-w/) 
- formatted SD card
- Raspberry Pi HQ camera
- camera cable adaptor
- Raspberry Pi 6mm 3MP wide angle lense
- [WittyPi 3 rev2] (https://www.uugear.com/product/witty-pi-3-realtime-clock-and-power-management-for-raspberry-pi/) 
- [Arduino uno board] (https://store-usa.arduino.cc/products/arduino-uno-rev3?selectedStore=us)
- [Gravity: Analog Dissolved Oxygen Sensor / Meter kit for Arduino] (https://www.dfrobot.com/product-1628.html) or [name] (https://atlas-scientific.com/kits/surveyor-analog-do-kit/)
- Waterproof DS18B20 digital temperature sensor
- [lithium ion battery pack] (https://www.pishop.ca/product/lithium-ion-battery-pack-3-7v-6600mah/)

## Camera construction guide
### Configure your Raspberry Pi

If you're not familiar with Raspberry Pi (rpi) computers I recommend following the [Raspberry Pi foundations tutorials] (https://www.raspberrypi.com/documentation/computers/getting-started.html) to set it up. You will need to format an sd card with Raspberry Pi OS and solder header pins to the pi if it did not come with them (in order to attache the WittyPi board). 

### Configure the power supply

For this project I used a lithium ion battery connected directly to the WittyPi board as shown below. The WittyPi board can be loaded with a schedule script that automatically turns your Pi on and off. I did this to conserve battery power, so that I could deploy my cameras for a week at a time. However, if you want your pi to run continuously after deployment, you don't need to use the WittyPi. You could simply get a power bank from your local outdoors shop and connect it to your pi directly with a usb cable. 

(add photo of wittypi and battery connected)

### Prepare the DO sensor 

Information about the DO sensor can be found [here] (https://wiki.dfrobot.com/Gravity__Analog_Dissolved_Oxygen_Sensor_SKU_SEN0237) and [here] (https://atlas-scientific.com/kits/surveyor-analog-do-kit/). The tip of the sensor will need to be filled with the appropriate solution (check the documentation of the sensor you have for instructions). 

### Configure your Arduino

This project uses an arduino board to collect dissolved oxygen and temperature data, and passes that data to the rpi over i2c through a usb cable. Connect the sensors as shown in the diagram below. Then connect the arduino to a computer with the arduino IDO installed (you can also do this on the rpi). Install the "atlas_gravity.zip", "OneWire-master.zip", and "Arduino-Temperature-Control_Library-master.zip" files (located in this project folder) as libraries to your arduino IDE (sketch > include library > Add .ZIP Library...). Then you can download the "temp_do_combined.ino" file from this project folder and upload it to your arduino through the IDE. 
 
To calibrate your DO sensor, open the serial plotter under the "tools" tab and select a baud rate of 9600 then type CAL. This will set the 100% DO calibration for your sensor. 

### Connect the camera 

The camera cable that comes with the rpi camera does not fit with the rpi zero board, so we need to swap it out for the adaptor. If you are using a different raspberry pi board (not a zero) you don't need to do this. This project uses an older camera and legacy camera support needs to be enabled in the rpi configuration for it to work. If you are using a newer camera you won't need to do that, but the python scripts used in this project probably won't work and would need to be adjusted. 

### Add the python scripts to the rpi

### Schedule the python scripts 

## Deployment tips

## Next steps 
### Adjusting dissolved oxygen values 

## Other resources 

I highly recommend [this guide] (https://raspberrypi-guide.github.io/) and [associated review paper] (https://doi.org/10.1111/2041-210X.13652) as a general resource for using Raspberry Pi computers for science projects. 
