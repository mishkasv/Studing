"""The fisrt task"""

class Animal:
    def eat(self):
        return (f'The {self.__class__.__name__} eats.')

    def sleep(self):
        return (f'The {self.__class__.__name__} sleeps.')


class Wolf(Animal):
    def run(self):
        return ('The Wolf runs.')
    def hunt(self):
        return 'The wolf is hunting.'


class Dolphin(Animal):
    def swim(self):
        return ('The Dolphin swims.')



class Falcon(Animal):
    def fly(self):
        return ('The Falcon flies.')


class Kangaroo(Animal):
    def jump(self):
        return ('The Kangaroo jumps.')
    def box(self):
        return 'The Kangaroo is boxing.'


class Snake(Animal):
    def crawl(self):
        return ('The Snake crawls.')
    def bite(self):
        return 'The Snake bites.'


siryi = Wolf()
print(siryi.run(), siryi.hunt(), sep='\n')
willy = Dolphin()
print(willy.swim(), willy.eat(), sep='\n')
free = Falcon()
print(free.fly(), free.sleep(), sep='\n')
jack = Kangaroo()
print(jack.jump(), jack.box(), sep='\n')
kaa = Snake()
print(kaa.bite(), kaa.crawl(), sep='\n')

print(f'The jack is instance of Animal:',isinstance(jack, Animal))
print(f'The siryi is instance of Animal:',isinstance(siryi, Animal))
print(f'The willy is instance of Animal:',isinstance(willy, Animal))
print(f'The kaa is instance of Animal:',isinstance(kaa, Animal))
print(f'The free is instance of Animal:',isinstance(free, Animal))




