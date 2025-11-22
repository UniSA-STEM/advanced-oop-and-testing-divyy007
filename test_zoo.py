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