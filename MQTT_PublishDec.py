import paho.mqtt.client as mqtt
from cryptography.fernet import Fernet


def load_key():
    return open("secret.key", "rb").read()


def encrypt_message(message1):
    key = load_key()
    encoded_message = message1.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message


broker_address = "65.1.195.121"
print("Creating new instance")
client = mqtt.Client("P2")
client.username_pw_set(username="uname", password="pwd")
print("Connecting to broker")
client.connect(broker_address)
client.loop_start()
message = 0
# while True:
#     message = input("Enter message: ")
#     client.publish("test", message)
#     if message == "bye":
#         break

message = "bye"
client.publish("test", message)

client.loop_stop()
