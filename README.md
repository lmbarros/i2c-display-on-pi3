# I2C Display Example

Using a display (based on the SSD1306 controller) on a balena device.

## Further experiments

### I2C Baud Rate

Set the config variable `BALENA_HOST_CONFIG_dtparam` to
`i2c_arm=on,i2c_baudrate=1000000` to increase the speed of the I2C communication
(and therefore make the display refresh more quickly).

Note that this overrides balena defaults, so we have to set `i2c_arm=on`
manually. You'd also need to explicitly set any other values that are set by
default (e.g., `audio=on` if you need to use audio).
