import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeypadScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.OLED import OLED, OledDisplayMode
from kmk.extensions.pixel import Pixel, PixelSettings
from kmk.handlers.sequences import simple_key_sequence

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D1, board.D3, board.D4, board.D2]

keyboard.matrix = KeypadScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap =[KC.Macro(Press(KC.LCTRL), Tap(KC.S), Release(KC.LCTRL)),
KC.Macro(Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL)),
KC.Macro(Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL)),
KC.Macro(Press(KC.LCTRL), Tap(KC.Z), Release(KC.LCTRL))]

keyboard.extensions.append(
    OLED(
        data_pin=board.GP0,
        clk_pin=board.GP1,
        rotate=0,
        flip=False,
        to_display=OLED.display_layer,
        display_mode=OledDisplayMode.FULL,
    )
)

pixel = Pixel(
    pin=board.D0,
    num_pixels=2,        
    brightness=0.3,
    animation=None,
)

keyboard.extensions.append(pixel)

def update_leds():
    caps_on = keyboard.lock_status.caps_lock
    num_on = keyboard.lock_status.num_lock

    if caps_on:
        pixel.set_pixel(0, (255, 0, 0))
    else:
        pixel.set_pixel(0, (0, 0, 0))

    if num_on:
        pixel.set_pixel(1, (255, 0, 0))
    else:
        pixel.set_pixel(1, (0, 0, 0))

    pixel.show()


keyboard.after_matrix_scan = update_leds

if __name__ == '__main__':
    keyboard.go()