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


class MainWindow(MDApp):
    def build(self):
        return MainPanel()


if __name__ == '__main__':
    MainWindow().run()