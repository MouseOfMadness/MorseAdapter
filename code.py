#Morse Adapter by Mouse of Madness
#for raspberry pi pico and circuit python
import board
import digitalio
import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)


#solder headphone cable or socket to pins. White 0, Red 1, and ground.
key_one_pin = board.GP1       # pin to connect button to
key_two_pin = board.GP0       #oops, swapped wiring issue, change depending on your own wiring

# Initializing Button
key_one = digitalio.DigitalInOut(key_one_pin)
key_one.direction = digitalio.Direction.INPUT
key_one.pull = digitalio.Pull.UP

key_two = digitalio.DigitalInOut(key_two_pin)
key_two.direction = digitalio.Direction.INPUT
key_two.pull = digitalio.Pull.UP

pressed1 = False
pressed2 = False

while True:
    #for list of keys to press
    #https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/adafruit_hid/keycode.py
    if key_one.value == True:
        if pressed1 == True:
            pressed1 = False
            print("Key1 Released")
            #keyboard.release(Keycode.LEFT_BRACKET) #for vband and iambic
            keyboard.release(Keycode.SPACEBAR) #for general software, games, etc.
    else:
        if pressed1 == False:    
            pressed1 = True
            print("Key1 Pressed")
            #keyboard.press(Keycode.LEFT_BRACKET)
            keyboard.press(Keycode.SPACEBAR)
            time.sleep(0.01)
            
    if key_two.value == True:
        if pressed2 == True:
            pressed2 = False
            print("Key2 Released")
            keyboard.release(Keycode.RIGHT_BRACKET) #for vband and iambic
    else:
        if pressed2 == False:    
            pressed2 = True
            print("Key2 Pressed")
            keyboard.press(Keycode.RIGHT_BRACKET)
            time.sleep(0.01)
