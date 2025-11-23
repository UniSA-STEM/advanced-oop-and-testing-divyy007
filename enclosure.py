'''
File: enclosure.py
Description: Enclosure class for housing Animal instances while enforcing compatibility and environment rules. 
Author: Divyesh
ID: 110449639
Username: divyy007
This is my own work as defined by the University's Academic Integrity Policy.
'''


from animal import Animal
from typing import Type

class Enclosure:
    """Houses animals and enforces compatibility constraints."""
    
    def __init__(self, name: str, size: int, environmental_type: str, cleanliness_level: int, compatible_species: Type[Animal]):
        self.__name = name
        self.__size = size
        self.__environmental_type = environmental_type
        
        if not 1 <= cleanliness_level <= 10:
             raise ValueError("Cleanliness level must be between 1 and 10.")
        self.__cleanliness_level = cleanliness_level
        self.__compatible_species = compatible_species 
        self.__housed_animals = {}

    def get_name(self):
        return self.__name
        
    def get_environmental_type(self):
        return self.__environmental_type

    def get_cleanliness_level(self):
        return self.__cleanliness_level
        
    def get_housed_animals(self):
        return self.__housed_animals

    def add_animal(self, animal: Animal):
        """Adds an animal if it meets environmental and species constraints."""
        
        if not isinstance(animal, self.__compatible_species):
            raise ValueError(f"Species mismatch: {animal.get_name()} cannot be housed here.")
            
        if animal.get_environment_type() != self.__environmental_type:
            raise ValueError(f"Environmental mismatch: {animal.get_name()} requires {animal.get_environment_type()}.")
            
        self.__housed_animals[animal.get_name()] = animal
        
    def remove_animal(self, animal_name: str):
        if animal_name not in self.__housed_animals:
            raise ValueError(f"Animal '{animal_name}' not found in enclosure '{self.__name}'.")
        return self.__housed_animals.pop(animal_name)

    def report_status(self):
        animal_names = ", ".join(self.__housed_animals.keys())
        return (f"ENCLOSURE: {self.__name}\n"
                f"  Type: {self.__environmental_type}, Cleanliness: {self.__cleanliness_level}/10\n"
                f"  Animals Housed: {animal_names if animal_names else 'None'}")

    def clean(self):
        """Restores the enclosure to maximum cleanliness."""
        self.__cleanliness_level = 10