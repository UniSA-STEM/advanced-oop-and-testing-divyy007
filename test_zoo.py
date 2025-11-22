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