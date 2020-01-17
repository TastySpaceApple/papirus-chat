import RPi.GPIO as GPIO

# Assume Papirus Zero
SW1 = 21
SW2 = 16
SW3 = 20
SW4 = 19
SW5 = 26

import time

class PapirusButtonsHandler():
    def __init__(self):
        self.buttons_pins = [SW5, SW4, SW3, SW2, SW1]
        self.lastValues = [False, False, False, False, False]
        self.running = False
	    self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        for pin in self.buttons_pins:
            GPIO.setup(pin, GPIO.IN)

    def getButtonClicked(self):
        values = [GPIO.input(pin) == False for pin in self.buttons_pins]
        bclicked = False
        #numButtonsPressed = sum(1 if buttonValue == True else 0 for buttonValue in values)

        for buttonIndex in range(len(values)):
            if self.lastValues[buttonIndex] == True and values[buttonIndex] == False:
            	bclicked = buttonIndex
                break

        self.lastValues = values
	    return buttonIndex
