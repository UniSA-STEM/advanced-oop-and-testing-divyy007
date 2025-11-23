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

class ZooManager:
    """The central system for managing the zoo's assets."""
    
    def __init__(self):
        self.__animals = {}
        self.__enclosures = {}
    
    def get_animals(self):
        return self.__animals

    def get_enclosures(self):
        return self.__enclosures
    
    def add_animal(self, animal: Animal):
        if not isinstance(animal, Animal):
            raise TypeError("System Error: Only Animal objects can be added.")
        
        if animal.get_name() in self.__animals:
             raise ValueError(f"Error: {animal.get_name()} is already registered.")
             
        self.__animals[animal.get_name()] = animal
        print(f"✅ [Registry]: Registered new animal: {animal.get_name()}")

    def add_enclosure(self, enclosure: Enclosure):
        if not isinstance(enclosure, Enclosure):
            raise TypeError("System Error: Only Enclosure objects can be added.")

        if enclosure.get_name() in self.__enclosures:
             raise ValueError(f"Error: {enclosure.get_name()} already exists.")
             
        self.__enclosures[enclosure.get_name()] = enclosure
        print(f"✅ [Construction]: Built new enclosure: {enclosure.get_name()}")

    def assign_animal_to_enclosure(self, animal_name: str, enclosure_name: str):
        try:
            animal = self.__animals[animal_name]
            enclosure = self.__enclosures[enclosure_name]
        except KeyError:
            raise ValueError(f"Error: Could not find {animal_name} or {enclosure_name}.")

        if animal.is_under_treatment():
            raise ValueError(f"🚫 [Safety]: Cannot move {animal_name}. Currently under treatment.")
            
        enclosure.add_animal(animal)
        
        print(f"🚚 [Transport]: Successfully moved {animal_name} to {enclosure_name}.")
        
    def generate_animal_report(self, species_class):
        print(f"\n--- 📊 Generating {species_class.__name__} Report ---")
        found_animals = []
        
        for animal in self.__animals.values():
            if isinstance(animal, species_class):
                found_animals.append(animal.get_name())
        
        return found_animals

    def check_medical_logs(self):
        print("\n--- 🏥 Checking Medical Logs ---")
        severe_cases = []
        
        for animal in self.__animals.values():
            for record in animal.get_health_records():
                if record.get_severity() >= 7:
                    severe_cases.append(f"URGENT: {animal.get_name()} - {record}")
        
        return severe_cases


# --- Demonstration Script ---

def run_zoo_walkthrough():
    print("=== 🦁 INITIALIZING ZOO MANAGEMENT SYSTEM 🦁 ===\n")
    
    zoo = ZooManager()

    print("--- Step 1: Registering Animals ---")
    leo = Mammal("Leo", 5, "Meat", "Savannah")
    waddles = Bird("Waddles", 2, "Fish", "Aquatic")
    scales = Reptile("Scales", 1, "Rodents", "Desert")

    zoo.add_animal(leo)
    zoo.add_animal(waddles)
    zoo.add_animal(scales)
    print("")

    print("--- Step 2: Constructing Enclosures ---")
    savannah_zone = Enclosure("Savannah Zone", 500, "Savannah", 10, Mammal)
    aquatic_center = Enclosure("Aquatic Center", 300, "Aquatic", 9, Bird)
    
    zoo.add_enclosure(savannah_zone)
    zoo.add_enclosure(aquatic_center)
    print("")

    print("--- Step 3: Moving Animals to Habitats ---")
    try:
        zoo.assign_animal_to_enclosure("Leo", "Savannah Zone")
        zoo.assign_animal_to_enclosure("Waddles", "Aquatic Center")
    except ValueError as e:
        print(e)
    print("")

    print("--- Step 4: Testing Safety Protocols (Failures) ---")
    
    print("Attempting to put 'Scales' (Reptile) into 'Aquatic Center' (Bird only)...")
    try:
        zoo.assign_animal_to_enclosure("Scales", "Aquatic Center")
    except ValueError as e:
        print(f"❌ Failed: {e}")

    print("")

    print("--- Step 5: Medical Emergency Simulation ---")
    print("🚨 EVENT: Leo has broken a tooth!")
    leo.add_health_issue("Broken Tooth", "2024-11-24", 8, "Surgery")

    print("Attempting to move Leo back to enclosure...")
    try:
        zoo.assign_animal_to_enclosure("Leo", "Savannah Zone")
    except ValueError as e:
        print(f"❌ Failed: {e}")

    mammals = zoo.generate_animal_report(Mammal)
    print(f"Mammal Census: {mammals}")

    sick_list = zoo.check_medical_logs()
    if sick_list:
        print("Active Medical Alerts:")
        for alert in sick_list:
            print(f"  - {alert}")

    print("\n=== 🏁 SIMULATION COMPLETE 🏁 ===")

if __name__ == "__main__":
    run_zoo_walkthrough()