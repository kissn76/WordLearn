from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock
import db_sqlite as db


Builder.load_file("kv/language.kv")


class LanguageElemetntItem(BoxLayout):
    pass


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
                elyt = LanguageElemetntItem()
                elyt.ids.code.text = str(type_t[0])
                elyt.ids.name.text = str(type_t[1])
                elyt.ids.description.text = str(type_t[2])
                self.ids.item_list.add_widget(elyt)


    def add(self):
        print("Add new Language")