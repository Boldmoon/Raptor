import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import threading

time.sleep(1)
ENABLE_PRINT = 1
in1 = 17
in2 = 18
in3 = 27
in4 = 22
bled = 10
buzz = 23
rled1 = 25
rled2 = 24
ena = 13
enb = 12
pwm1 = 20
pwm2 = 40
pwm3 = 60
pwm4 = 80
pwm5 = 100
speedpwm = 100
print("Initializing GPIO pins.")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ena, GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

p1 = GPIO.PWM(ena, 1000)
p2 = GPIO.PWM(enb, 1000)
p1.start(pwm3)
p2.start(pwm3)
GPIO.setup(bled, GPIO.OUT)
GPIO.setup(buzz, GPIO.OUT)
GPIO.setup(rled1, GPIO.OUT)
GPIO.setup(rled2, GPIO.OUT)
GPIO.output(buzz, GPIO.HIGH)
GPIO.output(bled, GPIO.HIGH)
GPIO.output(rled1, GPIO.HIGH)
GPIO.output(rled2, GPIO.HIGH)
time.sleep(0.5)
GPIO.output(buzz, GPIO.LOW)
GPIO.output(bled, GPIO.LOW)
GPIO.output(rled1, GPIO.LOW)
GPIO.output(rled2, GPIO.LOW)


def destroy():
    print("\ndestroy")
    GPIO.output(ena, GPIO.LOW)
    GPIO.output(enb, GPIO.LOW)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(rled2, GPIO.LOW)
    GPIO.output(rled1, GPIO.LOW)
    GPIO.output(buzz, GPIO.HIGH)
    GPIO.output(rled2, GPIO.HIGH)
    GPIO.output(rled1, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(buzz, GPIO.LOW)
    GPIO.output(rled2, GPIO.LOW)
    GPIO.output(rled1, GPIO.LOW)
    GPIO.cleanup()


def forward():
    print("\nforward")
    p1.ChangeDutyCycle(speedpwm)
    p2.ChangeDutyCycle(speedpwm)
    GPIO.output(rled2, GPIO.LOW)
    GPIO.output(rled1, GPIO.LOW)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)


def reverse():
    print("\nreverse")
    p1.ChangeDutyCycle(speedpwm)
    p2.ChangeDutyCycle(speedpwm)
    GPIO.output(rled2, GPIO.LOW)
    GPIO.output(rled1, GPIO.LOW)
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)


def turn_left():
    print("\nturn_left")
    p1.ChangeDutyCycle(speedpwm)
    p2.ChangeDutyCycle(speedpwm)
    GPIO.output(rled1, GPIO.LOW)
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    GPIO.output(rled2, GPIO.HIGH)


def turn_right():
    print("\nturn_right")
    p2.ChangeDutyCycle(speedpwm)
    p1.ChangeDutyCycle(speedpwm)
    GPIO.output(rled2, GPIO.LOW)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(rled1, GPIO.HIGH)


def stop():
    print("\nstop")
    GPIO.output(rled2, GPIO.LOW)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(rled1, GPIO.LOW)


def honk():
    print("\nhonk")
    GPIO.output(buzz, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(buzz, GPIO.LOW)


def speed_one():
    global speedpwm
    global pwm1
    print("\nspeed_one")
    speedpwm = pwm1


def speed_two():
    global speedpwm
    global pwm2
    print("\nspeed_two")
    speedpwm = pwm2


def speed_three():
    global speedpwm
    global pwm3
    print("\nspeed_three")
    speedpwm = pwm3


def speed_four():
    global speedpwm
    global pwm4
    print("\nspeed_three")
    speedpwm = pwm4


def speed_five():
    global speedpwm
    global pwm5
    print("\nspeed_three")
    speedpwm = pwm5

def speed_changer(pcmd, scmd):
    if pcmd == "f":
        scmd()
        forward()
    elif pcmd == "r":
        scmd()
        reverse()
    elif pcmd == "tl":
        scmd()
        turn_left()
    elif pcmd == "tr":
        scmd()
        turn_right()
    elif pcmd == "s":
        scmd()
        stop()



text = 0


def on_message(client, userdata, message):
    global text
    string_message = str(message.payload.decode("utf-8"))
    text = string_message
    print(text)


broker_address = "proxima.boldmoon.in"
client = mqtt.Client("RV3")
client.username_pw_set(username="uname", password="pwd")
client.on_message = on_message
time.sleep(0.5)
client.connect(broker_address)
client.loop_start()
print("Connected to Server.")

time.sleep(0.5)
client.subscribe("V3")
time.sleep(0.5)
print("Ready to drive")
GPIO.output(buzz, GPIO.HIGH)
GPIO.output(rled2, GPIO.HIGH)
GPIO.output(rled1, GPIO.HIGH)
time.sleep(0.2)
GPIO.output(buzz, GPIO.LOW)
GPIO.output(rled2, GPIO.LOW)
GPIO.output(rled1, GPIO.LOW)
time.sleep(0.2)
GPIO.output(buzz, GPIO.HIGH)
GPIO.output(rled2, GPIO.HIGH)
GPIO.output(rled1, GPIO.HIGH)
time.sleep(0.2)
GPIO.output(buzz, GPIO.LOW)
GPIO.output(rled2, GPIO.LOW)
GPIO.output(rled1, GPIO.LOW)
prevcmd = "s"

while True:
    if text == "h":
        h1 = threading.Thread(target=honk)
        h1.start()
        text = 0
    elif text == "f":
        forward()
        prevcmd = "f"
        text = 0
    elif text == "r":
        reverse()
        prevcmd = "r"
        text = 0
    elif text == "tl":
        stop()
        turn_left()
        prevcmd = "tl"
        text = 0
    elif text == "tr":
        stop()
        turn_right()
        prevcmd = "tr"
        text = 0
    elif text == "s":
        stop()
        prevcmd = "s"
        text = 0
    elif text == "s1":
        speed_changer(prevcmd, speed_one)
        text = 0
    elif text == "s2":
        speed_changer(prevcmd, speed_two)
        text = 0
    elif text == "s3":
        speed_changer(prevcmd, speed_three)
        text = 0
    elif text == "s4":
        speed_changer(prevcmd, speed_four)
        text = 0
    elif text == "s5":
        speed_changer(prevcmd, speed_five)
        text = 0
    elif text == "d":
        destroy()
        text = 0
        break
print("Bye")
client.loop_stop()

