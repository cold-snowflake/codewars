#Teach snoopy and scooby doo how to bark using object
#methods. Currently only snoopy can bark and not scooby doo.

class Dog ():
    def __init__(self, breed):
        self.breed = breed

    def bark (self):
        return("Woof")




snoopy = Dog("Beagle")

# snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")

print( f"snoopy {snoopy.bark()}")
print(f"scoobydo {scoobydoo.bark()}")
