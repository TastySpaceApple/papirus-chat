# -*- coding: utf-8 -*-

import Tkinter
from PIL import ImageTk, Image, ImageDraw, ImageFont
from views import ButtonsLabelsView
from controllers import KeyboardInputController

WHITE = 255
BLACK = 0

class ChatAppDesktopDemo(Tkinter.Tk):

    def __init__(self):
        Tkinter.Tk.__init__(self)

        width = 200
        height = 96

        im = Image.new('1', (width, height), WHITE)
        self.ImbImage = Tkinter.Canvas(self, highlightthickness=0, bd=0, bg='red', width=width, height=height)
        self.ImbImage.pack()

        draw = ImageDraw.Draw(im)
        #draw.rectangle((0, 0, width, height), fill=WHITE, outline=WHITE)
        #draw.rectangle([0, 0, 40, 40 ], fill=BLACK)

        #draw.text((5, 10), ('test'), fill=BLACK, font=font)
        keyboard = KeyboardInputController()

        keyboard.button_press(0)

        button_labels_view_height = 25
        button_labels_view = ButtonsLabelsView(
            (0, height - button_labels_view_height),
            (width, button_labels_view_height),
            color=WHITE, bgcolor=BLACK)

        button_labels_view.set_labels(keyboard.get_labels())

        button_labels_view.draw(draw)

        del draw

        self.i = ImageTk.PhotoImage(im)
        self.ImbImage.create_image(width/2, height/2, image=self.i)

if __name__ == "__main__":
    ChatAppDesktopDemo().mainloop()
