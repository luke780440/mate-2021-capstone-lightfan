from time import sleep
from threading import Thread
import serial

class Comms:
    def __init__(self, port, baud_rate):
        self.port = port
        self.baud_rate = baud_rate
        ser = serial.Serial(self.port, self.baud_rate)
        self.ser.close()
        self.ser.open()
        
    def run(self):
        while True:
            packets = self.ser.read(64)
            packet_list = packets.split(chr(0x7f))
            
            for packet in packet_list:
                if len(packet) != 3:
                    continue
                self.photoResistor = packet[0]
                self.rpm = packet[1]
                self.temp = packet[2]
            lightVal = int(photoResistor)/255 * 1053 
            fan_speed = int(lightVal/1053 * 255)   
            self.ser.write(fan_speed)

    def start_thread(self):
        start_thread = Thread(target = self.run) #initializing the thread 
        start_thread.start()
        

ob = Comms("/dev/tty.usbmodem14201", 9600)
#ob.start_thread()


#basic interface code
user_input = input("Would you like to turn on the fan? Enter Y for yes or N for no: ")
if user_input == Y:
    print("Hi hi!")
    while True:
        ob.start_thread()
        print("Light values:", photoResistor)
        sleep(2)
        print("Fan speed:", fan_speed)
        sleep(2)

else:
    print("Bye bye")
    



