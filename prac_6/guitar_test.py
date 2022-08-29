from guitar import Guitar as Gt


def run_test():
    """Run test for """
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    guitar = Gt(name, year, cost)
    print(guitar)
    another = Gt("Another Guitar", 2013, 1899)
    print(another)
    print(f"{guitar.name} get_age() - Expected {98}. Got {guitar.get_age()}")
    print(f"{another.name} get_age() - Expected {7}. Got {another.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected {False} Got {another.is_vintage()}")


run_test()
