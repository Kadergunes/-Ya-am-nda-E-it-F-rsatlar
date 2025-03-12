class Animal_sound():
    def sound (self):
        return 'bark!'

class Animal_move():
    def move (self):
        return 'walking!'

class Dog(Animal_move,Animal_sound):
    print(f'DOGS SOUND {sound()} and {move()}')


dog1=Dog()
print(dog1.move())
print(dog1.sound())
