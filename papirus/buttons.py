import RPi.GPIO as GPIO

# Assume Papirus Zero
SW1 = 21
SW2 = 16
SW3 = 20
SW4 = 19
SW5 = 26

import thread
import time

class PapirusButtonsHandler(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.setup()
        self.button_pins = (SW5, SW4, SW3, SW2, SW1)
        self.lastValues = [False, False, False, False, False]
        self.listeners = []
        self.running = false

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        for pin in self.button_pins:
            GPIO.setup(pin, GPIO.IN)

    def add_listener(self, listener):
        self.listeners.append(listener);
        if not self.running:
            self.run()

    def notifyPress(self, buttonIndex):
        for listener in self.listeners:
            listener(buttonIndex)

    def run(self):
        self.running = True
        while True:
            values = [GPIO.input(pin) == True for pin in self.button_pins]
            #numButtonsPressed = sum(1 if buttonValue == True else 0 for buttonValue in values)

            for buttonIndex in range(values):
                if self.lastValues[buttonIndex] == True
                        and values[buttonIndex] == False:
                        self.notifyPress(buttonIndex)

            time.sleep(0.2)
