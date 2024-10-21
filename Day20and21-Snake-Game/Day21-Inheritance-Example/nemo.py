class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale.")


class Fish(Animal):         # Inherits the Animal class

    def __init__(self):
        super().__init__()  # Gets hold of the __init__ method from animal.
                            # Now the fish class has self.num_eyes = 2 as well.

    def swim(self):
        print("Moving in water.")

    def breathe(self):
        super().breathe()                   # Gets hold of the breathing method.
        print("Doing this underwater.")     # But also provides extra functionality, overriding it


nemo = Fish()
nemo.swim()
nemo.breathe()