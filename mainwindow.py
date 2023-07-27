from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock
import db_sqlite as db


class ElemetntItem3(BoxLayout):
    pass


class TypelistWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(TypelistWindow, self).__init__(**kwargs)
        Clock.schedule_once(self.on_start, 0)


    def on_start(self, *args):
        database = db.Database()
        types = database.types_get()

        for type_t in types:
            elyt = ElemetntItem3()
            elyt.ids.id.text = str(type_t[0])
            elyt.ids.name.text = str(type_t[1])
            elyt.ids.description.text = str(type_t[2])
            self.ids.item_list.add_widget(elyt)


    def add(self):
        TypeAddPopup().open()


class TypeAddPopup(Popup):
    def __init__(self, **kwargs):
        super(TypeAddPopup, self).__init__(**kwargs)
        self.title = "Add new Type"


    def add(self):
        id = self.ids.id_input.text
        name = self.ids.name_input.text
        description = self.ids.description_input.text
        print("Add new Type", id, name, description)


class LanguagelistWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(LanguagelistWindow, self).__init__(**kwargs)
        Clock.schedule_once(self.on_start, 0)


    def on_start(self, *args):
        database = db.Database()
        types = database.languages_get()

        for type_t in types:
            elyt = ElemetntItem3()
            elyt.ids.id.text = str(type_t[0])
            elyt.ids.name.text = str(type_t[1])
            elyt.ids.description.text = str(type_t[2])
            self.ids.item_list.add_widget(elyt)


    def add(self):
        print("Add new Language")


class MainPanel(BoxLayout):
    pass


class MainWindow(App):
    def build(self):
        return MainPanel()


if __name__ == '__main__':
    MainWindow().run()