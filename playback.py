import pyautogui
import cv2
import numpy as np
from time import sleep, time
import os
import json
import threading

Stop_recording = False
file = "actions_test_10-07-2020_15-56-43.json"

def main():

    initializePyAutoGUI()
    countdownTimer()
    t1 = threading.Thread(target=playActions, args=[file])
    t2 = threading.Thread(target=recordScreen)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done")


def recordScreen():
    output = "video.avi"
    img = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    # get info from img
    height, width, channels = img.shape
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output, fourcc, 100.0, (width, height))

    while not Stop_recording:
        try:
            img = pyautogui.screenshot()
            image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            out.write(image)
            StopIteration(0.5)
        except KeyboardInterrupt:
            break

    out.release()
    cv2.destroyAllWindows()

def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = False


def countdownTimer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 3):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")

def playActions(filename):
    # Read the file
    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, 'recordings', filename)
    with open(filepath, 'r') as jsonfile:
        # parse the json
        data = json.load(jsonfile)
        # loop over each action
        # Because we are not waiting any time before executing the first action, any delay before the initial
        # action is recorded will not be reflected in the playback.
        for index, action in enumerate(data):
            action_start_time = time()
            # look for escape input to exit
            if action['button'] == 'Key.esc':
                break
            # perform the action
            if action['type'] == 'keyDown':
                key = convertKey(action['button'])
                pyautogui.keyDown(key)
                print("keyDown on {}".format(key))
            elif action['type'] == 'keyUp':
                key = convertKey(action['button'])
                pyautogui.keyUp(key)
                print("keyUp on {}".format(key))
            elif action['type'] == 'click' and action['button'] == "Button.right":
                pyautogui.rightClick(action['pos'][0], action['pos'][1], duration=0.25)
                print("right click on {}".format(action['pos']))
            elif action['type'] == 'click' and action['button'] == "Button.left":
                # Check if the period between clicks is short and perform a double click then, otherwise
                # it performs a single click
                if index > 0:
                    if (data[index]['time']) - (data[index - 1]['time']) < 0.5:
                        pyautogui.doubleClick(action['pos'][0], action['pos'][1])
                        print("Double click on {}".format(action['pos']))
                pyautogui.leftClick(action['pos'][0], action['pos'][1], duration=0.25)
                print("left click on {}".format(action['pos']))

            # then sleep until next action should occur
            try:
                next_action = data[index + 1]
            except IndexError:
                # this was the last action in the list
                break
            elapsed_time = next_action['time'] - action['time']

            # if elapsed_time is negative, that means our actions are not ordered correctly. throw an error
            if elapsed_time < 0:
                raise Exception('Unexpected action ordering.')

            # adjust elapsed_time to account for our code taking time to run
            elapsed_time -= (time() - action_start_time)
            if elapsed_time < 0:
                elapsed_time = 0
            print('sleeping for {}'.format(elapsed_time))
            sleep(elapsed_time)
            STOP_RECORDING = True
    global Stop_recording
    Stop_recording = True


# convert pynput button keys into pyautogui keys
# https://pynput.readthedocs.io/en/latest/_modules/pynput/keyboard/_base.html#Key
# https://pyautogui.readthedocs.io/en/latest/keyboard.html
def convertKey(button):
    PYNPUT_SPECIAL_CASE_MAP = {
        'alt_l': 'altleft',
        'alt_r': 'altright',
        'alt_gr': 'altright',
        'caps_lock': 'capslock',
        'ctrl_l': 'ctrlleft',
        'ctrl_r': 'ctrlright',
        'page_down': 'pagedown',
        'page_up': 'pageup',
        'shift_l': 'shiftleft',
        'shift_r': 'shiftright',
        'num_lock': 'numlock',
        'print_screen': 'printscreen',
        'scroll_lock': 'scrolllock',
    }
    # example: 'Key.F9' should return 'F9', 'w' should return as 'w'
    cleaned_key = button.replace('Key.', '')

    if cleaned_key in PYNPUT_SPECIAL_CASE_MAP:
        return PYNPUT_SPECIAL_CASE_MAP[cleaned_key]

    return cleaned_key


if __name__ == "__main__":
    main()
