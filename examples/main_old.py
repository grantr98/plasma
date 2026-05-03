import time
import plasma

# Set how many LEDs you have
NUM_LEDS = 50

# Set the brightness
BRIGHTNESS = 0.5

# set up the WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(NUM_LEDS, color_order=plasma.COLOR_ORDER_RGB)

# start updating the LED strip
led_strip.start()


while True:

    print("Non Spooky Rainbows!")
    HUE_START = 0  # Icy
    HUE_END = 255  # Blue
    SPEED = 0.1  # bigger = faster (harder, stronger)

    distance = 0.0
    direction = SPEED
    while True:
        for i in range(NUM_LEDS):
            # generate a triangle wave that moves up and down the LEDs
            j = max(0, 1 - abs(distance - i) / (NUM_LEDS / 3))
            hue = HUE_START + j * (HUE_END - HUE_START)

            led_strip.set_hsv(i, hue / 360, 1.0, BRIGHTNESS)

        # reverse direction at the end of colour segment to avoid an abrupt change
        distance += direction
        if distance > NUM_LEDS:
            direction = - SPEED
        if distance < 0:
            direction = SPEED

        time.sleep(0.01)
