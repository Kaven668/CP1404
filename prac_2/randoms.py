import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# The random number between 5 and 20.

# What was the smallest number you could have seen, what was the largest?
# The smallest number is 5 the largest number is 20.


# What did you see on line 2?
# The number between 3 and 10 the step is 2 and exclude 10.

# What was the smallest number you could have seen, what was the largest?
# The smallest number is 3 and the largest number is 9.

# Could line 2 have produced a 4?
# Could not because the step is 2.


# What did you see on line 3?
# Countless float number between 2.5 and 5.5 but don't include 2.5 and 5.5.

# What was the smallest number you could have seen, what was the largest?
# The smallest number is higher than 2.5 and the largest number is lower than 5.5.


# Write code, not a comment, to produce a random number between 1 and 100 inclusive.

print(random.randint(1, 100))
