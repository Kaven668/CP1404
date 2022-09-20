def main():
    filenames = ["Away In A Manger.txt",
                 "SilentNight.txt",
                 "O little town of bethlehem.TXT",
                 "ItIsWell (oh my soul).txt",
                 "The_lord_is_King.jpg",
                 "file no extension"]

    for filename in filenames:
        fixed_filename = get_fix_filename(filename)
        print(fixed_filename)


def get_fix_filename(filename_extension):
    data = filename_extension.split(".")
    filename = data[0]
    length_of_name = len(filename)
    index = 1
    while index < length_of_name:
        current_character = filename[index]
        precious_character = filename[index - 1]
        if current_character.isupper() and precious_character.isaplha():
            filename = filename[:index] + " " + filename[index:]
            length_of_name = len(filename)
            index += 1
        index += 1
    if len(data) == 2:
        filename = filename.strip().title() + "." + data[1].lower()
    return filename.replace(" ", "_")


if __name__ == '__main__':
    main()
