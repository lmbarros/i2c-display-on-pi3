# I2C Display on balena Example

This is a simple and extensively commented example on how to use an I2C
peripheral connected to a Raspberry Pi 3 running on the
[balena](https://www.balena.io) platform. (Disclaimer: I work for balena.)

The concepts shall be the same regardless of which I2C peripheral you want to
use, but here I am using a little 128x64 pixels monochrome OLED display driven
by an SSD1306 chip. It's similar to [this Monochrome 0.96" 128x64 OLED Graphic
Display](https://www.adafruit.com/product/326) by Adafruit.

Anyway, go check the code. It's well-documented.

## Connections

A picture would definitely help here, but for now all I have is this:

| **Display Pin** | **Raspberry PI GPIO Pin Number** | **Raspberry PI GPIO Pin Description** |
|-----------------|----------------------------------|---------------------------------------|
| VCC             | 1                                | 3v3 Power                             |
| GND             | 6                                | Ground                                |
| SDA (Data)      | 3                                | GPIO 2 (I2C1 SDA)                     |
| SCL (Clock)     | 5                                | GPIO 2 (I2C1 SCL)                     |

Actually there's not much margin to be creative when connecting I2C peripherals
to a Pi, but you may want to check the [Raspberry Pi
Pinout](https://pinout.xyz/pinout/i2c#) website for some more info.

## Further experiments (left as exercise to the reader!)

### I2C Baud Rate

I was able to improve the refresh times of my display by increasing the I2C baud
rate. In a balena world, you simply need to set the config variable
`BALENA_HOST_CONFIG_dtparam` to `i2c_arm=on,i2c_baudrate=1000000`.

The magic is really done by `i2c_baudrate=1000000`, but you also need to add
`i2c_arm=on` to ensure I2C is enabled. balena will enable I2C by default, but
since we are manually changing the `dtparam`s, we have to explicitly set all the
values that matter for us. (This would be the same for other parameters that
balena sets by default, like `audio=on`).
