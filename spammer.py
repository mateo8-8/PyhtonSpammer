# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import time
import pyautogui

def SendMessage():
    time.sleep(4)
    # Open a text file contained in the same folder as your python file, "hulu.txt" happens to be the
    # name of the text file I have with my project
    text = open('spammer_text.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        #This is the part that delays the sending of messages, to make it annoying, decomment this and it'll send
        #a message every 0.10 seconds, I recommend the Shrek script or something similar to annoy fellow friends
        time.sleep(0.10)
        pyautogui.press('enter')

SendMessage()


