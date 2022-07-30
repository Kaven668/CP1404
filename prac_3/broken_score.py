"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    """Get score and display the result"""
    score = float(input("Enter score: "))
    print(determine_grades(score))


def determine_grades(score):
    """Determine the resulte of the grades"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif 50 < score < 90:
        return "Passable"
    elif score > 90:
        return "Excellent"
    else:
        return "Bad"


main()
