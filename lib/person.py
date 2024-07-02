APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="", job=""):
        self.name = name  # Using the property setter for name
        self.job = job    # Using the property setter for job

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
            self._name = None
        else:
            self._name = value.title()

    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, value):
        if value not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            self._job = None
        else:
            self._job = value

    def __str__(self):
        if self.name is None or self.job is None:
            return "Invalid Person object."
        return f"{self.name} is a {self.job}."
