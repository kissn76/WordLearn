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
        self.ids.item_list.clear_widgets()

        if bool(types):
            for type_t in types:
                elyt = ElemetntItem3()
                elyt.ids.code.text = str(type_t[1])
                elyt.ids.name.text = str(type_t[2])
                elyt.ids.description.text = str(type_t[3])
                self.ids.item_list.add_widget(elyt)
        else:
            Clock.schedule_once(self.on_start, 1)


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
                elyt.ids.code.text = str(type_t[1])
                elyt.ids.name.text = str(type_t[2])
                elyt.ids.description.text = str(type_t[3])
                self.ids.item_list.add_widget(elyt)
        else:
            Clock.schedule_once(self.on_start, 1)


    def add(self):
        print("Add new Language")


class MainPanel(BoxLayout):
    def database_del(self):
        database = db.Database()
        database.database_drop()
        self.ids.tp_tlw.on_start()
        self.ids.tp_llw.on_start()


    def database_create(self):
        database = db.Database()
        database.create_tables()


class MainWindow(App):
    def build(self):
        return MainPanel()


if __name__ == '__main__':
    MainWindow().run()