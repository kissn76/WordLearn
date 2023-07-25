from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import db_sqlite as db


class MainMenu(BoxLayout):
    def select(self, button):
        print(button)


class TypelistWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"


    def type_set(self, instance, value):
        print(instance, value)


    def load(self):
        database = db.Database()
        types = database.types_get()

        for type_t in types:
            self.ids.item_list.add_widget(Label(text=str(type_t[0])))
            b = Label(text=f"[ref={type_t[0]}/{type_t[1]}][color=0000ff]{type_t[1]}[/color][/ref]", markup=True)
            b.bind(on_ref_press=self.type_set)
            self.ids.item_list.add_widget(b)


class MainWindow(App):
    def build(self):
        tlw = TypelistWindow()
        tlw.load()
        return tlw


if __name__ == '__main__':
    MainWindow().run()