import os
import time

def delayed_shutdown(state:int):
    if (state == 1):
        os.system(f"sudo shutdown -h + 0")
    if (state == 2):
        os.system(f"sudo shutdown -r + 0")