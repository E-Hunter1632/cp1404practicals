"""Basic dynamic widgets app"""

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Main dynamic labels program."""

    def __init__(self, **kwargs):
        """Initialise the app"""
        super().__init__(**kwargs)
        # List of names (strings) to create labels from.
        self.names = ["Eric", "Bob", "Dave", "Someone", "Another"]

    def build(self):
        """Build the GUI. """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create the widgets. """
        for name in self.names:
            # create temp label per entry
            temp_label = Label(text=name)


DynamicLabelsApp().run()
