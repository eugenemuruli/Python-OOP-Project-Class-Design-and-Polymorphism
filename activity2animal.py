# animals.py
from typing import List


class Animal:
    """Base class for animals. Defines move() method to be overridden."""
    
    def move(self) -> None:
        raise NotImplementedError("Subclasses must implement move()")


class Dog(Animal):
    def move(self) -> None:
        print("🐶 The dog is running on four legs.")


class Snake(Animal):
    def move(self) -> None:
        print("🐍 The snake is slithering silently.")


class Bird(Animal):
    def move(self) -> None:
        print("🐦 The bird is flying through the sky.")


class Fish(Animal):
    def move(self) -> None:
        print("🐠 The fish is swimming gracefully.")


def demonstrate_animal_movement(animals: List[Animal]) -> None:
    """Calls move() on any list of animals — demonstrates polymorphism."""
    print("=== Animal Movement Simulation ===")
    for animal in animals:
        animal.move()
    print("==================================")