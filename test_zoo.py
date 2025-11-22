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
