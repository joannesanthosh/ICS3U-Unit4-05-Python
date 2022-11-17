# Created by: Joanne Santhosh
# Created on: Nov 15
# This program uses a continue statement


def main():
    # this function uses a continue statement
    try:
        positive_integer = int(input("Enter how many number you want to add: "))
        result = 0
        for loop_counter in range(0, positive_integer):
            number = float(input("Enter a number to add:"))
            if number < 0:
                continue
            result = result + number
        print("\nThe sum of the numbers is {}.".format(result))
    except Exception:
        print("\n This is an invalid input. Please try again")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
