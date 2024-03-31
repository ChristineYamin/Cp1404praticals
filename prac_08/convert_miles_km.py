from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMile(App):
    """MilesConverterApp is a Kivy App for converting miles into kilometres"""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle calculation (could be button press or other call)."""
        miles = float(self.root.ids.input_miles.text)
        result = miles * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Handle up and down button press, add the increment to the text input, call calculation function."""
        miles = float(self.root.ids.input_miles.text) + change
        self.handle_calculate()
        self.root.ids.input_miles.text = str(miles)

ConvertMile().run()