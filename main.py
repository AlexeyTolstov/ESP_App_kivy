import requests

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

# while True:
#     n = int(input())
#     if n:
#         requests.get("http://192.168.0.34/?value=1")
#     else:
#         requests.get("http://192.168.0.34/?value=0")


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = FloatLayout()

        self.isOn = False
        Window.clearcolor = (.0, .0, .0, 1)
        self.btn = Button(text="On",
                          pos_hint={'center_x': 0.5,
                                    'center_y': 0.5},
                          size_hint=(0.2, 0.2))
        self.btn.bind(on_press=self.light)
        self.layout.add_widget(self.btn)

    def light(self, _):
        if self.isOn:
            requests.get("http://192.168.0.34/?value=0")
            self.btn.text = "On"
            self.isOn = False
            Window.clearcolor = (.0, .0, .0, 1)
        else:
            requests.get("http://192.168.0.34/?value=1")
            self.btn.text = "Off"
            self.isOn = True
            Window.clearcolor = (1, 1, 1, 1)

    def build(self):
        return self.layout


if __name__ == "__main__":
    MyApp().run()