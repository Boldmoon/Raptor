import paho.mqtt.client as mqtt
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.slider import Slider
from kivy.core.window import Window
from kivy.uix.label import Label
from playsound import playsound
Window.clearcolor = (1, 1, 1, 1)

class App(App):
    client = mqtt.Client("Winwo")
    message = 0
    text = 0
    textstr = "5"
    speedl2 = Label(text=textstr,
                    color=(1, 0, 0, 1),
                    font_size='25sp',
                    size_hint=(.4, .34))
    def on_message(self, client, userdata, message):
        data = message.payload.decode("utf-8").split(':')

        self.root.update(data[0], data[1], 1)

    def sound(self, name):
        if name == "r":
            playsound('Assests/Rev.mp3')

    def build(self):
        self.icon = 'RaptorIcon.png'
        self.client.on_message = self.on_message
        self.client.username_pw_set(username="uname", password="pwd")
        self.client.connect('proxima.boldmoon.in', 1883)
        self.client.loop_start()
        layout = FloatLayout()
        speedl1 = Label(text=f'Speed',
                       color=(1, 0, 0, 1),
                       font_size='25sp',
                       size_hint=(.4, .45))
        speed = Slider(orientation='horizontal',
                       min=1,
                       max=5,
                       value=5,
                       size_hint=(.3, .3),
                       value_track=True,
                       value_track_color=[1, 0, 0, 1],
                       pos_hint={'x': .05, 'y': .13})
        reverse = Button(text="Reverse",
                     font_size="20sp",
                     background_color=(0.059, 0.969, 0.961),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.28, .28),
                     pos_hint={'x': .36, 'y': .12})
        brea = Button(text="Stop",
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
        destroy = Button(text="Off",
                         font_size="20sp",
                         background_color=(0.059, 0.969, 0.961),
                         color=(1, 1, 1, 1),
                         size=(32, 32),
                         size_hint=(.10, .10),
                         pos_hint={'x': .08, 'y': .85})
        honk = Button(text="Honk",
                         font_size="20sp",
                         background_color=(0.059, 0.969, 0.961),
                         color=(1, 1, 1, 1),
                         size=(32, 32),
                         size_hint=(.10, .10),
                         pos_hint={'x': .2, 'y': .85})
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
        brea.bind(on_press=self.brea)
        forward.bind(on_press=self.forward)
        left.bind(on_press=self.left)
        right.bind(on_press=self.right)
        honk.bind(on_press=self.honk)
        destroy.bind(on_press=self.destroy)
        speed.bind(value=self.on_value)
        layout.add_widget(speed)
        layout.add_widget(speedl1)
        layout.add_widget(self.speedl2)
        layout.add_widget(reverse)
        layout.add_widget(brea)
        layout.add_widget(forward)
        layout.add_widget(left)
        layout.add_widget(right)
        layout.add_widget(destroy)
        layout.add_widget(honk)
        return layout

    def on_pause(self):
        self.client.disconnect()
    def reverse(self, event):
        self.message = "r"
        self.sound("r")
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
    def destroy(self, event):
        self.message = "d"
        self.client.publish("V3", self.message)
    def brea(self, event):
        self.message = "s"
        self.client.publish("V3", self.message)
    def honk(self, event):
        self.message = "h"
        self.client.publish("V3", self.message)
    def on_value(self, instance, speed):
        self.text = speed
        self.text = float(self.text)
        self.text = round(self.text)
        self.textstr = str(self.text)
        self.speedl2.text = self.textstr
        if self.text == 1:
            self.message = "s1"
            self.client.publish("V3", self.message)
        elif self.text == 2:
            self.message = "s2"
            self.client.publish("V3", self.message)
        elif self.text == 3:
            self.message = "s3"
            self.client.publish("V3", self.message)
        elif self.text == 4:
            self.message = "s4"
            self.client.publish("V3", self.message)
        elif self.text == 5:
            self.message = "s5"
            self.client.publish("V3", self.message)


App().run()
