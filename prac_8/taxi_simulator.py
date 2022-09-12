from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program"""
    exist_taxi = None
    print("Let's drive!")
    print(MENU)
    total_cost = 0

    choose = input(">>> ").upper()

    while choose != "Q":
        if choose == "C":
            print("Taxis available:")
            display_taxi(taxis)
            taxi_choose = int(input("Choose taxi: "))
            try:
                exist_taxi = taxis[taxi_choose]
            except IndexError:
                print("Invalid input")

        elif choose == "D":
            if exist_taxi:
                exist_taxi.start_fare()
                drive_distance = int(input("Drive how far?"))
                exist_taxi.drive(drive_distance)
                trip_cost = exist_taxi.get_fare()
                print(f"Your {exist_taxi.name}, trip cost you {trip_cost}")
                total_cost += trip_cost
            else:
                print("You need to choose a taxi before you can drive")

        else:
            print("Invalid input")

        print(f"Bill to date: $ {total_cost}")
        print(MENU)
        choose = input(">>> ").upper()

    print(f"Total trip cost {total_cost}")
    print("Taxi are now:")
    display_taxi(taxis)


def display_taxi(taxis_list):
    """Display list of taxis"""
    for i, taxi in enumerate(taxis_list):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()
