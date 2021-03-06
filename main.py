import time
import board
import neopixel
import matplotlib.colors as colors

pixel_pin = board.D18
num_pixels = 126
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER)

def color_to_rgb(color):
    return tuple(round(255 * x) for x in colors.to_rgb(color))

def T1(r, g, b):
    for i in range(14):
        pixels[i] = (r, g, b)

def T2(r, g, b):
    for i in range(14,28):
        pixels[i] = (r, g, b)

def T3(r, g, b):
    for i in range(28, 42):
        pixels[i] = (r, g, b)

def T4(r, g, b):
    for i in range(42, 56):
        pixels[i] = (r, g, b)

def T5(r, g, b):
    for i in range(56,70):
        pixels[i] = (r, g, b)

def T6(r, g, b):
    for i in range(70, 84):
        pixels[i] = (r, g, b)

def T7(r, g, b):
    for i in range(84, 98):
        pixels[i] = (r, g, b)

def T8(r, g, b):
    for i in range(98, 112):
        pixels[i] = (r, g, b)

def T9(r, g, b):
    for i in range(112, 126):
        pixels[i] = (r, g, b)



def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

###############################################################################
###############################################################################

pixels.fill(color_to_rgb('red'))
pixels.show()
time.sleep(2)
pixels.fill(color_to_rgb('green'))
pixels.show()
time.sleep(2)
pixels.fill(color_to_rgb('blue'))
pixels.show()
time.sleep(2)

while True:
    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step

# time.sleep(2)