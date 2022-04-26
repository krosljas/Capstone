import os
import glob
import time
 
os.system('modprobe w1-gpio') #recieving data from gpio pins
os.system('modprobe w1-therm') #reading from the temperature sensor
 
base_dir = '/sys/bus/w1/devices/' #point to the location of sensor data in pi
device_folder = glob.glob(base_dir + '28*')[0] #default location of sensor data in pi
device_file = device_folder + '/w1_slave' #default location of sensor data in pi
  
def read_temp_raw(): #function that opens file that contains the temperature output
    f = open(device_file, 'r') #opening the file
    lines = f.readlines() #reading the file line by line
    f.close() #closing the file
    return lines #returning the lines so the function can use it
 
def read_temp(): #processing the data to farhenheit and celcisus from read_temp_raw
    lines = read_temp_raw()  #reading the value from the previous function
    while lines[0].strip()[-3:] != 'YES': #while loop to check if there is data
        time.sleep(0.2) #time delay
        lines = read_temp_raw() #reading the values in a loop from the previous function
    equals_pos = lines[1].find('t=') #finding the temperatrue with t = Line[1] means looking for second element in the array
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:] #the starting position of temperature t and adding 2 positions to only get temperature numbers
        temp_c = float(temp_string) / 1000.0 #conversion to celcius
        temp_f = temp_c * 9.0 / 5.0 + 32.0 #conversion to farenheit
        return temp_f 


f = open("Data/temp.txt", "w") #opening a txt file for the data

for i in range(10): #for loop to get values
    
    curr_temp = str(read_temp()) #converting float to string
    f.write(curr_temp + '\n') #writing to new txt files
    time.sleep(.3) #time delay

f.close() #close file
