import time
import board
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# Create the object representing our 128x64 OLED display. It is connected to the
# Raspberry Pi using the default I2C pins, so we can simply use `board.I2C()` to
# refer to them. I am explicitly passing the I2C address of my device (0x3c)
# because I am not sure what is the default used by the Adafruit library.
#
# Telling which GPIO pins are used and what is the address of the display is the
# closest we'll get to I2C. The actual work of using the I2C protocol to send
# commands to the display is abstracted by the Adafruit library. Other
# peripherals will typically (or hopefully!) have their own specific libraries.
#
# And I am using hardcoded values for things like display resolution because I
# want to keep the example as simple as possible. The average real-world
# application would benefit from some "best practices" of programming.
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, board.I2C(), addr=0x3c)

# Here we create an image the same size as our display. We'll make all drawing
# to this image and then blit (draw) it at once to the display.
#
# That funny "1" is the way to tell that this is a monochrome (1 bit per pixel)
# image.
image = Image.new("1", (128, 64))

# This is an object that is capable of drawing things on the image we just
# created.
draw = ImageDraw.Draw(image)

# And this is the font we'll used to write some text into the display.
font = ImageFont.load_default()

# Nothing like an infinite loop :-)
while True:
    # We first draw a rectangle filling the whole screen. The `fill=0` means
    # that each pixel of the rectangle will have the value 0 (that is, black).
    draw.rectangle([(0,0), (127,63)], fill=0)

    # Now write a message to the image, now using `fill=255`, i.e., white (or
    # whatever color your display is -- mine is actually blue).
    draw.text((4,4), "Hello", fill=255, font=font)

    # Copy the image data to the display, and update (`show()`) the display.
    oled.image(image)
    oled.show()

    # Leave the display alone for 1.5s to allow the user to read the message.
    time.sleep(1.5)

    # Same as above, but without the sleep. Just a basic subliminal message :-P
    draw.rectangle([(0,0), (127,63)], fill=0)
    draw.text((60,32), "balena!", fill=255, font=font)
    oled.image(image)
    oled.show()

    # And the second part of the proper "Hello World" message, now in with a
    # black text on white background.
    draw.rectangle([(0,0), (127,63)], fill=255)
    draw.text((20,20), "World", fill=0, font=font)
    oled.image(image)
    oled.show()
    time.sleep(1.5)
