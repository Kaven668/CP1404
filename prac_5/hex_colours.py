
COLOR_DICT = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff", "Alizarin crimson": "e32636",
              "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7",
              "Aqua": "#00ffff", "Aureolin": "fdee00"}


def main():
    """Choose color program"""
    color_name = input("Enter a color name:").title()
    while color_name != "":
        print("{} is {}".format(color_name, COLOR_DICT.get(color_name)))
        color_name = input("Enter a color name:").title()


main()
