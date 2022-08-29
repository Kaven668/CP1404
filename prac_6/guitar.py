VINTAGE_AGE = 50
YEAR = 2020


class Guitar:
    """Create a class about Guitar"""

    def __init__(self, name="", year=0, cost=0):
        """Construct the Guitar for each values"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string of Guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Get the age of guitar"""
        return YEAR - self.year

    def is_vintage(self):
        """Determine the guitar vintage or not """
        return self.get_age() >= VINTAGE_AGE


if __name__ == "__main__":
    guitar = Guitar()
    print(guitar)
