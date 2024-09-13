# animals/mammals.py

class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"Dog(name={self.name}, breed={self.breed})"
