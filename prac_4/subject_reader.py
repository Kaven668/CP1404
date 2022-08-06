"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_subjcet()
    print(subjects)
    display_subject(subjects)


def display_subject(subjects):
    total_students = 0
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")
        total_students += subject[2]
    print("Total students:",total_students)


def load_subjcet():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject =[]
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject.append(parts)
    input_file.close()
    return subject



main()