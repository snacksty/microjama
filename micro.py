import RPi.GPIO as gpio
import MFRC522
import Keypad
import sys
import os
import time

# Variable of configuration
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


# Initial setup functions
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
    gpio.setwarnings(False)
    setupKeypad()
    setupRgbLed()
    setupAlert()
    setupRfid()

    print("System initiatilizing..")

# Destroy objects was used
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

# Features to run
def getOptionFromKeys():
    pass

def readFromKeypad():
    keypad = Keypad.Keypad(keys,rowsPins,colsPins,rows,cols)    #creat Keypad object
    keypad.setDebounceTime(50)      #set the debounce time
    key = ""
    while(True):
        key = keypad.getKey()       #obtain the state of keys
        if(key != keypad.NULL):     #if there is key pressed, print its key code.
            print (f"{key}", end="")
            break
    return key


def scanTag():
    mfrc = MFRC522.MFRC522()
    while(True):
		# Scan for cards    
        (status,TagType) = mfrc.MFRC522_Request(mfrc.PICC_REQIDL)
		# If a card is found
        if status == mfrc.MI_OK:
            print ("Card detected")
			# Get the UID of the card
            (status,uid) = mfrc.MFRC522_Anticoll()				
			# If we have the UID, continue
            if status == mfrc.MI_OK:
                print ("Card UID: "+ str(map(hex,uid)))
				# Select the scanned tag
                if mfrc.MFRC522_SelectTag(uid) == 0:
                    print ("MFRC522_SelectTag Failed!")
            break


def loop():
    while(True):
        pass
    pass 

if __name__ == '__main__':
    setupAll()

    try:
        letter = ""
        while(True):
            print("\n\nHola!\nElije lo que quieres hacer:")
            print("  A -> Escanear un Tag RFID")
            print("  B -> Introducir la clave desde Keypad")
            print(">> ", end="")
            letter = readFromKeypad()
            

            if (letter == "A"):
                print("Scanning...")
                scanTag()
            elif (letter == "B"):
                print("Write Password: ", end="")
                passw = input()


            else:
                print("Esta opción no esta Activa!\n\n\n")
    except:
        pass
    finally:
        destroyAll()