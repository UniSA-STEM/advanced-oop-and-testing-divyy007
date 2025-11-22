import pytest
from animal import Mammal, Bird, Reptile
from enclosure import Enclosure
from main import ZooManager
from custom_exceptions import AssignmentError

# --- Fixtures (Setup) ---
@pytest.fixture
def zoo():
    """Fixture to provide a fresh ZooManager instance for each test."""
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

# --- Tests ---

def test_add_animal(zoo, lion):
    """Test adding an animal to the registry."""
    zoo.add_animal(lion)
    assert "Leo" in zoo.get_animals()
    assert isinstance(zoo.get_animals()["Leo"], Mammal)

def test_add_duplicate_animal(zoo, lion):
    """Test that adding a duplicate animal raises an error."""
    zoo.add_animal(lion)
    with pytest.raises(AssignmentError):
        zoo.add_animal(lion)

def test_assign_animal_to_enclosure_success(zoo, lion, savannah_enclosure):
    """Test successful assignment of animal to compatible enclosure."""
    zoo.add_animal(lion)
    zoo.add_enclosure(savannah_enclosure)
    
    zoo.assign_animal_to_enclosure("Leo", "Savannah Pen")
    
    # Check if animal is inside the enclosure object
    housed = savannah_enclosure.get_housed_animals()
    assert "Leo" in housed

def test_assign_incompatible_species(zoo, penguin, savannah_enclosure):
    """Test assignment fails when species does not match enclosure type."""
    zoo.add_animal(penguin)
    zoo.add_enclosure(savannah_enclosure)
    
    # Penguin (Bird) cannot go into Mammal enclosure
    with pytest.raises(AssignmentError) as excinfo:
        zoo.assign_animal_to_enclosure("Pingu", "Savannah Pen")
    assert "Species mismatch" in str(excinfo.value)

def test_assign_incompatible_environment(zoo):
    """Test assignment fails when environment types do not match."""
    # Create a Mammal that lives in Water (edge case)
    whale = Mammal("Moby", 10, "Plankton", "Aquatic")
    savannah_pen = Enclosure("Dry Pen", 500, "Savannah", 10, Mammal)
    
    zoo.add_animal(whale)
    zoo.add_enclosure(savannah_pen)
    
    with pytest.raises(AssignmentError) as excinfo:
        zoo.assign_animal_to_enclosure("Moby", "Dry Pen")
    assert "Environmental mismatch" in str(excinfo.value)

def test_sick_animal_movement_restriction(zoo, lion, savannah_enclosure):
    """Test that a sick animal cannot be moved."""
    zoo.add_animal(lion)
    zoo.add_enclosure(savannah_enclosure)
    
    # Make the lion sick
    lion.add_health_issue("Flu", "2024-01-01", 5, "Rest")
    
    with pytest.raises(AssignmentError) as excinfo:
        zoo.assign_animal_to_enclosure("Leo", "Savannah Pen")
    assert "under treatment" in str(excinfo.value)

def test_animal_polymorphism():
    """Test that different animals make different sounds."""
    lion = Mammal("Simba", 1, "Meat", "Land")
    bird = Bird("Tweety", 1, "Seeds", "Air")
    
    assert lion.cry() == "ROAR!"
    assert bird.cry() == "CAW! CAW!"

