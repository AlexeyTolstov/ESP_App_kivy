from requests import get

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

from kivy.clock import Clock


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = FloatLayout()
        self.isRun = False
        self.btn = Button(text="Start",
                          pos_hint={'center_x': 0.5,
                                    'center_y': 0.25},
                          size_hint=(0.2, 0.2))
        self.btn.bind(on_press=self.st_func)

        self.layout.add_widget(self.btn)

        self.label_dog = Label(text="",
                               pos_hint={'center_x': 0.75,
                                         'center_y': 0.9})
        self.label_person = Label(text="",
                                  pos_hint={'center_x': 0.75,
                                            'center_y': 0.7})

        self.layout.add_widget(self.label_dog)
        self.layout.add_widget(self.label_person)

        Clock.schedule_interval(self.update, 1)

    def st_func(self, instance):
        self.isRun = not self.isRun

        if self.isRun:
            instance.text = "Stop"
        else:
            instance.text = "Start"

    def update(self, _):
        if self.isRun:
            req = get("http://192.168.4.1/").json()
            self.label_dog.text = "Dog: " + str(req["Dog"]["x_coord"]) + " | " + str(req["Dog"]["y_coord"])
            self.label_person.text = "Person: " + str(req["Person"]["x_coord"]) + " | " + str(req["Person"]["y_coord"])
        else:
            pass

    def build(self):
        return self.layout


if __name__ == "__main__":
    MyApp().run()