import kivy
from kivy.app import App
from kivy.uix.dropdown  import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy. uix . button  import Button


class CustomDropDown(DropDown):
    pass


class DropdownDemo(FloatLayout):
    def __init__(self, **kwargs):
        super(DropdownDemo, self).__init__(**kwargs)
        self.dropdown = CustomDropDown()

        self.mainbutton = Button(text ='Do you in college?', size_hint_x = 0.6, size_hint_y = 0.15)
        self.add_widget(self.mainbutton)
        self.mainbutton.bind(on_release = self.dropdown.open)

        self.dropdown.bind(on_select = lambda instance, x: setattr(self.mainbutton, 'text', x))
        self.dropdown.bind(on_select = self.callback)

    def callback(self, instance, x):
        print ( "The chosen mode is: {0}" . format ( x ) )


class Try(App):
    def build(self):
        return DropdownDemo()


if __name__ == '__main__':
    Try().run()