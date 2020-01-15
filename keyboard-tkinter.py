# -*- coding: utf-8 -*-

import Tkinter
from PIL import ImageTk, Image, ImageDraw, ImageFont



# initially set all white background
#image = Image.new('1', (width, height), WHITE)

# prepare for drawing
#draw = ImageDraw.Draw(image)
#draw.rectangle((0, 0, width, height), fill=WHITE, outline=WHITE)

#font = ImageFont.truetype('FreeMonoBold.ttf', 10)
#draw.text((5, 10), ('test'), fill=BLACK, font=font)




WHITE = 255
BLACK = 0

class KeyboardView():
    def __init__(self, position, size, color=255, bgcolor=1, font_size = 10):
        self.size = size
        self.position = position
        self.rect = (position[0], position[1], position[0] +size[0], position[1]+size[1])
        self.characters = (reversed((u'[]', u'א', u'ב', u'ג', u'ד')),
                           reversed((u'ה', u'ו', u'ז', u'ח', u'ט')),
                           reversed((u'י', u'כ', u'ל', u'מ', u'נ')),
                           reversed((u'ס', u'ע', u'פ', u'צ', u'ק')),
                           reversed((u'ר', u'ש', u'ת')))
        self.pointer_character = u"|";
        self.color = color;
        self.bgcolor = bgcolor;
        self.font_size = font_size
        self.font = ImageFont.truetype('Heebo-Regular.ttf', font_size, encoding="utf-8")

    def draw(self, draw):
        draw.rectangle(self.rect, fill=self.bgcolor)
        bottomY = self.position[1] + self.size[1]
        for col in range(len(self.characters)):
            text = "".join(self.characters[col])
            (textwidth, textheight) = draw.textsize(text, font=self.font)
            leftX = self.size[0] - col*35 - 30
            draw.text((leftX - textwidth / 2, bottomY - self.font_size * 2), text , fill=self.color, font=self.font)
            draw.text((leftX, bottomY - self.font_size), self.pointer_character , fill=self.color, font=self.font)

class image_manip(Tkinter.Tk):

    def __init__(self):
        Tkinter.Tk.__init__(self)
        
        width = 200
        height = 96
        self.configure(bg='red')
        im = Image.new('1', (width, height), WHITE)
        self.ImbImage = Tkinter.Canvas(self, highlightthickness=0, bd=0, bg='red', width=width, height=height)
        self.ImbImage.pack()
       
        draw = ImageDraw.Draw(im)
        #draw.rectangle((0, 0, width, height), fill=WHITE, outline=WHITE)
        #draw.rectangle([0, 0, 40, 40 ], fill=BLACK)
        
        #draw.text((5, 10), ('test'), fill=BLACK, font=font)
        keyboard_height = 25
        keyboard_view = KeyboardView(
            (0, height - keyboard_height),
            (width, keyboard_height),
            color=WHITE, bgcolor=BLACK)

        keyboard_view.draw(draw)
        
        del draw

        self.i = ImageTk.PhotoImage(im)
        self.ImbImage.create_image(width/2, height/2, image=self.i)


def run():
    image_manip().mainloop()
    
if __name__ == "__main__":
    run()
