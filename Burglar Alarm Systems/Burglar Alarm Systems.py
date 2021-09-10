import RPi.GPIO as GPIO
import time
from twilio.rest import Client

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)  # buzzer
GPIO.setwarnings(False)
GPIO.setup(27, GPIO.IN)  # vibration sensor
GPIO.setwarnings(False)
GPIO.setup(22, GPIO.OUT)  # green light
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT)  # red light

    

while True:
    state = GPIO.input(27)

    if (state==1):  # if vibration SEnsor output is high, then do this
        print("Movement Detected")
        try:
        account_sid = "XXXXXX"  # Put your Twilio account SID here
        auth_token = "XXXXXX"  # Put your auth token here
        client = Client(account_sid, auth_token)
    
        message = client.api.account.messages.create(
            to="XXXXXX",  # Put your cellphone number here
            from_="XXXXXX",  # Put your Twilio number here
            body="Movement Detected") # Message, that you want to send
        except:
            print("fail to send message")
        GPIO.output(17, GPIO.HIGH)  # then,raised an alarm
        GPIO.output(22, GPIO.LOW)  # green led set off
        GPIO.output(26, GPIO.HIGH)  # red led set on
        
    else: #if vibration SEnsor output is low, then do this
        print("No movement detected")
        GPIO.output(26, GPIO.LOW)  # red led set off
        GPIO.output(22, GPIO.HIGH)  # green led set on
        GPIO.output(17, GPIO.LOW) #alarm stop

