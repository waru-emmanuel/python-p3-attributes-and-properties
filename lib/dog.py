APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="", breed=None):
        self.name = name  # Using the property setter for name
        self.breed = breed  # Using the property setter for breed

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
            self._name = None
        else:
            self._name = value

    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, value):
        if value is not None and value not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            self._breed = None
        else:
            self._breed = value

    def __str__(self):
        if self.name is None or self.breed is None:
            return "Invalid Dog object."
        return f"{self.name} is a {self.breed}."
