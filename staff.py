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