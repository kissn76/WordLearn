from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock
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

        self.types =  wordtype.types_get()
        self.types_name = {}
        if bool(self.types):
            for code, obj in self.types.items():
                self.types_name.update({obj.name: code})
                element = Button(size_hint_y=None)
                element.text = obj.name
                element.bind(on_release=lambda element: self.dropdown.select(element.text))
                self.dropdown.add_widget(element)


    def callback(self, instance, x):
        self.type = self.types_name[x]
        print(self.type)


class WordTypeElemetntItem(BoxLayout):
    pass


class WordTypelistWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(WordTypelistWindow, self).__init__(**kwargs)
        Clock.schedule_once(self.on_start, 0)


    def on_start(self, *args):
        self.ids.item_list.clear_widgets()

        types =  wordtype.types_get()
        if bool(types):
            for code, obj in types.items():
                elyt = WordTypeElemetntItem()
                elyt.ids.code.text = code
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
        wordtype.WordType(code, name, description).save()
        self.dismiss()
        self.master.on_start()