from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class PronunciationAddBoxRow(BoxLayout):
    def __init__(self, **kwargs):
        super(PronunciationAddBoxRow, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.add_widget(TextInput())
        self.add_widget(TextInput())


class PronunciationAddBox(BoxLayout):
    def __init__(self, **kwargs):
        super(PronunciationAddBox, self).__init__(**kwargs)
        self.orientation = "vertical"
        btn_add = Button(text="+", size_hint_x=None)
        btn_add.bind(on_release=lambda element: self.new_row())
        self.add_widget(btn_add)
        self.add_widget(PronunciationAddBoxRow())


    def new_row(self):
        self.add_widget(PronunciationAddBoxRow())