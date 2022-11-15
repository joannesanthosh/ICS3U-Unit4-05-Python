# Created by: Joanne Santhosh
# Created on: Nov 15
# This program uses a continue statement


def main():
    # this function uses a continue statement

    # input
    positive_integer = int(input("Enter a positive number: "))
    print("")

    # process & output
    while positive_integer > 0:
        # yes, this is the exception on placing the counter at the top
        positive_integer = positive_integer - 1

        if positive_integer > 0:
            continue
        print("The sum is : {}".format(positive_integer))

    print("/nDone.")


if __name__ == "__main__":
    main()
