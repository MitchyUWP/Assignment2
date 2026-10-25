"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return annual_cost / (SEMESTERS_PER_YEAR * credits)


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return cost_per_credit(annual_cost, credits) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER


def cost_of_skipped_classes(annual_cost, credits, classes_skipped):
    """Give back the tuition value of skipped CS 1430 class meetings."""
    return cost_per_class(annual_cost, credits) * classes_skipped


# ---- PROGRAM ----

def main():
    print("Welcome! Let's calculate how much those lecture-day naps cost.")

    while True:
        annual_cost_input = input("Enter the total cost for one year: $")

        valid_input = annual_cost_input.count(".") <= 1 and annual_cost_input.replace(".", "", 1).isdigit()

        if not valid_input:
            print("Wrong input. Please enter the dollar amount for college.")
            continue

        annual_cost = float(annual_cost_input)

        if annual_cost > 105000:
            print("For that price, college better come with a dragon.")
        elif annual_cost >= 0:
            break
        else:
            print("Wrong input. Please enter the dollar amount for college.")

    while True:
        credits_input = input("Enter the number of credits this semester: ")
        if credits_input.isdigit():
            credits = int(credits_input)
            if credits >= 1 and credits <= 18:
                break

        print("Wrong input. Please enter a number of credits from 1 to 18.")

    menu_options = (
        "1. Cost per semester",
        "2. Cost per month",
        "3. Cost per class day",
        "4. Cost per credit",
        "5. Cost per CS 1430 class",
        "6. Worth It?",
        "Q. Quit",
    )

    while True:
        print("College Cost Calculator: Wallet Warning Edition")
        for option in menu_options:
            print(option)

        choice = input("Choose an option: ")
        choice = choice.upper()

        if choice == "Q":
            break
        elif choice == "1":
            print(f"Cost per semester: ${cost_per_semester(annual_cost):.2f}")
        elif choice == "2":
            print(f"Cost per month: ${cost_per_month(annual_cost):.2f}")
        elif choice == "3":
            print(f"Cost per class day: ${cost_per_day(annual_cost):.2f}")
        elif choice == "4":
            print(f"Cost per credit: ${cost_per_credit(annual_cost, credits):.2f}")
        elif choice == "5":
            print(f"Cost per CS 1430 class: ${cost_per_class(annual_cost, credits):.2f}")
        elif choice == "6":
            while True:
                classes_skipped_input = input("How many CS 1430 classes did you skip this semester? ")
                if classes_skipped_input.isdigit():
                    classes_skipped = int(classes_skipped_input)
                    if classes_skipped <= CS1430_MEETINGS_PER_SEMESTER:
                        break

                print(f"Wrong input. Please enter a number of classes from 0 to {CS1430_MEETINGS_PER_SEMESTER}.")

            skipped_cost = cost_of_skipped_classes(annual_cost, credits, classes_skipped)
            print(f"Tuition value of skipped CS 1430 classes: ${skipped_cost:.2f}")
        else:
            print("Wrong input. Please choose 1-6 or Q.")

    print("Thanks for stopping by! May the odds be ever in your favor!")
# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
