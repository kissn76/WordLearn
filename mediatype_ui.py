from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock
import mediatype


Builder.load_file("kv/mediatype.kv")


class MediaTypeChooser(BoxLayout):
    def __init__(self, **kwargs):
        super(MediaTypeChooser, self).__init__(**kwargs)

        self.type = None

        self.dropdown = DropDown()
        self.mainbutton = Button(text ='Select type...')
        self.add_widget(self.mainbutton)
        self.mainbutton.bind(on_release = self.dropdown.open)

        self.dropdown.bind(on_select = lambda instance, x: setattr(self.mainbutton, 'text', x))
        self.dropdown.bind(on_select = self.callback)

        self.names = {}
        for obj in mediatype.get_all():
            self.names.update({obj.name: obj.code})
            element = Button(size_hint_y=None)
            element.text = obj.name
            element.bind(on_release=lambda element: self.dropdown.select(element.text))
            self.dropdown.add_widget(element)


    def callback(self, instance, x):
        self.type = self.names[x]
        print(self.type)


class MediaTypeElementItem(BoxLayout):
    pass


class MediaTypeList(BoxLayout):
    def __init__(self, **kwargs):
        super(MediaTypeList, self).__init__(**kwargs)
        Clock.schedule_once(self.on_start, 0)


    def on_start(self, *args):
        self.ids.item_list.clear_widgets()

        for obj in mediatype.get_all():
            elyt = MediaTypeElementItem()
            elyt.ids.code.text = obj.code
            elyt.ids.name.text = obj.name
            elyt.ids.description.text = obj.description
            self.ids.item_list.add_widget(elyt)


    def add(self):
        MediaTypeAddPopup(self).open()


class MediaTypeAddPopup(Popup):
    def __init__(self, master, **kwargs):
        super(MediaTypeAddPopup, self).__init__(**kwargs)
        self.title = "Add new Type"
        self.master = master


    def add(self):
        code = self.ids.code_input.text.strip()
        name = self.ids.name_input.text.strip()
        description = self.ids.description_input.text.strip()
        mediatype.MediaType(code=code, name=name, description=description).save()
        self.dismiss()
        self.master.on_start()
