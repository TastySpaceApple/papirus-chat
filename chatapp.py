# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont


from papirus import Papirus
from papirus import PapirusButtonsHandler
from views import ButtonsLabelsView
from controllers import KeyboardInputController
import time

WHITE = 255
BLACK = 0

class ChatApp():

    def __init__(self):
        #self.papirus = Papirus(rotation=180)
        #self.papirus.clear()

        self.buttons = PapirusButtonsHandler()

        self.width = 200
        self.height = 96

        # views
        buttons_labels__view_height = 30
        self.buttons_labels_view = KeyboardView(
            (0, height - buttons_labels_view_height),
            (width, buttons_labels_view_height),
            color=WHITE, bgcolor=BLACK)

        # controllers
	    self.keyboard = KeyboardInputController()

        #firstdraw
        self.draw(True)

    def draw(self, first_draw=False):
        im = Image.new('1', (self.width, self.height), WHITE)

        draw = ImageDraw.Draw(im)

        self.buttons_labels_view.set_labels(keyboard.get_labels)
	    self.buttons_labels_view.draw(draw)

        del draw

        #self.papirus.display(im)
        #if first_draw:
        #    self.papirus.update()
        #else:
        #    self.papirus.partial_update()

    def run(self):
        while True:
            if (btn_clicked = self.buttons.getButtonClicked()) is not False:
                self.keyboard.button_press(btn_clicked)
            self.draw()
            time.sleep(0.2)



if __name__ == "__main__":
    chatapp = ChatApp()
    chatappapp.run()
