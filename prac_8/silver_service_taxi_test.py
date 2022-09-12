from silver_service_taxi import SilverServiceTaxi


def main():
    benz = SilverServiceTaxi("Benz", 100, 4)
    print(benz)

    benz.drive(100)
    print(benz)

    print(benz.get_fare())
    benz.add_fuel(100)
    print(benz)
    benz.drive(89)
    print(benz)
    print(benz.get_fare())
    print(benz.get_fare())


if __name__ == '__main__':
    main()