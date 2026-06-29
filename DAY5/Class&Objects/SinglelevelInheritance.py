class Dog:
    def sound():
        print("BOW BOW")
    def eat(self):
        print("Dog is Eating")
class Cat(Dog):
    def sound():
        print("MEOW MEOW")

# Instance
d=Cat()
d.eat()