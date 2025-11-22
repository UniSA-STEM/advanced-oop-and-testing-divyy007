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
    
    # --- Core Management Methods ---
    
    def add_animal(self, animal: Animal):
        """Adds an animal object to the central registry, performing validation."""
        # Validation Check 1: Ensure input is an Animal type
        if not isinstance(animal, Animal):
            raise TypeError("Only Animal objects can be added to the zoo.")
        
        # Validation Check 2: Ensure name is unique (KeyError handling implicitly needed when accessing)
        animal_name = animal.get_name()
        if animal_name in self.__animals:
             raise AssignmentError(f"Animal '{animal_name}' already exists.")
             
        self.__animals[animal_name] = animal
        print(f"REPORT: Added animal: {animal_name} ({animal.__class__.__name__})")

    def remove_animal(self, animal_name: str):
        """Removes an animal from the registry and checks if it is assigned to an enclosure."""
        # Exception Handling using Try-Except for KeyError
        try:
            animal = self.__animals.pop(animal_name)
            # Before deletion, check if it's in an enclosure (ideally, remove it first, but simplified for core assignment scope)
            
            print(f"REPORT: Removed animal: {animal_name}")
            return animal
        except KeyError:
            # Explicitly raise a more descriptive error if needed, or handle gracefully
            raise AssignmentError(f"Animal '{animal_name}' not found in registry.")
        
    def add_enclosure(self, enclosure: Enclosure):
        # Validation Check 1: Ensure input is an Enclosure type
        if not isinstance(enclosure, Enclosure):
            raise TypeError("Only Enclosure objects can be added to the zoo.")

        enc_name = enclosure.get_name()
        if enc_name in self.__enclosures:
             raise AssignmentError(f"Enclosure '{enc_name}' already exists.")
             
        self.__enclosures[enc_name] = enclosure
        print(f"REPORT: Added enclosure: {enc_name} (Type: {enclosure.get_environmental_type()})")

    def assign_animal_to_enclosure(self, animal_name: str, enclosure_name: str):
        """Assigns an animal to an enclosure, enforcing all health and species constraints."""
        try:
            animal = self.__animals[animal_name]
            enclosure = self.__enclosures[enclosure_name]
        except KeyError as e:
            # Handle if animal or enclosure is not found [9]
            raise AssignmentError(f"Could not find required entity: {e.args}")

        # Constraint 1: Health Status Check (Animal under treatment should not be moved)
        if animal.is_under_treatment(): # Assumes animal.py implements this getter
            # Raise a custom exception when a rule is violated [12, 13]
            raise AssignmentError(f"Animal {animal_name} is under treatment and cannot be moved.")
            
        # Constraint 2 & 3: Species/Environment Check (delegated to Enclosure logic)
        enclosure.add_animal(animal)
        
        print(f"REPORT: Assigned {animal_name} to {enclosure_name}.")

    # --- Reporting and Utilities ---
    
    def generate_animal_report_by_species(self, species_class):
        """Generates a list of animals belonging to a specific class (e.g., Mammal)."""
        # Uses List Comprehension for filtering objects based on type
        report = [
            animal.get_name() 
            for animal in self.__animals.values() 
            if isinstance(animal, species_class) # Using isinstance() for type filtering
        ]
        return report

    def generate_health_reports_by_severity(self, min_severity: int):
        """Generates reports for animals with health issues above a minimum severity."""
        sick_animals = []
        for animal in self.__animals.values():
            records = animal.get_health_records() # Assumes this returns the list of records
            for record in records:
                if record.get_severity() >= min_severity:
                    sick_animals.append(f"{animal.get_name()} (Severity {record.get_severity()})")
        
        # Sort the results by name using a lambda expression if the list stored tuples/objects
        return sick_animals

# --- Demonstration Script ---
# (The sources require main.py to act as a demonstration script/walkthrough)

def run_demonstration():
    zoo = ZooManager()

    # 1. Create Animals (Inheritance & Abstraction in action)
    leo = Mammal("Leo", 5, "Meat", "Savannah")
    penguin = Bird("Waddles", 2, "Fish", "Aquatic")
    viper = Reptile("Scales", 1, "Rodents", "Desert")

    # 2. Add Animals to ZooManager (Composition)
    zoo.add_animal(leo)
    zoo.add_animal(penguin)
    zoo.add_animal(viper)

    # 3. Create Enclosures
    lion_habitat = Enclosure("Lion Habitat", 500, "Savannah", 10, Mammal)
    penguin_pool = Enclosure("Penguin Pool", 300, "Aquatic", 8, Bird)
    
    zoo.add_enclosure(lion_habitat)
    zoo.add_enclosure(penguin_pool)

    # 4. Assign Animals (Successful)
    try:
        zoo.assign_animal_to_enclosure("Leo", "Lion Habitat")
        zoo.assign_animal_to_enclosure("Waddles", "Penguin Pool")
    except AssignmentError as e:
        print(f"ASSIGNMENT FAILED: {e}")

    # 5. Demonstrate Constraints (Incompatible Species)
    print("\n--- Testing Constraints (Failures) ---")
    try:
        # Attempt to put a Reptile in a Bird enclosure
        zoo.assign_animal_to_enclosure("Scales", "Penguin Pool")
    except AssignmentError as e:
        # Exception Handling to prevent crash [11]
        print(f"FAILURE REPORT: {e}")