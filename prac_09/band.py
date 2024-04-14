class Band:
    """Band Class"""
    def __init__(self, name):
        """Initalise a band based on name and musicians"""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band"""
        self.musicians.append(musician)

    def play(self):
        """Print the musician and instruments name"""
        for musician in self.musicians:
            if musician.instruments:
                for instrument in musician.instruments:
                    print(f"{musician.name} is playing: {instrument}")
            else:
                print(f"{musician.name} needs an instrument!")

    def __str__(self):
        """Return a string """
        return f"{self.name} ({len(self.musicians)} members)"
