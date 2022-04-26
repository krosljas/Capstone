import smbus2 #I2C modules
import math #used for scaling calculations
import time #time delay imports

#Registers
reg_1 = 0x6b #MPU6050 power managment register
reg_2 = 0x6c #MPU6050 power managment register

def read_byte(reg): #reading the address
	return bus.read_byte_data(address, reg) 

def read_word(reg): #reading accelrometer data off MPU6050
	h = bus.read_byte_data(address, reg) #read the address for register
	l = bus.read_byte_data(address, reg+1) #read address from the next register
	value = (h << 8) + l #concentration of the higher and lower value for unsigned bit value
	return value #returned in 16 bit
#this function converts the 16 unsigned bit value
def read_word_2c(reg):
	val = read_word(reg) #read the 16 unsigned bit value
	if (val >= 0x8000): #if val is greater than register return
		return -((65535-val)+1) #gets signed value from mpu 6050
	else:
		return val
		
def dist(a, b): #calculating the magnitude
	return math.sqrt((a*a)+(b*b))
	
bus = smbus2.SMBus(1) # interface communication with the I2C bus
address = 0x68 #address of the MPU6050

#activate to be able to access the module through restting the sensor
bus.write_byte_data(address, reg_1, 0)

# Data collection portion for IMU
f = open("Data/accel.txt", "w") #packet the data into a txt file
for i in range(50):#collect 100 values
	
	acceleration_xout = read_word_2c(0x3b) #collection of the x values from MPU6050 0x3b is the x register
	acceleration_yout = read_word_2c(0x3d) #collection of the y values from MPU6050 0x3b is the y register
	acceleration_zout = read_word_2c(0x3f) #collection of the z values from MPU6050 0x3b is the z register
	#the mpu6050 uses a sensitivity scale factor of 16384 LSB
	acceleration_xout_scaled = acceleration_xout / 16384.0 #scaling the x values
	acceleration_yout_scaled = acceleration_yout / 16384.0 #scaling the y values
	acceleration_zout_scaled = acceleration_zout / 16384.0 #scaling the z values
	
	f.write('{0} {1} {2}\n'.format(acceleration_xout_scaled, acceleration_yout_scaled, acceleration_zout_scaled))
	time.sleep(0.3)
	
f.close()
