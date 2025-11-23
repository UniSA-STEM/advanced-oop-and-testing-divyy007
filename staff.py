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
        self.__name = name
        self.__employee_id = employee_id
        
    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Staff: {self.__name} (ID: {self.__employee_id})"
    
class Zookeeper(Staff):
    """Staff member responsible for feeding and cleaning."""
    def __init__(self, name: str, employee_id: str):
        super().__init__(name, employee_id)
        
    def feed_animal(self, animal: Animal):
        action = animal.eat()
        return f"{self.get_name()} is feeding {animal.get_name()}. Result: {action}"
        
    def clean_enclosure(self, enclosure: Enclosure):
        enclosure.clean() 
        return f"{self.get_name()} cleaned {enclosure.get_name()}. Cleanliness is now maxed out."
    
class Veterinarian(Staff):
    """Staff responsible for medical checks and health records."""
    def __init__(self, name: str, employee_id: str):
        super().__init__(name, employee_id)

    def conduct_health_check(self, animal: Animal):
        """Inspects an animal and prints out their history."""
        records = animal.get_health_records()
        if not records:
            return f"{animal.get_name()} is healthy with no recent issues."
        
        report = [str(r) for r in records]
        return f"{self.get_name()} conducted check on {animal.get_name()}. Issues: \n" + "\n".join(report)

    def record_health_issue(self, animal: Animal, description: str, date: str, severity: int, treatment: str):
        """Creates a new health record for an animal."""
        animal.add_health_issue(description, date, severity, treatment)
        return f"{self.get_name()} recorded issue for {animal.get_name()} (Severity {severity})."