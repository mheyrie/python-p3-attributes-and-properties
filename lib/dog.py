#!/usr/bin/env python3

# APPROVED_BREEDS = [
#     "Mastiff",
#     "Chihuahua",
#     "Corgi",
#     "Shar Pei",
#     "Beagle",
#     "French Bulldog",
#     "Pug",
#     "Pointer"
# ]

class Dog:
    def __init__(self, name="Fido"):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")

    name = property(get_name, set_name)

dog_instance = Dog()
print(dog_instance.set_name("Dreed")) 





#  python3 lib/dog.py

    
