'''
File: enclosure.py
Description: Enclosure class for housing Animal instances while enforcing compatibility and environment rules. 
Author: Divyesh
ID: 110449639
Username: divyy007
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from custom_exceptions import AssignmentError
from typing import Type

class Enclosure:
    """Represents a specific habitat that holds compatible animals."""
    
    def __init__(self, name: str, size: int, environmental_type: str, cleanliness_level: int, compatible_species: Type[Animal]):
        self.__name = name
        self.__size = size
        self.__environmental_type = environmental_type
        
        # Ensure cleanliness is within the valid 1-10 range
        if not 1 <= cleanliness_level <= 10:
             raise ValueError("Cleanliness level must be between 1 and 10.")
        self.__cleanliness_level = cleanliness_level
        
        # This determines exactly which class of animal (e.g., Mammal) is allowed here
        self.__compatible_species = compatible_species 
        
        # Stores the animals currently inside this enclosure
        self.__housed_animals = {} 

    # --- Getters ---
    def get_name(self):
        return self.__name
        
    def get_environmental_type(self):
        return self.__environmental_type

    def get_cleanliness_level(self):
        return self.__cleanliness_level
        
    def get_housed_animals(self):
        return self.__housed_animals

    # --- Main Logic ---

    def add_animal(self, animal: Animal):
        """Adds an animal, but only if it matches the species and environment rules."""
        
        # Check 1: Is this the right species for this enclosure?
        if not isinstance(animal, self.__compatible_species):
            raise AssignmentError(f"Species mismatch: {animal.get_name()} ({animal.__class__.__name__}) cannot be housed with type {self.__compatible_species.__name__}.")
            
        # Check 2: Does the animal like this environment?
        if animal.get_environment_type() != self.__environmental_type:
            raise AssignmentError(f"Environmental mismatch: {animal.get_name()} requires {animal.get_environment_type()} environment.")
            
        # If checks pass, add them to the list
        self.__housed_animals[animal.get_name()] = animal
        
    def remove_animal(self, animal_name: str):
        """Removes an animal from the enclosure."""
        if animal_name not in self.__housed_animals:
            raise AssignmentError(f"Animal '{animal_name}' not found in enclosure '{self.__name}'.")
        return self.__housed_animals.pop(animal_name)

    def report_status(self):
        """Returns a summary of the enclosure and who lives there."""
        animal_names = ", ".join(self.__housed_animals.keys())
        return (f"ENCLOSURE: {self.__name}\n"
                f"  Type: {self.__environmental_type}, Cleanliness: {self.__cleanliness_level}/10\n"
                f"  Animals Housed: {animal_names if animal_names else 'None'}")

    def clean(self):
        """Restores the enclosure to maximum cleanliness."""
        self.__cleanliness_level = 10