from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivymd.uix.list import TwoLineListItem
from kivy.clock import Clock


Builder.load_file("kv/tools.kv")


class AssetList(Popup):
    def __init__(self, **kwargs):
        super(AssetList, self).__init__(**kwargs)
        Clock.schedule_once(self.on_start, 0)


    def on_start(self, *args):
        pass


    def add(self):
        pass


class Chooser(Button):
    def __init__(self, elements, button_text=None, popup_title=None, none_row=True, **kwargs):
        super(Chooser, self).__init__(**kwargs)
        self.__value = None

        self.button_text = None
        if bool(button_text):
            self.text = button_text
        else:
            self.text = "Select..."
        self.button_text = self.text

        self.__popup = ChooserPopup(self, elements, none_row)
        if bool(popup_title):
            self.title = popup_title
        else:
            self.title = "Chooser"
        self.__popup.title = popup_title


    def get_value(self):
        return self.__value


    def popup_open(self):
        self.__popup.open()


    def callback(self, x, y):
        if len(y) > 0:
            self.__value = y
            self.text = f"{x} ({y})"
        else:
            self.__value = None
            self.text = self.button_text
        self.__popup.dismiss()


class ChooserPopup(Popup):
    def __init__(self, master, elements, none_row=True, **kwargs):
        super(ChooserPopup, self).__init__(**kwargs)
        self.__master = master
        self.elements = elements
        self.none_row = none_row
        Clock.schedule_once(self.on_start, 0)


    def on_start(self, *args):
        if bool(self.none_row):
            self.row_add("None", "")
        for key, value in self.elements.items():
            self.row_add(value, key)


    def row_add(self, value, key):
        element = ChooserElement(self, value, key)
        self.ids.list.add_widget(element)


    def callback(self, value, key):
        self.__master.callback(value, key)


class ChooserElement(TwoLineListItem):
    def __init__(self, master, text, secondary_text, **kwargs):
        super(ChooserElement, self).__init__(**kwargs)
        self.__master = master
        self.text = text
        self.secondary_text = secondary_text


    def callback(self, x, y):
        self.__master.callback(x, y)
