import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeypadScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

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

if __name__ == '__main__':
    keyboard.go()