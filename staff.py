'''
File: staff.py
Description: Staff-related classes for animal care and enclosure maintenance. 
Author: Divyesh
ID: 110449639
Username: divyy007
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from enclosure import Enclosure

class Staff:
    """Base class for all staff members."""
    def __init__(self, name: str, employee_id: str):
        # Private attributes
        self.__name = name
        self.__employee_id = employee_id
        
    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Staff: {self.__name} (ID: {self.__employee_id})"
    
class Zookeeper(Staff):
    """Staff specialized in daily care and enclosure maintenance (Specialisation) [34]."""
    def __init__(self, name: str, employee_id: str):
        super().__init__(name, employee_id)
        
    def feed_animal(self, animal: Animal):
        """Zookeeper performs the feeding action (Association) [33]."""
        # Invokes the polymorphic method on the animal object
        action = animal.eat()
        return f"{self.get_name()} is feeding {animal.get_name()}. Result: {action}"
        
    def clean_enclosure(self, enclosure: Enclosure):
        """Zookeeper performs cleaning duties."""
        # Calls the public method on the enclosure object
        enclosure.clean() 
        return f"{self.get_name()} cleaned {enclosure.get_name()}. Cleanliness is now maxed out."

