from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock
import word
import phonetic_ui


Builder.load_file("kv/word.kv")


class WordListElement(BoxLayout):
    pass


class WordList(BoxLayout):
    def __init__(self, **kwargs):
        super(WordList, self).__init__(**kwargs)
        Clock.schedule_once(self.on_start, 0)


    def on_start(self, *args):
        self.ids.item_list.clear_widgets()

        for obj in word.get_all():
            elyt = WordListElement()
            elyt.ids.word.text = obj.word
            elyt.ids.type_code.text = obj.type_code
            elyt.ids.connection_id.text = str(obj.connection_id)
            self.ids.item_list.add_widget(elyt)


    def add(self):
        WordAddPopup(self).open()


class WordAddPopup(Popup):
    def __init__(self, master, **kwargs):
        super(WordAddPopup, self).__init__(**kwargs)
        self.title = "Add new Word"
        self.master = master


    def add(self):
        word = self.ids.word_input.text.strip()
        type_code = self.ids.type_code_input.text.strip()
        connection_id = self.ids.connection_id_input.text.strip()
        # db.Database().type_add(code, name, description)
        self.dismiss()
        self.master.on_start()


class WordChooser(BoxLayout):
    def __init__(self, **kwargs):
        super(WordChooser, self).__init__(**kwargs)

        self.word = None
        self.mainbutton_text = 'Select a word...'
        self.none_text = '...'

        self.dropdown = DropDown()

        self.mainbutton = Button(text=self.mainbutton_text)
        self.add_widget(self.mainbutton)
        self.mainbutton.bind(on_release = self.dropdown.open)

        self.dropdown.bind(on_select = self.callback)

        words = word.get_all()
        if bool(words):
            element = Button(size_hint_y=None)
            element.text = self.none_text
            element.bind(on_release=lambda element: self.dropdown.select(element.text))
            self.dropdown.add_widget(element)

            for obj in words:
                element = Button(size_hint_y=None)
                element.text = f"{obj.word} ({obj.type_code})"
                element.bind(on_release=lambda element: self.dropdown.select(element.text))
                self.dropdown.add_widget(element)


    def callback(self, instance, x):
        if x == self.none_text:
            setattr(self.mainbutton, 'text', self.mainbutton_text)
            self.word = None
        else:
            setattr(self.mainbutton, 'text', x)
            self.word = x
        print(self.word)
