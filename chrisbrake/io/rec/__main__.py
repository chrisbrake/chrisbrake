import datetime
import json
from pynput import keyboard

last_time = datetime.datetime.utcnow()


def build_event(key, kind):
    global last_time
    this_time = datetime.datetime.utcnow()
    delay = this_time - last_time
    last_time = this_time
    return {
        'delay': delay.total_seconds(),
        'key': key.__repr__(),
        'kind': kind
    }


def on_press(key):
    print(json.dumps(build_event(key, 'press')))


def on_release(key):
    print(json.dumps(build_event(key, 'release')))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def main():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()


if __name__ == '__main__':
    main()
