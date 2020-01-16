# -*- coding: utf-8 -*-

from PIL import ImageDraw, ImageFont

class ButtonsLabelsView():
    def __init__(self, position, size, color=255, bgcolor=0, font_size = 10, spacing=40, rightoffset=30):
        (self.width, self.height) = size
        self.position = position
        self.rect = (position[0], position[1], position[0] +size[0], position[1]+size[1])
        self.pointer_character = u"|";
        self.color = color;
        self.bgcolor = bgcolor;
        self.font_size = font_size
        self.font = ImageFont.truetype('Heebo-Regular.ttf', font_size, encoding="utf-8")
        self.spacing = spacing
        self.rightoffset = rightoffset;
        self.labels = ()

    def set_labels(self, labels):
        self.labels = labels

    def draw(self, draw):
        draw.rectangle(self.rect, fill=self.bgcolor)
        bottomY = self.position[1] + self.height
        for index in range(len(self.labels)):
            label = self.labels[index]
            (textwidth, textheight) = draw.textsize(label, font=self.font)
            leftX = self.width - index*self.spacing - self.rightoffset
            textStartLeftX = leftX - textwidth / 2
            if(textStartLeftX < 5):
                textStartLeftX = 5
            draw.text((textStartLeftX, bottomY - self.font_size * 2), "".join(reversed(label)) , fill=self.color, font=self.font)
            draw.text((leftX, bottomY - self.font_size), self.pointer_character , fill=self.color, font=self.font)
