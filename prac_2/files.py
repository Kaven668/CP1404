#  Program 1
in_file = open("name.txt", "w")
name = input("Inpute name:")
print(name, file=in_file)
in_file.close()

# Program 2
in_file = open("name.txt", "r")
first_line_str = in_file.readline()
print(f"Your name is {first_line_str}")
in_file.close()

# Program 3

num_file = open("number.txt", "r")

file_1 = num_file.readline()
file_2 = num_file.readline()
total = int(file_1) + int(file_2)
print(total)

# Program 4

in_file_1 = open("number.txt", "r")
total = 0
for line in in_file_1:
    number = int(line)
    total += number
in_file_1.close()
print(total)
