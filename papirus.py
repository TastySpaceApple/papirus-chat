# -*- coding: utf-8 -*-

from papirus import Papirus
from papirus import PapirusButtonsHandler
from apps import ChatApp

WHITE = 255
BLACK = 0

print("help")

class PapirusSystem():
    class PapirusDisplay:
        def __init__(self):
            self.papirus = Papirus(rotation=180)
            self.papirus.clear()

        def update(self, im):
            self.papirus.display(im)
            if first_draw:
                self.papirus.update()
            else:
                self.papirus.partial_update()

    def __init__(self, width=200, height=96):

        self.display = PapirusSystem.PapirusDisplay()
        self.input = PapirusButtonsHandler()
        self.input.start()

        self.app = ChatApp(self.display, self.input)
        self.input.button_press = lambda btnIndex: self.app.button_press(btnIndex)


if __name__ == "__main__":
    system = PapirusSystem()
    system.start()
