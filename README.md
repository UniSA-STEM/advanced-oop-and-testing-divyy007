[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_geRERRo)

# Zoo Management System

## Overview
This project is a Python-based **Zoo Management System** designed to digitally manage zoo operations. It replaces manual record-keeping with an Object-Oriented solution that handles animals, enclosures, staff assignments, and health records.

The system enforces strict constraints (e.g., species compatibility, health quarantine) and utilizes advanced OOP principles such as Inheritance, Polymorphism, Composition, and Abstraction.

## Features
*   **Animal Management:** Support for Mammals, Birds, and Reptiles with unique behaviors.
*   **Enclosure Management:** strict validation for species compatibility and environmental needs.
*   **Staff Operations:** Zookeepers for feeding/cleaning and Veterinarians for health management.
*   **Health System:** Detailed health records that influence zoo operations (e.g., sick animals cannot be moved).
*   **Robust Error Handling:** Custom exceptions for invalid assignments or logic errors.
*   **Unit Testing:** Comprehensive test suite using `pytest`.

## Project Structure
The codebase is modularized into separate files for better maintainability:

*   `animal.py`: Contains the abstract `Animal` class, concrete subclasses (`Mammal`, `Bird`, `Reptile`), and the `HealthRecord` class.
*   `enclosure.py`: Manages enclosure logic, cleanliness, and animal housing constraints.
*   `staff.py`: Defines `Staff`, `Zookeeper`, and `Veterinarian` roles and their specific interactions with animals/enclosures.
*   `custom_exceptions.py`: Defines the `AssignmentError` class used for logic validation.
*   `main.py`: A demonstration script that walks through the system's functionality (creating objects, assigning animals, handling errors, and reporting).
*   `test_zoo.py`: A suite of unit tests verifying core logic, constraints, and edge cases.

## Prerequisites
*   **Python 3.x**
*   **Pytest** (for running unit tests)

To install pytest, run:
```bash
pip install pytest