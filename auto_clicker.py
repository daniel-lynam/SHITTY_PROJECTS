import pyautogui
import time
import keyboard
# Settings
click_interval = 0.03  # Time between clicks in seconds
run_time = 1000         # Total runtime in seconds

print("Auto clicker will start in 3 seconds. Move your mouse to the desired position.")
time.sleep(3)

start_time = time.time()
try:
    while time.time() - start_time < run_time:
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('q'):  # if key 'q' is pressed
                break  # finishing the loop
        except:
            break  # if user pressed a key other than the given key the loop will break
        pyautogui.click()  # Simulates a mouse click
        time.sleep(click_interval)
except KeyboardInterrupt:
    print("Auto clicker stopped manually.")
finally:
    print("Auto clicker finished.")
