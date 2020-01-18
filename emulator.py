# -*- coding: utf-8 -*-

import tkinter
from PIL import ImageTk, Image, ImageDraw, ImageFont
from views import ButtonsLabelsView
from controllers import KeyboardInputController
from apps import ChatApp

WHITE = 255
BLACK = 0

print("help")

class Emulator(tkinter.Tk):
    class EmulatorInput:
        def __init__(self, tk):
            numButtons = 5
            self.buttons = [None] * numButtons
            for i in range(numButtons):
                self.buttons[i] = tkinter.Button(tk, text =" "+str(numButtons- i)+" ", command=lambda i=i: self.handle_press(i))
                offset = 15
                if i == 0: offset = 20
                self.buttons[i].pack(padx=(0, offset), side="right")
        def handle_press(self, buttonIndex):
            self.button_press(buttonIndex)

        def button_press(self, buttonIndex):
            print("press " + str(buttonIndex))

    class EmulatorDisplay:
        def __init__(self, canvas, width, height, tk):
            self.canvas = canvas
            self.width = width
            self.height = height
            self.tk = tk
        def update(self, im):
            self.i = ImageTk.PhotoImage(im)
            self.canvas.create_image(self.width/2, self.height/2, image=self.i)
            #self.canvas.draw()
            #self.tk.update_idletasks()
            self.tk.update()

    def __init__(self, width=200, height=96):

        tkinter.Tk.__init__(self)

        self.configure(background='white')

        canvas = tkinter.Canvas(self, highlightthickness=0, bd=0, bg='white', width=width, height=height)
        canvas.pack()

        self.display = Emulator.EmulatorDisplay(canvas, width, height, self)
        self.input = Emulator.EmulatorInput(self)

        self.app = ChatApp(self.display, self.input)
        self.input.button_press = lambda btnIndex: self.app.button_press(btnIndex)
        #self.app.start()

if __name__ == "__main__":
    Emulator().mainloop()
