class Dog(object):
    def __init__(self, name):
        self.name = name
class Chihuahua(Dog): pass
B = Dog("Buddy")
W = Chihuahua("Wink")

print(isinstance(W,Dog))