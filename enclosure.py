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

