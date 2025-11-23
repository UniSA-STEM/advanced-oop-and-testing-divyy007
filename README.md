# Zoo Management System

## 👋 Overview
Welcome to the **Zoo Management System**! This project was built to help modernize a local zoo that was previously running entirely on pen and paper. 

It is a Python-based application that uses Object-Oriented Programming (OOP) to manage the day-to-day chaos of running a zoo. It handles everything from tracking animals and their health to managing staff roles and ensuring animals are placed in the correct habitats.

## 🚀 Features
*   **Animal Tracking:** We can register Mammals, Birds, and Reptiles, each with their own specific behaviors (like unique sounds and diets).
*   **Smart Enclosures:** The system prevents mistakes, like putting a penguin in a desert or mixing incompatible species. It also tracks cleanliness levels.
*   **Staff Roles:** Distinct roles for **Zookeepers** (who feed and clean) and **Veterinarians** (who check health).
*   **Health & Safety:** Animals have detailed medical records. The system enforces safety rules—for example, a sick animal cannot be moved to a public enclosure until they recover.
*   **Error Handling:** The system gracefully handles invalid inputs (like bad IDs or wrong data types) without crashing.

## 📂 Project Structure
Here is a quick look at how the code is organized:

*   **`animal.py`**
    *   Contains the base `Animal` class and specific species (`Mammal`, `Bird`, `Reptile`).
    *   Also includes the `HealthRecord` class to track medical history.
*   **`enclosure.py`**
    *   Manages the habitats. This file handles the logic for checking if an animal is allowed inside based on species and environment.
*   **`staff.py`**
    *   Defines the `Staff` base class and the specialized `Zookeeper` and `Veterinarian` classes.
*   **`main.py`**
    *   **The Brain:** Contains the `ZooManager` class which acts as the central controller.
    *   **The Demo:** Runs a full walkthrough script showing the system in action (creating animals, moving them, handling emergencies, and printing reports).
*   **`test_zoo.py`**
    *   A suite of automated tests using `pytest` to ensure the logic is solid and bugs are caught early.

## ⚙️ Getting Started

### Prerequisites
You will need **Python 3.x** installed.

To run the tests, you need `pytest`:
```bash
pip install pytest
```

### How to Run
**1. Run the Simulation:**
To see the zoo in action, simply run the main file. This will execute a demonstration script.
```bash
python main.py
```

**2. Run the Tests:**
To verify that all logic and constraints are working correctly:
```bash
pytest 
# Or Run 
python -m pytest 
# For verbose
python -m pytest -v
```