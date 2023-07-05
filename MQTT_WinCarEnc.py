from playsound import playsound
playsound(r'windows_8_startup.mp3')
import time
import paho.mqtt.client as mqtt
time.sleep(1)
print("Initializing GPIO pins.")
playsound(r'initializing.mp3')
from cryptography.fernet import Fernet
time.sleep(1)
print("Loading decryption key.")
playsound(r'decryption.mp3')



text = 0

def load_key():
    return open("secret.key", "rb").read()


def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

def on_message(client, userdata, message):
    global text
    string_message = str(message.payload.decode("utf-8"))
    byte_message = bytes(string_message, 'utf-8')
    dec_message = decrypt_message(byte_message)
    text = dec_message


broker_address="65.1.195.121"

client = mqtt.Client("P1")
client.username_pw_set(username="uname", password="pwd")
client.on_message=on_message
time.sleep(2)
client.connect(broker_address)
client.loop_start()
print("Connected to MQTT broker.")
playsound(r'connecting.mp3')
time.sleep(2)
client.subscribe("test")
print("Subscribed to topic.")
playsound(r'subs.mp3')
time.sleep(0.5)
print("Ready to drive")
playsound(r'ready.mp3')
playsound(r'beep-08b.mp3')
playsound(r'beep-08b.mp3')
while True:
    if text == "d":
        print("Destroy")
        text = 0
        # # Car.destroy()
    elif text == "f":
        print("Forward")
        text = 0
        # # Car.forward()
    elif text == "r":
        print("Reverse")
        text = 0
        # # Car.reverse()
    elif text == "tl":
        print("Turn Left")
        text = 0
        # # Car.turn_left()
    elif text == "tr":
        print("Turn Right")
        text = 0
        # # Car.turn_right()
    elif text == "s":
        print("Stop")
        text = 0
        # # Car.stop()
    elif text == "fl":
        print("Forward Left")
        text = 0
        # # Car.forward_left()
    elif text == "fr":
        print("Forward Right")
        text = 0
        # # Car.forward_right()
    elif text == "bl":
        print("Backward Left")
        text = 0
        # # Car.backward_left()
    elif text == "br":
        print("Backward Right")
        text = 0
        # # Car.backward_right()
    elif text == "s0":
        print("Speed 0")
        text = 0
        # Car.speed_zero()
    elif text == "s1":
        print("Speed 1")
        text = 0
        # Car.speed_one()
    elif text == "s2":
        print("Speed 2")
        text = 0
        # Car.speed_two()
    elif text == "s3":
        print("Speed 3")
        text = 0
        # Car.speed_three()
    elif text == "s4":
        print("Speed 4")
        text = 0
        # Car.speed_four()
    elif text == "s5":
        print("Speed 5")
        text = 0
        # Car.speed_five()
    elif text == "s6":
        print("Speed 6")
        text = 0
        # Car.speed_six()
    elif text == "s7":
        print("Speed 7")
        text = 0
        # Car.speed_seven()
    elif text == "s8":
        print("Speed 8")
        text = 0
        # Car.speed_eight()
    elif text == "s9":
        print("Speed 9")
        text = 0
        # Car.speed_nine()
    elif text == "s10":
        print("Speed 10")
        text = 0
        # Car.speed_ten()
    elif text == "bye":
        print("bye")
        text = 0
        # Car.destroy()
        break


client.loop_stop()