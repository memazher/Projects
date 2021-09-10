import sys
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import tweepy
from firebase import firebase

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27, GPIO.OUT)

#Twitter API Credential

consumer_key        = 'xxxxx'
consumer_secret     = 'xxxxx'
access_token        = 'xxxxx'
access_token_secret = 'xxxxx'

#Google firebase Credential

url = 'xxxxx'    #firebase console url
firebase = firebase.FirebaseApplication(url)

#function to Access Twitter API

def OAuth():
	try:
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret )
		auth.set_access_token(access_token, access_token_secret)
		return auth
	except Exception as e:
		return None

#to continuously check DHT11 sensor output

while True:
    h, t = Adafruit_DHT.read_retry(11, 4)                     #store temperature/humidity in t and h variable
    print 'Temp: {0:0} C  Humidity: {1:0} %'.format(t, h)     #print temperature/humidity in the terminal
    firebase.put("/","/temperature",t)                        #upload temperature at firebase
    firebase.put("/","/humidity",h)                           #upload humidity at firebase
    if t > 27.0 and h > 65:
        print("AC ON")
        GPIO.output(27, GPIO.HIGH)                            #Relay triggered
        oauth = OAuth()                                       #calling twitter api function
        api = tweepy.API(oauth)
        try:
            api.update_status('Temp: {0:0} C  Humidity: {1:0} % AC ON'.format(t, h)) #posting tweet
        except tweepy.TweepError as error:
            if error.api_code == 187:                         #error handling
                # Do something special
                print('duplicate message')
            else:
                raise error
        print('a tweet is posted')
        
    else:
        print("Temperature and Humidity is stable, AC remain OFF")
        print("AC OFF")
        GPIO.output(27, GPIO.LOW)
        oauth = OAuth()
        api = tweepy.API(oauth)
        try:
            api.update_status('Temp: {0:0} C  Humidity: {1:0} % AC OFF'.format(t, h))
        except tweepy.TweepError as error:
            if error.api_code == 187:
                # Do something special
                print('duplicate message')
            else:
                raise error
        print('a tweet is posted')
        
    time.sleep(1)

#dua to twitter policy, we cannot tweet same message multiple times.
#sunce our system check sensor status continuously, same message will be tweet on the twitter
# as a result an error generate 187, to overcome we have included try and except block.

