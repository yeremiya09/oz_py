# animals/birds.py

class Eagle:
    def __init__(self, name: str, wingspan: float):
        self.name = name
        self.wingspan = wingspan

    def __str__(self):
        return f"Eagle(name={self.name}, wingspan={self.wingspan} meters)"
