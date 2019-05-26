import Rpi.GPIO as gpio
import sys
import time
gpio.setwarnings(False)

def init():

gpio.setmode(gpio.BOARD)

gpio.setup(11, gpio.OUT)

gpio.setup(15, gpio.OUT)

gpio.setup(16, gpio.OUT)

gpio.setup(18, gpio.OUT)



def forward(tf):

init()

gpio.output (11, False)

gpio.output (15, True)

gpio.output (16, True)

gpio.output (18, False)

time.sleep(tf) 

gpio.cleanup()

def reverse(tf):

init()

gpio.output (11, True)

gpio.output (15, False)

gpio.output (16, False)

gpio.output (18, True)

time.sleep(tf)

gpio.cleanup()

def left(tf):

init() 

gpio.output (11, False)

gpio.output (15, False)

gpio.output (16, False)

gpio.output (18, True)

time.sleep(tf)

gpio.cleanup()

def right(tf):

init()

gpio.output (11, True)

gpio.output (15, False)

gpio.output (16, True)

gpio.output (18, True)

time.sleep(tf)

gpio.cleanup()

def pivotleft(tf):

init()

gpio.output (11, False)

gpio.output (15, True)

gpio.output (16, False)

gpio.output (18, True)

time.sleep(tf)

gpio.cleanup()

def pivotright(tf):

init()

gpio.output (11, True)

gpio.output (15, False)

gpio.output (16, True)

gpio.output (18, False)

time.sleep(tf)

gpio.cleanup()


print("going forward")
forward(2)
print("going backward")
reverse(2)


