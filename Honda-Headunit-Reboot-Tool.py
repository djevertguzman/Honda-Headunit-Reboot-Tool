# Tool to reboot 5th Gen Honda Odyssey Headunit by emulating a USB keyboard
import usb_hid
import time
import board
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)
print("Keyboard ARMED")
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
run = True
while run:
    # Wait for Headunit to enumerate USB device.
    print("Killing in 10 Sec")
    time.sleep(10)
    try:
        # Send control-alt-delete.
        kbd.send(Keycode.CONTROL, Keycode.LEFT_ALT, Keycode.DELETE)
        print("Murdered")
    except Exception as e:
        print(f"Error sending keys: {e}")
    finally:
        # Release all keys.
        kbd.release_all()
    
    # Prevent Headunit restarting over and over again.
    print("Now Killing Myself")
    run = False

# Turn on the LED and prevent the script from restarting
led.value = True
while True:
    pass  # Endless loop to keep LED on