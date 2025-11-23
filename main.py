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
from custom_exceptions import AssignmentError

class ZooManager:
    """Manages all collections of animals, enclosures, and staff."""
    
    def __init__(self):
        # Using dictionaries to store objects by name
        self.__animals = {}
        self.__enclosures = {}
        self.__staff = {}
    
    # --- Getters ---
    def get_animals(self):
        return self.__animals

    def get_enclosures(self):
        return self.__enclosures
    
    # --- Core Management Methods ---
    
    def add_animal(self, animal: Animal):
        """Adds an animal object to the central registry."""
        # Verify input type
        if not isinstance(animal, Animal):
            raise TypeError("Only Animal objects can be added to the zoo.")
        
        # Check for duplicates
        animal_name = animal.get_name()
        if animal_name in self.__animals:
             raise AssignmentError(f"Animal '{animal_name}' already exists.")
             
        self.__animals[animal_name] = animal
        print(f"REPORT: Added animal: {animal_name} ({animal.__class__.__name__})")

    def remove_animal(self, animal_name: str):
        """Removes an animal from the registry."""
        # Safely remove the animal; handles cases where the name doesn't exist
        try:
            animal = self.__animals.pop(animal_name)
            print(f"REPORT: Removed animal: {animal_name}")
            return animal
        except KeyError:
            raise AssignmentError(f"Animal '{animal_name}' not found in registry.")

    def add_enclosure(self, enclosure: Enclosure):
        # Verify input type
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
            # Stop if the animal or enclosure names are invalid
            raise AssignmentError(f"Could not find required entity: {e.args}")

        # Constraint 1: Sick animals cannot be moved
        if animal.is_under_treatment():
            raise AssignmentError(f"Animal {animal_name} is under treatment and cannot be moved.")
            
        # Constraint 2 & 3: Add to enclosure (validation happens inside Enclosure class)
        enclosure.add_animal(animal)
        
        print(f"REPORT: Assigned {animal_name} to {enclosure_name}.")
        
    # --- Reporting and Utilities ---
    
    def generate_animal_report_by_species(self, species_class):
        """Generates a list of animals belonging to a specific class."""
        # Filter the list to include only the requested species
        report = [
            animal.get_name() 
            for animal in self.__animals.values() 
            if isinstance(animal, species_class)
        ]
        return report

    def generate_health_reports_by_severity(self, min_severity: int):
        """Generates reports for animals with health issues above a minimum severity."""
        sick_animals = []
        for animal in self.__animals.values():
            records = animal.get_health_records()
            for record in records:
                if record.get_severity() >= min_severity:
                    sick_animals.append(f"ATTENTION: {animal.get_name()} requires care (Severity: {record.get_severity()})")
        return sick_animals
        
# --- Demonstration Script ---

def run_demonstration():
    zoo = ZooManager()

    # 1. Setup initial animals
    leo = Mammal("Leo", 5, "Meat", "Savannah")
    penguin = Bird("Waddles", 2, "Fish", "Aquatic")
    viper = Reptile("Scales", 1, "Rodents", "Desert")

    # 2. Register animals in the system
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
        # Catch the error to keep the program running
        print(f"FAILURE REPORT: {e}")
        
    # 6. Demonstrate Health Constraint
    # Leo gets sick
    leo.add_health_issue("Broken tooth", "2024-05-01", 8, "Surgery required")
    print(f"STATUS: Leo is under treatment: {leo.is_under_treatment()}")
    
    try:
        # Attempt to move the sick animal
        print("ATTEMPT: Trying to move sick animal Leo...")
        zoo.assign_animal_to_enclosure("Leo", "Lion Habitat")
    except AssignmentError as e:
        print(f"FAILURE REPORT: {e}")

    # 7. Reporting
    print("\n--- Generating Reports ---")
    mammal_list = zoo.generate_animal_report_by_species(Mammal)
    print(f"Mammals in Zoo: {mammal_list}")
    
    sick_report = zoo.generate_health_reports_by_severity(5)
    print(f"High Severity Cases: {sick_report}")
    
if __name__ == "__main__":
    run_demonstration()