1a – Led blinking
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

ledPin = 15 #board pin
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, False)

try:
    while True:
        GPIO.output(ledPin, True)
        print("Led On")
        sleep(1)
        GPIO.output(ledPin, False)
        print("Led Off")
        sleep(1)
finally:
    GPIO.output(ledPin, False)
    GPIO.cleanup()

1b – pattern blinking
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
led1 = 29
led2 = 31
led3 = 33
led4 = 35
led5 = 36
led6 = 37
led7 = 38
led8 = 40

#setup the ledPin as output
GPIO.setup(led1, GPIO.OUT)
GPIO.output(led1, False)

def ledpattern(ledVal1, ledVal2, ledVal3, ledVal4, ledVal5, ledVal6, ledVal7, ledVal8):
    GPIO.output(led1, ledVal1)

def patternOne():
    for i in range (0,3):
        ledpattern(1,0,1,0,1,0,1,0)
        time.sleep(1)
        ledpattern(0,1,0,1,0,1,0,1)
        time.sleep(1)

def patternTwo():
    for i in range (0, 5):
        ledpattern(1,0,0,0,0,0,0,0)
        time.sleep(0.1)

def patternThree():
    for i in range (0, 5):
        ledpattern(0,0,0,0,0,0,0,1)
        time.sleep(0.1)
        
def patternFour():
    for i in range(0,5):
     ledpattern(0,1,1,1,1,1,1,1)
     time.sleep(0.1)  

def patternFive():
    for i in range(0,5):
        ledpattern(1,1,1,1,1,1,1,0) 
        time.sleep(0.1)

try:
    while True:
        patternOne()
        patternTwo()
        patternThree()
        patternFour()
        patternFive()

finally:
    GPIO.cleanup()



Prac 2 – 7 segment led
from time import sleep
import tm1637

try:
    import thread
except ImportError:
    import _thread as thread
Display = tm1637.TM1637(CLK=21, DIO=20, brightness=1.0)

try:
    print ("Starting clock in the background (press CTRL + C to stop):")
    Display.StartClock(military_time=False)
    print ('Continue Python script and tweak Display!')
    sleep(5)
    Display.ShowDoublepoint(False)
    sleep(5)
    loops = 3
    while loops > 0:
        for i in range(0, 10):
            Display.SetBrightness(i / 10.0)
            sleep(0.5)
        loops -= 1
    Display.StopClock()
    thread.interrupt_main()
except KeyboardInterrupt:
    print ("Properly closing the clock and open GPIO pins")
    Display.cleanup()

Prac 3 – camera
from time import sleep
from picamera import PiCamera
camera=PiCamera()

camera.resolution=(1080,1920)
camera.start_preview()
sleep(10)
camera.capture('/home/pi/Pictures/random.jpg')
camera.stop_preview()

Command:
$ sudo raspistill -o /home/pi/Desktop/image.jpg

prac 4 – telegram
import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

ledPin = 38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)

def on(pin):
    GPIO.output(pin, True)
    return

def off(pin):
    GPIO.output(pin, False)
    return

def handle(message):
    chat_id = message['chat']['id']
    command = message['text']
    print("Got command " +  command)

    if command == "on":
        bot.sendMessage(chat_id, on(ledPin))
    elif command == "off":
        bot.sendMessage(chat_id, off(ledPin))

bot = telepot.Bot('Enter your bot token') 
bot.message_loop(handle)
print("I am listening............")
while True:
    time.sleep(10)
    

Commands:
Install python package: sudo apt-get install python-pip

Install telepot: sudo pip install telepot

#python (file path)

Clone the git: git clone https://github.com/salmanfarisvp/TelegramBot.git

Run the code: python telegrambot.py



















        

