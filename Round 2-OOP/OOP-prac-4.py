class Animal: 
    def speak(self):
        print("Animal cannot speak!")
class Dog(Animal):
    def speak(self):
        print("Woof!")
class Cat(Animal):
    def speak(self):
        print("Meow!")



animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.speak()
