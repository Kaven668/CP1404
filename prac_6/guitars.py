from guitar import Guitar as Gt


def main():
    """My guitar program"""
    guitars = []
    print("My guitars!")
    name = input("Name:")
    while name != "":
        year = int(input("Year:"))
        cost = float(input("Cost:"))
        add_guitar = Gt(name, year, cost)
        guitars.append(add_guitar)
        print(add_guitar)
        name = input("Name:")

    guitars.append(Gt("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Gt("Line 6 JTV-59", 2010, 1512.9))

    print("... snip ...")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_str = ""
        if guitar.is_vintage():
            vintage_str = "(vintage)"
        print("Guitar {0}: {1.name} ({1.year}), worth ${1.cost:.2f}{2}".format(i + 1, guitar, vintage_str))


main()
