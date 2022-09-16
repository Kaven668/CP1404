from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_to_age = {"Tom": "24", "Jack": "23", "Bob": "12", "alexander": "32"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create the widgets"""
        for name in self.name_to_age:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """Press the entry"""
        name = instance.text
        self.status_text = f"{name}'s number is {self.name_to_age[name]} years old."

    def clear_all(self):
        """Clearn all information"""
        self.root.ids.entries_box.clear_widgets()
        self.status_text = ''
    def add_a_new(self):
        self.status_text = self.root.ids.user_input.text
        new_tab= Button(text=self.status_text)
        new_tab.bind(on_release =self.press_entry_2)
        self.root.ids.entries_box.add_widget(new_tab)
        self.clear_filed()

    def press_entry_2(self,instance):
        input1 = instance.text
        self.status_text = f"{input1}"



    def clear_filed(self):

        self.root.ids.user_input.text = ""





DynamicWidgetsApp().run()