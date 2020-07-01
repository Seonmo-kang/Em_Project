import RPi.GPIO as GPIO
from time import sleep
from MCP_main import analog_read
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIOIN = 17
GPIOOUT = 27
 
#핀 넘버링을 BCM 방식을 사용한다.
GPIO.setmode(GPIO.BCM)
#17번 핀을 입력용, 27번 핀을 출력용으로 설정한다.
#출력용 핀은 LED 상태를 확인하기 위해 사용하는 핀으로 실제 동작과는 무관하다.
GPIO.setup(GPIOIN, GPIO.IN)
GPIO.setup(GPIOOUT, GPIO.OUT)

class sensor1:
    
    def __init__(self):
        power = False
        
        
    def sensor_on(self):
        sensor = None
        while self.power:
            sensor=GPIO.input(18)
            
            if sensor==1:
                print("none")
                sleep(0.5)
                
            else:
                print("hand")
                sleep(0.5)
        print("Finish")
                
    def motion(self):        #GPIO 핀 17,27을 사용한다.
        
        #try:
        while self.power2:
            #HC-SR501센서의 출력 값을 읽는다.
            state =  GPIO.input(GPIOIN)
            if(state == True):
                print ('state: Motion detected')
                GPIO.output(GPIOOUT, state) 
                sleep(2)
            else:
                print ('state: No Motion')
                #HC-SR501센서의 출력 값을 LED로 보낸다.
                GPIO.output(GPIOOUT, state)
                sleep(0.5)
        print("Finish")
#        except KeyboardInterrupt:
#            GPIO.cleanup()
#        print ('HC-SR501 motion detection end')
    def jodo(self):
        while self.power3:
            reading = analog_read(0)
            voltage = reading * 3.3 / 1024
            print("Reading=%d\tVoltage=%f" % (reading, voltage))
            sleep(0.1)
        print("Finish")

