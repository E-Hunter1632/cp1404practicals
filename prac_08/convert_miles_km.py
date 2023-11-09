"""Convert miles to kilometers kivy app. """

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class ConvertMilesKmApp(App):
    """ ConvertMilesKMApp is a Kivy App for converting miles to kilometers """
    result_label = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 400)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.result_label = "Type Miles in field, then press convert to see Kilometers. "
        return self.root

    def handle_increment(self, increment):
        """Handle the increment Up and Down buttons. """
        pass

    def convert_miles_km(self, value):
        """Do the calculation from miles to kilometers. """
        try:
            result = float(value) * 1.609
            self.root.ids.result_label.text = str(result)
        except ValueError:
            pass


ConvertMilesKmApp().run()
