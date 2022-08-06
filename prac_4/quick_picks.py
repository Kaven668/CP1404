import random
MINNUM = 1
MAXNUM = 46
PER_PICK = 6

def main():
    """Quick pick program"""
    pick_number = check_valid_number()
    for i in range(pick_number):
        quick_pick = []
        for x in range(PER_PICK):
            number = random.randint(MINNUM,MAXNUM)
            while number in quick_pick:
                number = random.randint(MINNUM,MAXNUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number}" for number in quick_pick ))

def check_valid_number():
    """Check the valid input"""
    pick_numbers = input("How many numbers you want pick?")
    is_valid_number = False
    while not is_valid_number:
        try:
            pick_numbers = int(pick_numbers)
            if pick_numbers <= 0:
                pick_numbers = input("How many numbers you want pick?")
            else:
                is_valid_number = True
                return pick_numbers
        except ValueError:
            pick_numbers = input("How many numbers you want pick?")
    return pick_numbers



main()
