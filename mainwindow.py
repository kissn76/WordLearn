from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import db_sqlite as db
import word_ui
import wordtype_ui
import language_ui
import mediatype_ui
import media_ui


Builder.load_file("kv/mainwindow.kv")


class MainPanel(BoxLayout):
    def database_del(self):
        database = db.Database()
        database.database_drop()
        self.ids.tp_tlw.on_start()
        self.ids.tp_llw.on_start()
        self.ids.tp_wlw.on_start()
        self.ids.tp_mtlw.on_start()
        self.ids.tp_mlw.on_start()


    def database_create(self):
        database = db.Database()
        database.create_tables()
        self.ids.tp_tlw.on_start()
        self.ids.tp_llw.on_start()
        self.ids.tp_wlw.on_start()
        self.ids.tp_mtlw.on_start()
        self.ids.tp_mlw.on_start()


class MainWindow(App):
    def build(self):
        return MainPanel()


if __name__ == '__main__':
    MainWindow().run()