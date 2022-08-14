def main():
    """Email to name program"""
    email_to_name = {}
    email = input("Email:")
    while email != "":
        name = get_name(email)
        confirm = input(f"Is your name {name}?(Y/n)").upper()
        if confirm != "Y" and confirm != "":
            name = input("Name?")
        email_to_name[name] = name
        email = input("Email:")

    for email, name in email_to_name.items():
        print(f"{name} is ({email})")


def get_name(email):
    """Find the name out"""
    text = email.split("@")[0]
    part = text.split(".")
    name = " ".join(part).title()
    return name


main()
