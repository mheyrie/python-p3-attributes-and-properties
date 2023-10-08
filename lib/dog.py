#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Fido", breed = ""):
        self._name = name
        self.breed = breed

    def get_name(self):
        return self._name

    def set_name(self, value):
        
        if value == "" or type(value) in (int, float) or 1 > len(value) or len(value) > 25:
            print("Name must be a string between 1 and 25 characters.")
            
        else:
            self._name = value

    name = property(get_name, set_name)

    def get_breed(self):
        return self.breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self.breed = breed


    breed = property(get_breed, set_breed)


#  python3 lib/dog.py

    
