# import kivy module
import kivy

# this restricts the kivy version i.e
# below this kivy version you cannot use the app or software
kivy.require("1.9.1")

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# if you not import label and use it it through error
from kivy.uix.label import Label


# defining the App class
class MyLabelApp(App):
    def build(self):
        # label display the text on screen
        lbl = Label(text="Label is Added on screen !!:):)")
        return lbl


# creating the object
label = MyLabelApp()
# run the window
label.run()