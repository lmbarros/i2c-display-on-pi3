import time
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(board.SCL, board.SDA)

oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)

# 1-bit image
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

while True:
    draw.rectangle([(0,0), (127,63)], fill=0)
    draw.text((4,4), "Hello", fill=255, font=font)
    oled.image(image)
    oled.show()
    time.sleep(1.5)

    # Subliminar message :-)
    draw.rectangle([(0,0), (127,63)], fill=0)
    draw.text((60,32), "balena!", fill=255, font=font)
    oled.image(image)
    oled.show()
    # time.sleep(0.1)

    draw.rectangle([(0,0), (127,63)], fill=255)
    draw.text((20,20), "World", fill=0, font=font)
    oled.image(image)
    oled.show()
    time.sleep(1.5)
