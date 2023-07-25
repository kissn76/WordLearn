from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.clock import Clock
import db_sqlite as db


class TypelistWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(TypelistWindow, self).__init__(**kwargs)
        self.orientation = "vertical"
        Clock.schedule_once(self.on_start, 0)


    def on_start(self, *args):
        database = db.Database()
        types = database.types_get()

        for type_t in types:
            self.ids.item_list.add_widget(Label(text=str(type_t[0])))
            self.ids.item_list.add_widget(Label(text=type_t[1]))


class MainPanel(BoxLayout):
    pass


class MainWindow(App):
    def build(self):
        return MainPanel()


if __name__ == '__main__':
    MainWindow().run()