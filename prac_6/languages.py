from programming_language import ProgrammingLanguage as Pl


def main():
    """Check language is dynamic"""
    ruby = Pl("Ruby", "Dynamic", True, 1995)
    python = Pl("Python", "Dynamic", True, 1991)
    visual_basic = Pl("Visual Basic", "Static", False, 1991)
    languages = [ruby, python, visual_basic]
    print("The dynamic language are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
