# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont


from papirus import Papirus
from views import ButtonsLabelsView

WHITE = 255
BLACK = 0

class ChatApp():

    def __init__(self):
        self.papirus = Papirus(rotation=180)
        self.papirus.clear()

        self.buttons = PapirusButtonsHandler()
        self.buttons.add_listener(self.button_press)

        self.width = 200
        self.height = 96

        # views
        keyboard_height = 30
        keyboard_view = KeyboardView(
            (0, height - keyboard_height),
            (width, keyboard_height),
            color=WHITE, bgcolor=BLACK)

        #firstdraw
        self.draw(True)

    def draw(self, first_draw=False):
        im = Image.new('1', (self.width, self.height), WHITE)

        draw = ImageDraw.Draw(im)

        self.keyboard_view.draw(draw)

        del draw

        self.papirus.display(im)
        if first_draw:
            self.papirus.update()
        else
            self.papirus.partial_update()

    def button_press(self, buttonIndex):
        self.keyboard.button_press(buttonIndex)
        self.draw()



if __name__ == "__main__":
    app = ChatApp()
