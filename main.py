'''
File: main.py
Description: Provides a simple ZooManges class to register animals, enclosures, and staff, and includes a demonstration entry point exercise the core functionality. 
Author: Divyesh
ID: 110449639
Username: divyy007
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal, Mammal, Bird, Reptile, HealthRecord
from enclosure import Enclosure
from staff import Staff, Zookeeper, Veterinarian
from custom_exceptions import AssignmentError # Custom Exception (see below)

class ZooManager:
    """Manages all collections of animals, enclosures, and staff."""
    
    def __init__(self):
        # Using Dictionaries for fast lookups (Key: Name, Value: Object) [8]
        self.__animals = {}
        self.__enclosures = {}
        self.__staff = {}
    
    # --- Encapsulation (Getters/Setters) ---
    # Simplified getters for the collections (for reporting/main demonstration)
    def get_animals(self):
        """Returns the dictionary of all animals."""
        return self.__animals

    def get_enclosures(self):
        """Returns the dictionary of all enclosures."""
        return self.__enclosures