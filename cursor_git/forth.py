"""forht task"""
from abc import ABC, abstractmethod

class Laptop(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def screen(self):
        pass
    @abstractmethod
    def touchpad(self):
        pass
    @abstractmethod
    def keyboard(self):
        pass
    @abstractmethod
    def webcab(self):
        pass
    @abstractmethod
    def ports(self):
        pass
    @abstractmethod
    def dynamics(self):
        pass

class HPLaptop(Laptop):
    def screen(self):
        return 'The screen has size 13 inch'
    def keyboard(self):
        return 'keyboard without NUMPAD'
    def ports(self):
        return 'The HPLaptop has 2 usb portd, 1 hdmi, 1 ethernet'
    def dynamics(self):
        return 'The Laptop has 2 dynamics 5W both'
    def touchpad(self):
        return 'Does not work'
    def webcab(self):
        pass


mycomp = HPLaptop('mishka')
print(mycomp.name)
print(mycomp.ports())
print(mycomp.touchpad())
