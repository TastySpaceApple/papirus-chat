import RPi.GPIO as GPIO

# Assume Papirus Zero
SW1 = 21
SW2 = 16
SW3 = 20
SW4 = 19
SW5 = 26

import time
import threading

class PapirusButtonsHandler(threading.Thread()):
    def __init__(self):
        self.buttons_pins = [SW5, SW4, SW3, SW2, SW1]
        self.lastValues = [False, False, False, False, False]
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

    def button_press(self, buttonIndex):
        print("press " + str(buttonIndex))

    def run(self):
        while True:
            values = [GPIO.input(pin) == False for pin in self.buttons_pins]
            #numButtonsPressed = sum(1 if buttonValue == True else 0 for buttonValue in values)

            for buttonIndex in range(len(values)):
                if self.lastValues[buttonIndex] == True and values[buttonIndex] == False:
                	self.button_press(buttonIndex)
                    break

            self.lastValues = values
            time.sleep(0.3)
