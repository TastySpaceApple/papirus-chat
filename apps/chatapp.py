# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

from views import ButtonsLabelsView, TextInputView
from controllers import KeyboardInputController
import time

WHITE = 255
BLACK = 0

class ChatApp:

    def __init__(self, display, input):
        self.display = display
        self.input = input

        self.width = 200
        self.height = 96

        # views
        buttons_labels_view_height = 20
        self.buttons_labels_view = ButtonsLabelsView(
            (0, self.height - buttons_labels_view_height),
            (self.width, buttons_labels_view_height),
            color=BLACK, bgcolor=WHITE)

        text_input_height = 20
        self.text_input_view = TextInputView(
            (0, self.height - buttons_labels_view_height - text_input_height),
            (self.width, text_input_height))

        # controllers
        self.keyboard = KeyboardInputController()
        self.keyboard.character_entered = lambda c: self.text_input_view.enter(c)

        #firstdraw
        self.draw(True)

    def draw(self, first_draw=False):
        self.buttons_labels_view.set_labels(self.keyboard.get_labels())

        im = Image.new('1', (self.width, self.height), WHITE)

        draw = ImageDraw.Draw(im)
        self.buttons_labels_view.draw(draw)
        self.text_input_view.draw(draw)

        del draw

        self.display.update(im)

    def button_press(self, button_index):
        self.keyboard.button_click(button_index)
        self.draw()


#if __name__ == "__main__":
#    chatapp = ChatApp()
#    chatappapp.run()
