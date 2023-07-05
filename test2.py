from pynput import keyboard
cmd = 0
def press_callback(key):
    global cmd
    cmd = key

def release_callback(key):
    global cmd
    cmd = key

l = keyboard.Listener(on_press=press_callback,on_release=release_callback)
l.start()

while True:
    print(cmd)