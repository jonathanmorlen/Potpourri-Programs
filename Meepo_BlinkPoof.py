import keyboard
import time

key_delay = 0.01    # delay between key presses
counter = 1         # number of meepos


def press(c):
    keyboard.press(c)
    keyboard.release(c)
    time.sleep(key_delay)


def detect(k):
    if keyboard.is_pressed(k):
        global counter
        counter = int([c for c in k][1])
        print(counter)
        time.sleep(0.5)


if __name__ == '__main__':
    while True:
        # change number of poofs for different number of meepos
        detect('f1')
        detect('f2')
        detect('f3')
        detect('f4')
        detect('f5')
        if keyboard.is_pressed('5'):
            for i in range(counter - 1):
                press('tab')  # switch meepo
                press('w')  # poof
            press('tab')
            press('space')  # ready blink
            time.sleep(0.5)
