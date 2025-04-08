# MorseAdapter
A Pico based adapter for CW (Morse Code) keys

This is a super simple adapter for using a CW key with various software. The default configuration presses the space bar for use with various web, steam, and itch.io games as well as various training and practice software. 

Alternate key for key 1 is commented out for use with the website Vband. (https://hamradio.solutions/vband/) Key 2 is set up for the second contact on iambic style keys for Vband, though I do not currently have one available for testing.

To use this code your Pico must be configured to use CircuitPython. See https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython for instructions on setting it up. You will also need to copy the adafruit_hid CircuitPython library into the /lib/ folder on the Pico. Wiring is simple: I've used an aux cable, removed one end, and soldered the red and white wires to pins 0 and 1, and the third wire to ground.
