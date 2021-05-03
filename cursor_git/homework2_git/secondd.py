"""second task a"""
class Person:
    def __init__(self):
        arm = Arm(5, 1)
        self.discribearm = f'The arm has {arm.finger} fingers and {arm.ring} ring'
        self.snap = arm.snap('The Person snaps')


class Arm:
    def __init__(self, fingers : int, ring: int):
        self.finger = fingers
        self.ring = ring

    def snap(self, act):
        return act

john = Person()
print(john.snap)
print(john.discribearm)

"""second task b"""

class CellPhone:
    def __init__(self, screen, button):
        self.screen = f'The CellPhone has a screen by size: {screen.size}'
        self.button = f'The CellPhone has a one button: {button.button}'

class Screen:
    def __init__(self, w,h,):

        self.size = f'{w}x{h}'
class Button:
    def __init__(self, n):
        self.button = n

knopka = Button('Turn off/on')
ekran = Screen(4,5)
phone = CellPhone(ekran, knopka)

print(knopka.button)
print(ekran.size)
print(phone.button, phone.screen, sep='\n')

