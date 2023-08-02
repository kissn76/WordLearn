from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import phonetic


class PhoneticAddBoxRow(BoxLayout):
    def __init__(self, **kwargs):
        super(PhoneticAddBoxRow, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.add_widget(TextInput())
        self.add_widget(TextInput())


class PhoneticAddBox(BoxLayout):
    def __init__(self, **kwargs):
        super(PhoneticAddBox, self).__init__(**kwargs)
        self.orientation = "vertical"
        btn_add = Button(text="+", size_hint_x=None)
        btn_add.bind(on_release=lambda element: self.new_row())
        self.add_widget(btn_add)
        self.add_widget(PhoneticAddBoxRow())


    def new_row(self):
        self.add_widget(PhoneticAddBoxRow())