"""first a task"""
class Animal:
    def eat(self):
        return f'The {self.__class__.__name__} eats.'

    def sleep(self):
        return f'The {self.__class__.__name__} sleeps.'

class Horse(Animal):
    def gallop(self):
        return f'The {self.__class__.__name__} is gallopping.'
    def trot(self):
        return f'The {self.__class__.__name__} trots'


class Human:
    def eat(self):
        return f'The {self.__class__.__name__} eats.'

    def sleep(self):
        return f'The {self.__class__.__name__} sleeps on bad.'

    def study(self):
        return f'The {self.__class__.__name__} studies.'

    def work(self):
        return f'The {self.__class__.__name__} works.'

class Centaur(Horse, Human):
    def jump(self):
        return 'The Centaur jumps'


kent = Centaur()

print(kent.sleep(), kent.jump(), kent.study(), kent.work(), kent.gallop(), sep='\n')