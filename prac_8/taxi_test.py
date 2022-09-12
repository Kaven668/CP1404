from taxi import Taxi


def main():
    taxi = Taxi("Prius 1", 100)

    actual_distance_driven = taxi.drive(40)

    print(f"Taxi for drive{actual_distance_driven}")

    print(taxi)
    print(f"Current fare ${taxi.get_fare():.2f}")

    taxi.start_fare()
    actual_distance_driven = taxi.drive(100)
    print(f"Tried driving 100km, but taxi drove for {actual_distance_driven} km.")

    print(taxi)
    print(f"Current fare :$ {taxi.get_fare():.2f}")


if __name__ == '__main__':
    main()
