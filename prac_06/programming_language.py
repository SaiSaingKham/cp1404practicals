class ProgrammingLanguage:
    """Represent information about programming language."""

    def __init__(self, name, typing, reflection, year):
        """Create a ProgrammingLanguage object using the provided values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of a ProgrammingLanguage"""
        return f"{self.name}, {self.typing}, Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check whether the language possesses dynamic typing."""
        return self.typing == "Dynamic"


def run_tests():
    """Run tests on ProgrammingLanguage."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
