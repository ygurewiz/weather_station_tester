
import serial
from serial import Serial
import time
import re
import keyboard 

def main():
    ser_RW = serial.Serial("com12", baudrate = 9600, timeout =0.1)
    ser_write_only = serial.Serial("com8", baudrate = 9600, timeout =0.1)
    
    initPorts(ser_RW,ser_write_only)
    readPort(ser_RW,ser_write_only)
    ser_RW.close()
    

def readPort(ser_RW,ser_write_only):
    i=0
    while(True):  
        
        line = str(ser_RW.readline())      
        if(len(line)>3):
            print (line)
        #if keyboard.is_pressed('q'):
        #    print("\n\n\n\n\n detected pressing of q\n\n\n\n")
            #ser_RW.write('00BR\r'.encode('utf-8'))
            #write_comm('00TR4',ser_RW,ser_write_only)
        #    write_comm('00PE02',ser_RW,ser_write_only) 
        #    print ("\n\n\nend\n\n\n")
        try:
            if(len(line)>25 and not re.findall(line,'!')):
                windSpeed = line[7:11]
                windDirection = line[12:15]
                temp = line[16:21]
                perc = line[53]
                percInt = line[43:51]

                print ("temp: " + temp)
                print ("wind speed: " +windSpeed)
                print ("wind direction: " + windDirection)
                print ("perceiptation: " + perc)
                print ("perceiptation intensity: " + percInt)
                print("\n\n\n")
        except:
            print("")
        #print (line)
        #i=i+1
        #print(i)
  

init =False
def write_comm(com,ser_RW,ser_write_only):
    global init
    if init:
        ser_RW.write((com + '\r').encode('utf-8'))
    else:
        ser_write_only.write((com + '\r').encode('utf-8'))
    while(ser_RW.in_waiting>0):
        print(str(ser_RW.readline())+'\n')
        time.sleep(0.05)

    time.sleep(0.5)

def initPorts(ser_RW,ser_write_only):  
    global init

    write_comm('00KY04711',ser_RW,ser_write_only) #admin
    print("1")
    time.sleep(0.5)
    init = True
    ser_write_only.close()
    write_comm('00PE0010',ser_RW,ser_write_only)
    print("111")
    time.sleep(0.5)
    print("11111")
    write_comm('00PW0010',ser_RW,ser_write_only) 
    print("11111111")
    write_comm('00PH0100',ser_RW,ser_write_only) 
    time.sleep(0.5)
    #write_comm('00PT1',ser_RW,ser_write_only) 
    print("2")
    write_comm('00CS1',ser_RW,ser_write_only)
    print("3")
    time.sleep(0.5)
    write_comm('00DM0000',ser_RW,ser_write_only)
    print("4")
    time.sleep(0.5)
    write_comm('00TR0004',ser_RW,ser_write_only)
    time.sleep(0.5)
    print("5")
    write_comm('00OR1000',ser_RW,ser_write_only)
    time.sleep(0.5)
    print("6")
    write_comm('00PN0015',ser_RW,ser_write_only)
    time.sleep(0.5)

    
    


if __name__=='__main__':
    main()