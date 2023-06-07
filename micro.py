import RPi.GPIO as gpio
import MFRC522
import Keypad
import sys
import os
import time

buzzerPin = 11 # sound pin
rgbPins = [11, 12, 13] # rgb led pins
mfrc = MFRC522.MFRC522() # RFID

# Keypad
rows = 4        # number of rows of the Keypad
cols = 4        #number of columns of the Keypad
keys =  [   '1','2','3','A',    #key code
            '4','5','6','B',
            '7','8','9','C',
            '*','0','#','D'     ]
rowsPins = [12,16,18,22]     #out pins
colsPins = [19,15,13,11]


def setupAlert():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)         # use PHYSICAL GPIO Numbering
    gpio.setup(buzzerPin, gpio.OUT)   # set buzzerPin to OUTPUT mode
    print("Loaded Alert Module!")

def setupRgbLed():
    global pwmRed,pwmGreen,pwmBlue  
    gpio.setmode(gpio.BOARD)       # use PHYSICAL GPIO Numbering
    gpio.setup(rgbPins, gpio.OUT)     # set RGBLED pins to OUTPUT mode
    gpio.output(rgbPins, gpio.HIGH)   # make RGBLED pins output HIGH level
    pwmRed = gpio.PWM(rgbPins[0], 2000)      # set PWM Frequence to 2kHz
    pwmGreen = gpio.PWM(rgbPins[1], 2000)  # set PWM Frequence to 2kHz
    pwmBlue = gpio.PWM(rgbPins[2], 2000)    # set PWM Frequence to 2kHz
    pwmRed.start(0)      # set initial Duty Cycle to 0
    pwmGreen.start(0)
    pwmBlue.start(0)
    print("Loaded RGB Led!")

def setupKeypad():
    print("Loaded Keypad Module!")

def setupRfid():
    print("Loaded RFID Module!")

def setupAll():
    setupKeypad()
    setupRgbLed()
    setupAlert()
    setupRfid()

    print("System initiatilizing..")

def loop():
    while(True):
        pass
    pass

def destroyAll():
    destroyKeypad()
    destroyRgbLed()
    destroyAlert()
    destroyRfid()

def cleanUp():
    gpio.cleanup()

def destroyKeypad():
    cleanUp()

def destroyRgbLed():
    pwmRed.stop()
    pwmGreen.stop()
    pwmBlue.stop()
    gpio.cleanup()

def destroyAlert():
    cleanUp()

def destroyRfid():
    cleanUp()

if __name__ == '__main__':
    setupAll()

    try:
        pass
    except:
        pass
    finally:
        destroyAll()