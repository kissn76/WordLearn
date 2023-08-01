from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock
import db_sqlite as db


class WordlistElement(BoxLayout):
    pass


class WordlistWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(WordlistWindow, self).__init__(**kwargs)
        Clock.schedule_once(self.on_start, 0)


    def on_start(self, *args):
        database = db.Database()
        types = database.words_get()
        self.ids.item_list.clear_widgets()

        if bool(types):
            for type_t in types:
                elyt = WordlistElement()
                elyt.ids.id.text = str(type_t[0])
                elyt.ids.word.text = str(type_t[1])
                elyt.ids.type_code.text = str(type_t[2])
                elyt.ids.connection_id.text = str(type_t[3])
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

        self.dropdown = DropDown()
        self.mainbutton = Button(text ='Select a word...')
        self.add_widget(self.mainbutton)
        self.mainbutton.bind(on_release = self.dropdown.open)

        self.dropdown.bind(on_select = lambda instance, x: setattr(self.mainbutton, 'text', x))
        self.dropdown.bind(on_select = self.callback)

        database = db.Database()
        words = database.words_get()

        self.word_dict = {}

        if bool(words):
            for word_t in words:
                w = f"{str(word_t[1])} ({str(word_t[2])})"
                self.word_dict.update({w: str(word_t[0])})
                element = Button(size_hint_y=None)
                element.text = w
                element.bind(on_release=lambda element: self.dropdown.select(element.text))
                self.dropdown.add_widget(element)


    def callback(self, instance, x):
        self.word = x
        print(self.word)


class TypeChooser(BoxLayout):
    def __init__(self, **kwargs):
        super(TypeChooser, self).__init__(**kwargs)

        self.type = None

        self.dropdown = DropDown()
        self.mainbutton = Button(text ='Select type...')
        self.add_widget(self.mainbutton)
        self.mainbutton.bind(on_release = self.dropdown.open)

        self.dropdown.bind(on_select = lambda instance, x: setattr(self.mainbutton, 'text', x))
        self.dropdown.bind(on_select = self.callback)

        database = db.Database()
        types = database.types_get()

        self.type_dict = {}

        if bool(types):
            for type_t in types:
                self.type_dict.update({str(type_t[1]): str(type_t[0])})
                element = Button(size_hint_y=None)
                element.text = str(type_t[1])
                element.bind(on_release=lambda element: self.dropdown.select(element.text))
                self.dropdown.add_widget(element)


    def callback(self, instance, x):
        self.type = self.type_dict[x]
        print(self.type)


class ElemetntItem3(BoxLayout):
    pass


class TypelistWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(TypelistWindow, self).__init__(**kwargs)
        Clock.schedule_once(self.on_start, 0)


    def on_start(self, *args):
        database = db.Database()
        types = database.types_get()
        self.ids.item_list.clear_widgets()

        if bool(types):
            for type_t in types:
                elyt = ElemetntItem3()
                elyt.ids.code.text = str(type_t[0])
                elyt.ids.name.text = str(type_t[1])
                elyt.ids.description.text = str(type_t[2])
                self.ids.item_list.add_widget(elyt)


    def add(self):
        TypeAddPopup(self).open()


class TypeAddPopup(Popup):
    def __init__(self, master, **kwargs):
        super(TypeAddPopup, self).__init__(**kwargs)
        self.title = "Add new Type"
        self.master = master


    def add(self):
        code = self.ids.code_input.text.strip()
        name = self.ids.name_input.text.strip()
        description = self.ids.description_input.text.strip()
        db.Database().type_add(code, name, description)
        self.dismiss()
        self.master.on_start()


class LanguagelistWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(LanguagelistWindow, self).__init__(**kwargs)
        Clock.schedule_once(self.on_start, 0)


    def on_start(self, *args):
        database = db.Database()
        types = database.languages_get()
        self.ids.item_list.clear_widgets()

        if bool(types):
            for type_t in types:
                elyt = ElemetntItem3()
                elyt.ids.code.text = str(type_t[0])
                elyt.ids.name.text = str(type_t[1])
                elyt.ids.description.text = str(type_t[2])
                self.ids.item_list.add_widget(elyt)


    def add(self):
        print("Add new Language")


class MainPanel(BoxLayout):
    def database_del(self):
        database = db.Database()
        database.database_drop()
        self.ids.tp_tlw.on_start()
        self.ids.tp_llw.on_start()
        self.ids.tp_wlw.on_start()


    def database_create(self):
        database = db.Database()
        database.create_tables()
        self.ids.tp_tlw.on_start()
        self.ids.tp_wlw.on_start()


class MainWindow(App):
    def build(self):
        return MainPanel()


if __name__ == '__main__':
    MainWindow().run()