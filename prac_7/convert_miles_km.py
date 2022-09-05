from kivy.app import App
from kivy.lang import Builder


MILES_TO_KM = 1.60934


class MilesConvertApp(App):
    """Create a class called MilesConvertApp"""
    def build(self):
        """Build Kivy app form kv file"""
        self.title = "Convert APP"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handel_problem(self):
        """Calculation mile to KM"""
        values = self.get_valid_miles()
        result = values * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def add_changes(self, changes):
        """Make up and down button work"""
        values = self.get_valid_miles() + changes
        self.root.ids.input_miles.text = str(values)

    def get_valid_miles(self):
        """Get a valid input number"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConvertApp().run()
