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
    """Houses animals and enforces compatibility constraints."""
    
    # Note: Enclosure is composed of Animal objects
    def __init__(self, name: str, size: int, environmental_type: str, cleanliness_level: int, compatible_species: Type[Animal]):
        self.__name = name
        self.__size = size
        self.__environmental_type = environmental_type
        # Data validation for cleanliness level (ensuring valid input data)
        if not 1 <= cleanliness_level <= 10:
             raise ValueError("Cleanliness level must be between 1 and 10.")
        self.__cleanliness_level = cleanliness_level
        
        # Stores the required base class (e.g., Mammal or Bird) for validation
        self.__compatible_species = compatible_species 
        
        # Dictionary to store housed animals (Composition)
        self.__housed_animals = {} # Key: animal name, Value: Animal object

    # --- Getters ---
    def get_name(self):
        return self.__name
        
    def get_environmental_type(self):
        return self.__environmental_type

    def get_cleanliness_level(self):
        return self.__cleanliness_level
        
    def get_housed_animals(self):
        return self.__housed_animals

    # --- Core Functionality & Validation ---

    def add_animal(self, animal: Animal):
        """Adds an animal if it meets environmental and species constraints."""
        
        # Constraint 1: Check if the animal's class matches the compatible species
        if not isinstance(animal, self.__compatible_species):
            # Raise exception if species is incompatible
            raise AssignmentError(f"Species mismatch: {animal.get_name()} ({animal.__class__.__name__}) cannot be housed with type {self.__compatible_species.__name__}.")
            
        # Constraint 2: Check environmental needs (using an attribute for validation)
        if animal.get_environment_type() != self.__environmental_type:
            raise AssignmentError(f"Environmental mismatch: {animal.get_name()} requires {animal.get_environment_type()} environment.")
            
        # Add the animal to the housed collection
        self.__housed_animals[animal.get_name()] = animal
        
    def remove_animal(self, animal_name: str):
        """Removes an animal by name."""
        if animal_name not in self.__housed_animals:
            raise AssignmentError(f"Animal '{animal_name}' not found in enclosure '{self.__name}'.")
        return self.__housed_animals.pop(animal_name)

    def report_status(self):
        """Reports the enclosure status and lists contained animals."""
        animal_names = ", ".join(self.__housed_animals.keys())
        return (f"ENCLOSURE: {self.__name}\n"
                f"  Type: {self.__environmental_type}, Cleanliness: {self.__cleanliness_level}/10\n"
                f"  Animals Housed: {animal_names if animal_names else 'None'}")

    def clean(self, amount: int = 10):
        """Increases cleanliness level, capped at 10."""
        self.__cleanliness_level += amount
        if self.__cleanliness_level > 10:
            self.__cleanliness_level = 10