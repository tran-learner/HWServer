import os
import time

def delayed_shutdown(state:int):
    if (state == 1):
        os.system(f"sudo shutdown -h now")
    if (state == 2):
        os.system(f"sudo reboot now")