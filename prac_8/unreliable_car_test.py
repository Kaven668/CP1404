from unreliable_car import UnreliableCar


def main():
    benz = UnreliableCar("benz", 100, 65)
    print(benz)
    benz.drive(89)
    print(benz)


if __name__ == '__main__':
    main()
