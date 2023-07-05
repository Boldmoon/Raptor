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
import serial
import RPi.GPIO as GPIO

ENABLE_PRINT = 0


class Car(object):
    in1 = 17
    in2 = 18
    in3 = 27
    in4 = 22
    enA = 12
    enB = 13
    lowPwm = 10
    highPwm = 80
    brzina = 0

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.setup(self.in4, GPIO.OUT)
        GPIO.setup(self.enA, GPIO.OUT)
        GPIO.setup(self.enB, GPIO.OUT)
        self.pwmLeft = GPIO.PWM(self.enA, 50)
        self.pwmRight = GPIO.PWM(self.enB, 50)
        self.pwmLeft.start(0)
        self.pwmRight.start(0)

    def destroy(self):
        if ENABLE_PRINT == 1:
            print("destroy")
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)
        GPIO.output(self.enA, GPIO.LOW)
        GPIO.output(self.enB, GPIO.LOW)
        GPIO.cleanup()

    def forward(self):
        if ENABLE_PRINT == 1:
            print("forward")
        self.pwmLeft.ChangeDutyCycle(self.brzina)
        self.pwmRight.ChangeDutyCycle(self.brzina)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)

    def reverse(self):
        if ENABLE_PRINT == 1:
            print("reverse")
        self.pwmLeft.ChangeDutyCycle(self.brzina)
        self.pwmRight.ChangeDutyCycle(self.brzina)
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)

    def turn_left(self):
        if ENABLE_PRINT == 1:
            print("turn_left")
        self.pwmLeft.ChangeDutyCycle(self.brzina)
        self.pwmRight.ChangeDutyCycle(0)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)

    def turn_right(self):
        if ENABLE_PRINT == 1:
            print("turn_right")
        self.pwmLeft.ChangeDutyCycle(0)
        self.pwmRight.ChangeDutyCycle(self.brzina)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)

    def stop(self):
        if ENABLE_PRINT == 1:
            print("stop")
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)

    def forward_left(self):
        if ENABLE_PRINT == 1:
            print("forward_left")
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)
        self.pwmLeft.ChangeDutyCycle(self.highPwm)
        self.pwmRight.ChangeDutyCycle(self.lowPwm)

    def forward_right(self):
        if ENABLE_PRINT == 1:
            print("forward_right")
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)
        self.pwmLeft.ChangeDutyCycle(self.lowPwm)
        self.pwmRight.ChangeDutyCycle(self.highPwm)

    def backward_left(self):
        if ENABLE_PRINT == 1:
            print("backward_left")
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)
        self.pwmLeft.ChangeDutyCycle(self.highPwm)
        self.pwmRight.ChangeDutyCycle(self.lowPwm)

    def backward_right(self):
        if ENABLE_PRINT == 1:
            print("backward_right")
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)
        self.pwmLeft.ChangeDutyCycle(self.lowPwm)
        self.pwmRight.ChangeDutyCycle(self.highPwm)

    def speed_zero(self):
        if ENABLE_PRINT == 1:
            print("speed_zero")
        self.brzina = 0

    def speed_one(self):
        if ENABLE_PRINT == 1:
            print("speed_one")
        self.brzina = 10

    def speed_two(self):
        if ENABLE_PRINT == 1:
            print("speed_two")
        self.brzina = 20

    def speed_three(self):
        if ENABLE_PRINT == 1:
            print("speed_three")
        self.brzina = 30

    def speed_four(self):
        if ENABLE_PRINT == 1:
            print("speed_four")
        self.brzina = 40

    def speed_five(self):
        if ENABLE_PRINT == 1:
            print("speed_five")
        self.brzina = 50

    def speed_six(self):
        if ENABLE_PRINT == 1:
            print("speed_six")
        self.brzina = 60

    def speed_seven(self):
        if ENABLE_PRINT == 1:
            print("speed_seven")
        self.brzina = 70

    def speed_eight(self):
        if ENABLE_PRINT == 1:
            print("speed_eight")
        self.brzina = 80

    def speed_nine(self):
        if ENABLE_PRINT == 1:
            print("speed_nine")
        self.brzina = 90

    def speed_ten(self):
        if ENABLE_PRINT == 1:
            print("speed_ten")
        self.brzina = 100


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
    print(dec_message)


broker_address = "65.1.195.121"

client = mqtt.Client("P1")
client.username_pw_set(username="uname", password="pwd")
client.on_message = on_message
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
        Car.destroy()
        text = 0
    elif text == "f":
        Car.forward()
        text = 0
    elif text == "r":
        Car.reverse()
        text = 0
    elif text == "tl":
        Car.turn_left()
        text = 0
    elif text == "tr":
        Car.turn_right()
        text = 0
    elif text == "s":
        Car.stop()
        text = 0
    elif text == "fl":
        Car.forward_left()
        text = 0
    elif text == "fr":
        Car.forward_right()
        text = 0
    elif text == "bl":
        Car.backward_left()
        text = 0
    elif text == "br":
        Car.backward_right()
        text = 0
    elif text == "s0":
        Car.speed_zero()
        text = 0
    elif text == "s1":
        Car.speed_one()
        text = 0
    elif text == "s2":
        Car.speed_two()
        text = 0
    elif text == "s3":
        Car.speed_three()
        text = 0
    elif text == "s4":
        Car.speed_four()
        text = 0
    elif text == "s5":
        Car.speed_five()
        text = 0
    elif text == "s6":
        Car.speed_six()
        text = 0
    elif text == "s7":
        Car.speed_seven()
        text = 0
    elif text == "s8":
        Car.speed_eight()
        text = 0
    elif text == "s9":
        Car.speed_nine()
        text = 0
    elif text == "s10":
        Car.speed_ten()
        text = 0
    elif text == "bye":
        Car.destroy()
        text = 0
        break

client.loop_stop()
