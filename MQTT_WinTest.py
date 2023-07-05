import paho.mqtt.client as mqtt
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.slider import Slider
from kivy.core.window import Window
from kivy.uix.label import Label
Window.clearcolor = (1, 1, 1, 1)

class App(App):
    client = mqtt.Client("UV3")
    message = 0
    text = 0
    def on_message(self, client, userdata, message):
        data = message.payload.decode("utf-8").split(':')

        self.root.update(data[0], data[1], 1)


    def build(self):
        self.icon = 'eagle.png'
        self.client.on_message = self.on_message
        self.client.username_pw_set(username="uname", password="pwd")
        self.client.connect('proxima.boldmoon.in', 1883)
        self.client.loop_start()
        layout = FloatLayout()
        reverse = Button(text="Reverse",
                     font_size="20sp",
                     background_color=(0.059, 0.969, 0.961),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.28, .28),
                     pos_hint={'x': .36, 'y': .12})
        stop = Button(text="Stop",
                      font_size="20sp",
                      background_color=(0.059, 0.969, 0.961),
                      color=(1, 1, 1, 1),
                      size=(32, 32),
                      size_hint=(.28, .28),
                      pos_hint={'x': .36, 'y': .40})
        forward = Button(text="Forward",
                         font_size="20sp",
                         background_color=(0.059, 0.969, 0.961),
                         color=(1, 1, 1, 1),
                         size=(32, 32),
                         size_hint=(.28, .28),
                         pos_hint={'x': .36, 'y': .68})
        left = Button(text="Left",
                      font_size="20sp",
                      background_color=(0.059, 0.969, 0.961),
                      color=(1, 1, 1, 1),
                      size=(32, 32),
                      size_hint=(.28, .28),
                      pos_hint={'x': .08, 'y': .40})
        right = Button(text="Right",
                      font_size="20sp",
                      background_color=(0.059, 0.969, 0.961),
                      color=(1, 1, 1, 1),
                      size=(32, 32),
                      size_hint=(.28, .28),
                      pos_hint={'x': .64, 'y': .40})
        reverse.bind(on_press=self.reverse)
        stop.bind(on_press=self.destroy)
        forward.bind(on_press=self.forward)
        left.bind(on_press=self.left)
        right.bind(on_press=self.right)



        layout.add_widget(reverse)
        layout.add_widget(stop)
        layout.add_widget(forward)
        layout.add_widget(left)
        layout.add_widget(right)
        return layout

    def on_pause(self):
        self.client.disconnect()
    def reverse(self, event):
        self.message = "r"
        self.client.publish("V3", self.message)
    def destroy(self, event):
        self.message = "s"
        self.client.publish("V3", self.message)
    def forward(self, event):
        self.message = "f"
        self.client.publish("V3", self.message)
    def left(self, event):
        self.message = "tl"
        self.client.publish("V3", self.message)
    def right(self, event):
        self.message = "tr"
        self.client.publish("V3", self.message)


App().run()
