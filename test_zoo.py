import pytest
from animal import Mammal, Bird, Reptile
from enclosure import Enclosure
from main import ZooManager

# --- Fixtures ---
@pytest.fixture
def zoo():
    return ZooManager()

@pytest.fixture
def lion():
    return Mammal("Leo", 5, "Meat", "Savannah")

@pytest.fixture
def penguin():
    return Bird("Pingu", 2, "Fish", "Aquatic")

@pytest.fixture
def savannah_enclosure():
    return Enclosure("Savannah Pen", 500, "Savannah", 5, Mammal)

def test_add_animal(zoo, lion):
    zoo.add_animal(lion)
    assert "Leo" in zoo.get_animals()
    assert isinstance(zoo.get_animals()["Leo"], Mammal)

def test_add_duplicate_animal(zoo, lion):
    zoo.add_animal(lion)
    with pytest.raises(ValueError):
        zoo.add_animal(lion)

def test_assign_animal_to_enclosure_success(zoo, lion, savannah_enclosure):
    zoo.add_animal(lion)
    zoo.add_enclosure(savannah_enclosure)
    
    zoo.assign_animal_to_enclosure("Leo", "Savannah Pen")
    
    housed = savannah_enclosure.get_housed_animals()
    assert "Leo" in housed

def test_assign_incompatible_species(zoo, penguin, savannah_enclosure):
    zoo.add_animal(penguin)
    zoo.add_enclosure(savannah_enclosure)
    
    with pytest.raises(ValueError) as excinfo:
        zoo.assign_animal_to_enclosure("Pingu", "Savannah Pen")
    assert "Species mismatch" in str(excinfo.value)

def test_assign_incompatible_environment(zoo):
    whale = Mammal("Moby", 10, "Plankton", "Aquatic")
    savannah_pen = Enclosure("Dry Pen", 500, "Savannah", 10, Mammal)
    
    zoo.add_animal(whale)
    zoo.add_enclosure(savannah_pen)
    
    with pytest.raises(ValueError) as excinfo:
        zoo.assign_animal_to_enclosure("Moby", "Dry Pen")
    assert "Environmental mismatch" in str(excinfo.value)

def test_sick_animal_movement_restriction(zoo, lion, savannah_enclosure):
    zoo.add_animal(lion)
    zoo.add_enclosure(savannah_enclosure)
    
    lion.add_health_issue("Flu", "2024-01-01", 5, "Rest")
    
    with pytest.raises(ValueError) as excinfo:
        zoo.assign_animal_to_enclosure("Leo", "Savannah Pen")
    assert "under treatment" in str(excinfo.value)

def test_animal_polymorphism():
    lion = Mammal("Simba", 1, "Meat", "Land")
    bird = Bird("Tweety", 1, "Seeds", "Air")
    
    assert lion.cry() == "ROAR!"
    assert bird.cry() == "CAW! CAW!"