import paho.mqtt.client as mqtt
import threading
import keyboard
import time

message = "holder1"
text = "holder2"
cmd = "holder3"
killer1 = True

client = mqtt.Client("Winwo2")
client.username_pw_set(username="uname", password="pwd")
client.connect('proxima.boldmoon.in', 1883)
client.loop_start()


def on_pause():
    global client
    client.disconnect()


def reverse():
    global message, client
    message = "r"
    client.publish("V3", message)


def forward():
    global message, client
    message = "f"
    client.publish("V3", message)


def left():
    global message, client
    message = "tl"
    client.publish("V3", message)


def right():
    global message, client
    message = "tr"
    client.publish("V3", message)


def destroy():
    global message, client
    message = "d"
    client.publish("V3", message)


def brea():
    global message, client
    message = "s"
    client.publish("V3", message)


def honk():
    global message, client
    message = "h"
    client.publish("V3", message)


def on_value(speed):
    global message, client, text
    text = speed
    if text == 1:
        message = "s1"
        client.publish("V3", message)
    elif text == 2:
        message = "s2"
        client.publish("V3", message)
    elif text == 3:
        message = "s3"
        client.publish("V3", message)
    elif text == 4:
        message = "s4"
        client.publish("V3", message)
    elif text == 5:
        message = "s5"
        client.publish("V3", message)


