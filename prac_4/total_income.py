"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

incomes = []


def main():
    """Display income report for incomes over a given mounth_number of months."""
    months = int(input("How many months? "))
    for mounth_number in range(1, months + 1):
        income = float(input("Enter income for mounth_number {}:".format(str(mounth_number))))
        incomes.append(income)
    get_total_incomes(incomes)


def get_total_incomes(income):
    total = 0
    print("\nIncome Report\n-------------")
    for mounth, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(mounth + 1, income, total))


main()
