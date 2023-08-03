from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout
import wordtype


Builder.load_file("kv/wordtype.kv")


class WordTypeChooser(BoxLayout):
    def __init__(self, **kwargs):
        super(WordTypeChooser, self).__init__(**kwargs)

        self.type = None

        self.dropdown = DropDown()
        self.mainbutton = Button(text ='Select type...')
        self.add_widget(self.mainbutton)
        self.mainbutton.bind(on_release = self.dropdown.open)

        self.dropdown.bind(on_select = lambda instance, x: setattr(self.mainbutton, 'text', x))
        self.dropdown.bind(on_select = self.callback)

        self.names = {}
        for obj in wordtype.get_all():
            self.names.update({obj.name: obj.code})
            element = Button(size_hint_y=None)
            element.text = obj.name
            element.bind(on_release=lambda element: self.dropdown.select(element.text))
            self.dropdown.add_widget(element)


    def callback(self, instance, x):
        self.type = self.names[x]
        print(self.type)


class WordTypeElementItem(MDBoxLayout):
    pass


class WordTypeList(MDBoxLayout):
    def __init__(self, **kwargs):
        super(WordTypeList, self).__init__(**kwargs)
        Clock.schedule_once(self.on_start, 0)


    def on_start(self, *args):
        self.ids.item_list.clear_widgets()

        for obj in wordtype.get_all():
            elyt = WordTypeElementItem()
            elyt.ids.code.text = obj.code
            elyt.ids.name.text = obj.name
            elyt.ids.description.text = obj.description
            self.ids.item_list.add_widget(elyt)


    def add(self):
        WordTypeAddPopup(self).open()


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
