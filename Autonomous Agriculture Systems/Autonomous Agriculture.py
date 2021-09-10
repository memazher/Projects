import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT) #rain sensor
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.IN)#soil sensor
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.IN) #relay and pump

while True:
  state = GPIO.input(3)
  if (state==1): #if rain is not detected
    print("No rain")
    state1 = GPIO.input(17) #status of soil sensor record
     if  state1==1:
        print("dry")
        print("watering plant")
        GPIO.output(27, GPIO.HIGH)  # relay set on
        time.sleep(6) #6 second, time may vary
        GPIO.output(27, GPIO.LOW) # relay set off
  else:
    print("There is Rain outside")

 
  
    
    
    
  
