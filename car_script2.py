import RPi. GPIO as gpio
import time
import sys
import tkinter as tk

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(11,gpio.OUT)
    gpio.setup(15,gpio.OUT)
    gpio.setup(16,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.setup(19,gpio.OUT)
    gpio.setup(21,gpio.OUT)
    gpio.setup(23,gpio.OUT)
    gpio.setup(24,gpio.OUT)
    a=gpio.PWM(19,100)
    b=gpio.PWM(21,100)
    c=gpio.PWM(23,100)
    d=gpio.PWM(24,100)
    a.start(30)
    b.start(30)
    c.start(30)
    d.start(30)
    
def forward(tf):
    gpio.output(11, False)
    gpio.output(15, True)
    gpio.output(16, True)
    gpio.output(18, False)
    time.sleep(tf)
    gpio.cleanup()
    
def reverse(tf):
    gpio.output(11, True)
    gpio.output(15, False)
    gpio.output(16, False)
    gpio.output(18, True)
    time.sleep(tf)
    gpio.cleanup()
    
def turn_left(tf):
    gpio.output(11, True)
    gpio.output(15, True)
    gpio.output(16, True)
    gpio.output(18, False)
    time.sleep(tf)
    gpio.cleanup()
    
def turn_right(tf):
    gpio.output(11, False)
    gpio.output(15, True)
    gpio.output(16, False)
    gpio.output(18, False)
    time.sleep(tf)
    gpio.cleanup()
    
def pivot_left(tf):
    gpio.output(11, True)
    gpio.output(15, False)
    gpio.output(16, True)
    gpio.output(18, False)
    time.sleep(tf)
    gpio.cleanup()
    
def pivot_right(tf):
    gpio.output(11, False)
    gpio.output(15, True)
    gpio.output(16, False)
    gpio.output(18, True)
    time.sleep(tf)
    gpio.cleanup()
    
def key_input(event):
    init()
    print ('Key:', event.char)
    key_press = event.char
    sleep_time = 0.050
    
    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        reverse(sleep_time)
    elif key_press.lower() == 'a':
        turn_left(sleep_time)
    elif key_press.lower() == 'd':
        turn_right(sleep_time)
    elif key_press.lower() == 'q':
        pivot_left(sleep_time)
    elif key_press.lower() == 'e':
        pivot_right(sleep_time)
        
command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
        
    
    


