from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.list import MDList, TwoLineListItem
import wordtype
import tools


Builder.load_file("kv/wordtype.kv")


class WordTypeChooser(tools.Chooser):
    def __init__(self, **kwargs):
        elements = {}
        for obj in wordtype.get_all():
            elements.update({obj.code: obj.name})
        super(WordTypeChooser, self).__init__(elements, button_text="Select a Word Type...", popup_title="Word Type chooser", **kwargs)


class WordTypeList(tools.AssetList):
    def __init__(self, **kwargs):
        self.title = "Word Types"
        super(WordTypeList, self).__init__(**kwargs)


    def on_start(self, *args):
        self.ids.item_list.clear_widgets()

        for obj in wordtype.get_all():
            elyt = WordTypeListElement()
            elyt.ids.code.text = obj.code
            elyt.ids.name.text = obj.name
            elyt.ids.description.text = obj.description
            self.ids.item_list.add_widget(elyt)


    def add(self):
        WordTypeAddPopup(self).open()


class WordTypeListElement(MDBoxLayout):
    def edit(self, x):
        print("Edit:", x)


class WordTypeAddPopup(Popup):
    def __init__(self, master, **kwargs):
        super(WordTypeAddPopup, self).__init__(**kwargs)
        self.title = "Add new Type"
        self.master = master


    def add(self):
        code = self.ids.code_input.text.strip()
        name = self.ids.name_input.text.strip()
        description = self.ids.description_input.text.strip()

        ok, message = wordtype.WordType(code=code, name=name, description=description).save()
        if bool(ok):
            self.dismiss()
            self.master.on_start()
        else:
            print(message)
