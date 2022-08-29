class ProgrammingLanguage:
    """Creat a class about ProgrammingLanguage """
    def __init__(self, name, typing, reflection, year):
        """Construct the ProgrammingLanguage for each values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string fo ProgrammingLanguage"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine the language is Dynamic or not"""
        return self.typing == "Dynamic"


def run_test():
    """Run test program"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    print(python)
    print(visual_basic)


if __name__ == "__main__":
    run_test()
