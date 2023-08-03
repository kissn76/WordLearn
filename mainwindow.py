from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
import db_sqlite as db
import word_ui
import wordtype_ui
import language_ui
import mediatype_ui
import media_ui


Builder.load_file("kv/mainwindow.kv")


class MainPanel(MDBoxLayout):
    def database_del(self):
        database = db.Database()
        database.database_drop()


    def database_create(self):
        database = db.Database()
        database.create_tables()


    def open_wordtype_popup(self):
        wordtype_ui.WordTypeList().open()


class MainWindow(MDApp):
    def build(self):
        return MainPanel()


if __name__ == '__main__':
    MainWindow().run()