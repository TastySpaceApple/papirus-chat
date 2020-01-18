# -*- coding: utf-8 -*-

from PIL import ImageDraw, ImageFont

class TextInputView:
    def __init__(self, position, size, font_size = 12):
        self.position = position
        self.size = size
        self.rect = (position[0], position[1], position[0] +size[0] -1, position[1]+size[1] - 1)
        self.font_size = font_size
        self.font = ImageFont.truetype('Heebo-Regular.ttf', font_size, encoding="utf-8")
        self.value = u""
        self.middleY = self.position[1] + self.size[1] /  2

    def draw(self, draw):
        draw.rectangle(self.rect, outline=0)
        offset_right = 5
        (textwidth, textheight) = draw.textsize(self.value, font=self.font)

        draw.text((self.size[0] - textwidth - offset_right, self.middleY - textheight / 2 - 3), self.value , fill=0, font=self.font)

    def enter(self, c, rtl=True):
        if rtl:
            self.value = c + self.value
        else:
            self.value = self.value + c
