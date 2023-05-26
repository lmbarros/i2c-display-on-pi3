# I2C Display Example

Using a display (based on the SSD1306 controller) on a balena device.

## Doubts

**Why don't we need to run in privileged mode, nor any capabilities?** Maybe
because when we "share" a device with the container we get full access to the
device (and in this case at least, we don't need to do anything low-level that
is not via the device)? See a fragment of `balena inspect` on the container:

```json
"Devices": [
    {
        "PathOnHost": "/dev/i2c-1",
        "PathInContainer": "/dev/i2c-1",
        "CgroupPermissions": "rwm"
    }
],
```

**Why don't we need to load the i2c-dev kernel module manually? Who loads it?**
Apparently it is loaded during boot... perhaps by the kernel itself when it sees
that there is an i2c controller available? Not sure that's how things work
(feels there's some piece I am missing).

## Further experiments (left as exercise to the reader!)

### I2C Baud Rate

Set the config variable `BALENA_HOST_CONFIG_dtparam` to
`i2c_arm=on,i2c_baudrate=1000000` to increase the speed of the I2C communication
(and therefore make the display refresh more quickly).

Note that this overrides balena defaults, so we have to set `i2c_arm=on`
manually. You'd also need to explicitly set any other values that are set by
default (e.g., `audio=on` if you need to use audio).
