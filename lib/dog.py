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
        self._name = None
        self._breed = None
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not self._is_valid_name(value):
            self._name = None
        else:
            self._name = value

    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, value):
        if not self._is_valid_breed(value):
            self._breed = None
        else:
            self._breed = value

    def _is_valid_name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            return False
        return True

    def _is_valid_breed(self, breed):
        if breed is not None and breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            return False
        return True

    def __str__(self):
        if self.name is None or self.breed is None:
            return "Invalid Dog object."
        return f"{self.name} is a {self.breed}."
