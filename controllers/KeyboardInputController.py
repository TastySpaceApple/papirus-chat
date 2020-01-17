# -*- coding: utf-8 -*-

KEYBOARD_LAYOUTS = {
    'he': (list(u' אבגד'),
           list(u'הוזחט'),
           list(u'יכלמנ'),
           list(u'סעפצק'),
           list(u'רשת'))
}
class KeyboardInputController():

    def __init__(self, keyboardLayoutName='he'):
        self.keyboardLayoutName = keyboardLayoutName
        self.keyboardLayout = KEYBOARD_LAYOUTS[keyboardLayoutName]
        self.hierarchy = -1

    def get_labels(self):
        if(self.hierarchy == -1):
            return ["".join(line) for line in self.keyboardLayout]
        else:
            return self.keyboardLayout[self.hierarchy]

    def button_click(self, buttonIndex):
        if self.hierarchy == -1:
            self.hierarchy = buttonIndex
        else:
            self.hierarchy = -1
