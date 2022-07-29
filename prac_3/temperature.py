MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)


def main():
    '''Temperature convert program'''
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = caculate_celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit:"))
            celsius = caculate_fahrenheit_to_celsuies(fahrenheit)
            print(f'Resule:{celsius:.2f} C')
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def caculate_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit"""
    faulthandler = celsius * 9.0 / 5 + 32
    return faulthandler


def caculate_fahrenheit_to_celsuies(fahrenheit):
    '''Convert fahrenheit to celsuies'''
    celsuies = 5 / 9 * (fahrenheit - 32)
    return celsuies


main()
