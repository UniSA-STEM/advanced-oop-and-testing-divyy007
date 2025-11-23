'''
File: animal.py
Description: Abstract base class and subclass for animals in the zoo.
Author: Divyesh
ID: 110449639
Username: divyy007
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod
from typing import List
from custom_exceptions import AssignmentError

class HealthRecord:
    """Stores details about a single health event for an animal."""
    def __init__(self, description: str, date: str, severity: int, treatment: str):
        self.__description = description
        self.__date = date
        
        # Ensure severity is a reasonable number
        if not 1 <= severity <= 10:
            raise ValueError("Severity must be between 1 and 10.")
        self.__severity = severity
        self.__treatment = treatment
    
    def get_severity(self):
        return self.__severity

    def get_treatment(self):
        return self.__treatment
        
    def __str__(self):
        return f"Issue: {self.__description} (Severity: {self.__severity}, Treatment: {self.__treatment})"

class Animal(ABC):
    """The base class that all specific animal types will inherit from."""
    
    def __init__(self, name: str, age: int, dietary_needs: str, environment_type: str):
        self.__name = name
        self.__age = age
        self.__dietary_needs = dietary_needs
        self.__environment_type = environment_type
        # Each animal keeps its own list of health records
        self.__health_records: List[HealthRecord] = []

    # These methods must be defined by the specific animal subclasses
    @abstractmethod
    def cry(self):
        """Every animal makes a different sound."""
        pass
    
    @abstractmethod
    def eat(self):
        pass
        
    @abstractmethod
    def sleep(self):
        pass

    # --- Helper methods to access private data ---
    def get_name(self) -> str:
        return self.__name

    def get_environment_type(self) -> str:
        return self.__environment_type
        
    def get_health_records(self) -> List[HealthRecord]:
        return self.__health_records
    
    def is_under_treatment(self) -> bool:
        """Checks if the animal is currently being treated."""
        for record in self.__health_records:
            # If the treatment is anything other than 'None', they are sick
            if record.get_treatment().lower() != "none":
                return True
        return False
    def add_health_issue(self, description: str, date: str, severity: int, treatment: str):
        """Adds a new health record to the animal's history."""
        record = HealthRecord(description, date, severity, treatment)
        self.__health_records.append(record)
        if treatment.lower() != "none":
            print(f"ALERT: {self.__name} is now under treatment.")
    
    def __str__(self):
        """Returns a readable string representation of the animal."""
        return f"{self.__name} ({self.__class__.__name__}, Age: {self.__age})"

# --- Specific Animal Types ---

class Mammal(Animal):
    def __init__(self, name: str, age: int, dietary_needs: str, environment_type: str):
        # Initialize the parent Animal class
        super().__init__(name, age, dietary_needs, environment_type)
        
    def cry(self):
        return "ROAR!"

    def eat(self):
        return "Chewing..."

    def sleep(self):
        return "Curled up and resting."

class Bird(Animal):
    def __init__(self, name: str, age: int, dietary_needs: str, environment_type: str):
        super().__init__(name, age, dietary_needs, environment_type)
        
    def cry(self):
        return "CAW! CAW!"

    def eat(self):
        return "Pecking grain."

    def sleep(self):
        return "Perched and sleeping."

class Reptile(Animal):
    def __init__(self, name: str, age: int, dietary_needs: str, environment_type: str):
        super().__init__(name, age, dietary_needs, environment_type)
        
    def cry(self):
        return "Hissing softly."

    def eat(self):
        return "Swallowing prey whole."

    def sleep(self):
        return "Basking under heat lamp."