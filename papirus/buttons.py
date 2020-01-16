import RPi.GPIO as GPIO

# Assume Papirus Zero
SW1 = 21
SW2 = 16
SW3 = 20
SW4 = 19
SW5 = 26

import threading
import time

class PapirusButtonsHandler(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.buttons_pins = [SW5, SW4, SW3, SW2, SW1]
        self.lastValues = [False, False, False, False, False]
        self.listeners = []
        self.running = False
	self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        for pin in self.buttons_pins:
            GPIO.setup(pin, GPIO.IN)

    def add_listener(self, listener):
        self.listeners.append(listener)
        if not self.running:
            self.run()

    def notifyPress(self, buttonIndex):
	print "button pressed " + str(buttonIndex)
        for listener in self.listeners:
            listener(buttonIndex)

    def run(self):
        self.running = True
        while True:
            values = [GPIO.input(pin) == False for pin in self.buttons_pins]
	    print values
            #numButtonsPressed = sum(1 if buttonValue == True else 0 for buttonValue in values)

            for buttonIndex in range(len(values)):
                if self.lastValues[buttonIndex] == True and values[buttonIndex] == False:
                	self.notifyPress(buttonIndex)

            self.lastValues = values
	    time.sleep(1)
