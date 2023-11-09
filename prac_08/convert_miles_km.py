"""Convert miles to kilometers kivy app. """

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesKmApp(App):
    """ ConvertMilesKMApp is a Kivy App for converting miles to kilometers """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 400)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesKmApp().run()
