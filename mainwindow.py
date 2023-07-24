from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import db_sqlite as db


class TypesWindow(GridLayout):

    def __init__(self, **kwargs):
        super(TypesWindow, self).__init__(**kwargs)

        self.cols = 2
        self.add_widget(Label(text='id'))
        self.add_widget(Label(text='name'))

        database = db.Database()
        types = database.types_get()

        for type_t in types:
            self.add_widget(Label(text=str(type_t[0])))
            self.add_widget(Label(text=type_t[1]))


class MainWindow(App):

    def build(self):
        return TypesWindow()


if __name__ == '__main__':
    MainWindow().run()