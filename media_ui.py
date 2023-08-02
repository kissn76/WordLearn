from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock
import media


Builder.load_file("kv/media.kv")


class MediaChooser(BoxLayout):
    def __init__(self, **kwargs):
        super(MediaChooser, self).__init__(**kwargs)

        self.media = None

        self.dropdown = DropDown()
        self.mainbutton = Button(text ='Select media...')
        self.add_widget(self.mainbutton)
        self.mainbutton.bind(on_release = self.dropdown.open)

        self.dropdown.bind(on_select = lambda instance, x: setattr(self.mainbutton, 'text', x))
        self.dropdown.bind(on_select = self.callback)

        self.names = {}
        for obj in media.get_all():
            self.names.update({obj.name: obj.code})
            element = Button(size_hint_y=None)
            element.text = obj.name
            element.bind(on_release=lambda element: self.dropdown.select(element.text))
            self.dropdown.add_widget(element)


    def callback(self, instance, x):
        self.media = self.names[x]
        print(self.media)


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

        self.names = {"Voice": "voice", "Picture": "picture"}
        for n, c in self.names.items():
            element = Button(size_hint_y=None)
            element.text = n
            element.bind(on_release=lambda element: self.dropdown.select(element.text))
            self.dropdown.add_widget(element)


    def callback(self, instance, x):
        self.type = self.names[x]
        print(self.type)


class MediaFileChooser(BoxLayout):
    def __init__(self, **kwargs):
        super(MediaFileChooser, self).__init__(**kwargs)

        self.path = None
        self.popup = MediaFileChooserPopup()


    def callback(self, instance, x):
        self.path = self.names[x]
        print(self.path)


class MediaFileChooserPopup(Popup):
    pass


class MediaElementItem(BoxLayout):
    pass


class MediaList(BoxLayout):
    def __init__(self, **kwargs):
        super(MediaList, self).__init__(**kwargs)
        Clock.schedule_once(self.on_start, 0)


    def on_start(self, *args):
        self.ids.item_list.clear_widgets()

        for obj in media.get_all():
            elyt = MediaElementItem()
            elyt.ids.name.text = obj.name
            elyt.ids.type.text = obj.type
            elyt.ids.path.text = obj.path
            elyt.ids.description.text = obj.description
            self.ids.item_list.add_widget(elyt)


    def add(self):
        MediaAddPopup(self).open()


class MediaAddPopup(Popup):
    def __init__(self, master, **kwargs):
        super(MediaAddPopup, self).__init__(**kwargs)
        self.title = "Add new Media"
        self.master = master


    def add(self):
        name = self.ids.name_input.text.strip()
        type = self.ids.type_input.text.strip()
        path = self.ids.path_input.text.strip()
        description = self.ids.description_input.text.strip()
        media.Media(name=name, type=type, path=path, description=description).save()
        self.dismiss()
        self.master.on_start()
