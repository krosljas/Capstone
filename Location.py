#GPS Interfacing with Raspberry Pi using Pyhton
#http://www.electronicwings.com

import serial #import serial pacakge
import time #to be able to time delay
import sys  #import system package

def GPS_Info():
    global NMEA_buff #making global varibles so they can be accesed by all classes
    global lat_in_degrees
    global long_in_degrees
    nmea_time = [] 
    nmea_latitude = [] #create a list of latitude values
    nmea_longitude = [] #create a list of longitude values
    nmea_time = NMEA_buff[0] #extract time from GPGGA string
    nmea_latitude = NMEA_buff[1] #extract latitude from GPGGA string
    nmea_longitude = NMEA_buff[3]#extract longitude from GPGGA string
    
    lat = float(nmea_latitude) #converting string into float for calculation
    longi = float(nmea_longitude) #converting string into float for calculation
    
    lat_in_degrees = convert_to_degrees(lat)    #convert latitude into decimal format
    long_in_degrees = convert_to_degrees(longi) #convert longitude into decimal format

#convert raw NMEA string into degree decimal format   
def convert_to_degrees(raw_value): #below is the conversion from NMEA to the commonly used terms of long and lat
    decimal_value = raw_value/100.00 
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - int(decimal_value))/0.6
    position = degrees + mm_mmmm
    position = "%.4f" %(position)
    return position
    


gpgga_info = "$GPGGA," #GPGGA is a basic GPS NMEA message
ser = serial.Serial ("/dev/serial0")              #Opening serial pot 0 where connection is established
GPGGA_buffer = 0
NMEA_buff = 0
lat_in_degrees = 0 #inital varible for lat
long_in_degrees = 0 #initial varible for longitude

#Open a specific file
file1 = open('Data/location.txt', 'w'); #writing the data to GPSData.txt
                                  
good_header = "   Latitude  :   Longitude  :   Time\n"; 
#writing the header to the file                                
file1.write(good_header);

tyme = time.perf_counter(); 

for i in range(10):
        received_data = (str)(ser.readline())
        GPGGA_data_available = received_data.find(gpgga_info)   #check for NMEA GPGGA string                 
        if (GPGGA_data_available>0): #check if there is data that is there
            GPGGA_buffer = received_data.split("$GPGGA,",1)[1]  #store data coming after "$GPGGA," string 
            NMEA_buff = (GPGGA_buffer.split(','))#store comma separated data in buffer
            GPS_Info()                                          #get time, latitude, longitude
 
            #print("latitude:", lat_in_degrees," longitude: ", "-", long_in_degrees, '\n')
            file1.write("   " + lat_in_degrees + "      " + "-" + long_in_degrees + "        " + str(time.perf_counter() - tyme) + "\n");
            time.sleep(3)
file1.close()
