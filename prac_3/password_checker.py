def main():
    """Change password to asterisk program"""
    pwd = get_password()
    length_asterisks = show_asterisk(pwd)
    print(length_asterisks)
    # print(len(length_asterisks))


def get_password():
    """Get the valid password"""
    pwd = input("Enter password:")
    while len(pwd) < 2 or len(pwd) > 20:
        print("Invalid")
        pwd = input("Enter password:")
    return pwd


def show_asterisk(pwd):
    """Change password to asterisk"""
    length = len(pwd) * "*"
    return length


main()
