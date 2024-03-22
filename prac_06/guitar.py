"""
Word Occurrences
Estimate: 30 minutes
Actual:   50 minutes
"""
class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name="",year = 0 , cost = 0 ):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Initialise a guitar instance."""
        return f"{self.name} get_age() - Expected {self.get_age()}. Got {self.get_age()}\n{self.name} is_vintage() - Expected {self.is_vintage()}. Got {self.is_vintage()}"
        # return f"{self.name} ,{self.year} : {self.cost}"


    def get_age(self):
        """ Calculate the age of guitar"""
        current_year = 2024
        return current_year-self.year

    def is_vintage(self):
        "Determine the guitar is vintage or not "
        if self.get_age() >= 50:
            return True
        else:
            return False

