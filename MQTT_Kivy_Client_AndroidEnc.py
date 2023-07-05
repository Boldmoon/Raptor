import paho.mqtt.client as mqtt
from cryptography.fernet import Fernet
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider


def load_key():
    return open("secret.key", "rb").read()


def encrypt_message(message1):
    key = load_key()
    encoded_message = message1.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message


Window.clearcolor = (1, 1, 1, 1)


class Main(App):
    client = mqtt.Client("P3")
    message = "0"
    text = 0
    textstr = "10"
    speedl2 = Label(text=textstr,
                    color=(1, 0, 0, 1),
                    font_size='25sp',
                    size_hint=(.4, .34))

    def on_message(self, client, userdata, message):
        data = message.payload.decode("utf-8").split(':')
        self.root.update(data[0], data[1], 1)

    def build(self):
        self.client.on_message = self.on_message
        self.client.username_pw_set(username="uname", password="pwd")
        self.client.connect('65.1.195.121', 1883)
        self.client.loop_start()
        self.client.publish("test", encrypt_message(self.message))
        layout = FloatLayout()
        speedl1 = Label(text=f'Speed',
                        color=(1, 0, 0, 1),
                        font_size='25sp',
                        size_hint=(.4, .45))
        speed = Slider(orientation='horizontal',
                       min=0,
                       max=10,
                       value=10,
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
        speed.bind(value=self.on_value)
        layout.add_widget(speed)
        layout.add_widget(speedl1)
        layout.add_widget(self.speedl2)
        layout.add_widget(reverse)
        layout.add_widget(stop)
        layout.add_widget(forward)
        layout.add_widget(left)
        layout.add_widget(right)
        return layout

    def on_stop(self):
        self.client.publish("test", "bye")

    def on_pause(self):
        self.client.disconnect()

    def on_resume(self):
        self.client.connect('65.1.195.121', 1883)

    def reverse(self, event):
        self.message = "r"
        encMessage = encrypt_message(self.message)
        self.client.publish("test", encMessage)

    def destroy(self, event):
        self.message = "s"
        encMessage = encrypt_message(self.message)
        self.client.publish("test", encMessage)

    def forward(self, event):
        self.message = "f"
        encMessage = encrypt_message(self.message)
        self.client.publish("test", encMessage)

    def left(self, event):
        self.message = "tl"
        encMessage = encrypt_message(self.message)
        self.client.publish("test", encMessage)

    def right(self, event):
        self.message = "tr"
        encMessage = encrypt_message(self.message)
        self.client.publish("test", encMessage)

    def on_value(self, instance, speed):
        self.text = speed
        self.text = float(self.text)
        self.text = round(self.text)
        self.textstr = str(self.text)
        self.speedl2.text = self.textstr
        if self.text == 0:
            self.message = "s0"
            encMessage = encrypt_message(self.message)
            self.client.publish("test", encMessage)
        elif self.text == 1:
            self.message = "s1"
            encMessage = encrypt_message(self.message)
            self.client.publish("test", encMessage)
        elif self.text == 2:
            self.message = "s2"
            encMessage = encrypt_message(self.message)
            self.client.publish("test", encMessage)
        elif self.text == 3:
            self.message = "s3"
            encMessage = encrypt_message(self.message)
            self.client.publish("test", encMessage)
        elif self.text == 4:
            self.message = "s4"
            encMessage = encrypt_message(self.message)
            self.client.publish("test", encMessage)
        elif self.text == 5:
            self.message = "s5"
            encMessage = encrypt_message(self.message)
            self.client.publish("test", encMessage)
        elif self.text == 6:
            self.message = "s6"
            encMessage = encrypt_message(self.message)
            self.client.publish("test", encMessage)
        elif self.text == 7:
            self.message = "s7"
            encMessage = encrypt_message(self.message)
            self.client.publish("test", encMessage)
        elif self.text == 8:
            self.message = "s8"
            encMessage = encrypt_message(self.message)
            self.client.publish("test", encMessage)
        elif self.text == 9:
            self.message = "s9"
            encMessage = encrypt_message(self.message)
            self.client.publish("test", encMessage)
        elif self.text == 10:
            self.message = "s10"
            encMessage = encrypt_message(self.message)
            self.client.publish("test", encMessage)


myApp = Main()
myApp.run()
