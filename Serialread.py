import serial

ser = serial.Serial(
        # Serial Port to read the data from
        port='/dev/ttyUSB0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
# Pause the program for 1 second to avoid overworking the serial port
while 1:
    
    if (ser.inWaiting() > 0):
        x=ser.readline()
        x=x.decode("utf-8")
        x = x.split()
        y = x[1]
        print(y) 