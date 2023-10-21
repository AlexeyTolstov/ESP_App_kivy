from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from plyer import gps


class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout()
        self.label = Label(text="start")
        self.layout.add_widget(self.label)

    def on_start(self):
        gps.configure(on_location=self.on_gps_location)
        gps.start()

    def on_gps_location(self, **kwargs):
        print(kwargs)
        self.label.text = str(kwargs)

    def build(self):
        return self.layout


if __name__ == "__main__":
    MainApp().run()