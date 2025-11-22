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
    """Class to encapsulate complex health data (Composition)."""
    def __init__(self, description: str, date: str, severity: int, treatment: str):
        # All attributes are private
        self.__description = description
        self.__date = date
        # Data validation for severity
        if not 1 <= severity <= 10:
            raise ValueError("Severity must be between 1 and 10.")
        self.__severity = severity
        self.__treatment = treatment
    
    # Getter for required constraint check (Encapsulation)
    def get_severity(self):
        return self.__severity

    def get_treatment(self):
        """Returns the treatment plan."""
        return self.__treatment
        
    def __str__(self):
        # Uses F-String for readable string formatting
        return f"Issue: {self.__description} (Severity: {self.__severity}, Treatment: {self.__treatment})"

class Animal(ABC):
    """Abstract Base Class for all animals (Generalisation)"""
    
    def __init__(self, name: str, age: int, dietary_needs: str, environment_type: str):
        # Private attributes enforced
        self.__name = name
        self.__age = age
        self.__dietary_needs = dietary_needs
        self.__environment_type = environment_type
        # List of HealthRecord objects (Composition)
        self.__health_records: List[HealthRecord] = []
    # Mandatory Abstract Methods (must be implemented by children)
    @abstractmethod
    def cry(self):
        """Defines the unique sound the animal makes (Polymorphism)."""
        pass
    
    @abstractmethod
    def eat(self):
        pass
        
    @abstractmethod
    def sleep(self):
        pass
 # --- Getters (Accessors) for private data ---
    def get_name(self) -> str:
        return self.__name

    def get_environment_type(self) -> str:
        return self.__environment_type
        
    def get_health_records(self) -> List[HealthRecord]:
        return self.__health_records
    
    def is_under_treatment(self) -> bool:
        """Checks if any current health record indicates treatment required."""
        # Simple check based on treatment being recorded
        return any(rec for rec in self.__health_records if rec.get_treatment().lower() != "none")

    # --- Methods for Veterinarian interaction (Encapsulation/Setters) ---
    def add_health_issue(self, description: str, date: str, severity: int, treatment: str):
        """Allows staff to add a new health record."""
        record = HealthRecord(description, date, severity, treatment)
        self.__health_records.append(record)
        if treatment.lower() != "none":
            print(f"ALERT: {self.__name} is now under treatment.")
    
    def __str__(self):
        """Magic method for string conversion."""
        return f"{self.__name} ({self.__class__.__name__}, Age: {self.__age})"

# --- Subclasses (Specialisation) ---

class Mammal(Animal):
    def __init__(self, name: str, age: int, dietary_needs: str, environment_type: str):
        # Use super() to call the parent's constructor
        super().__init__(name, age, dietary_needs, environment_type)
        
    def cry(self):
        return "ROAR!" # Implements the abstract method (Polymorphism)

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

   