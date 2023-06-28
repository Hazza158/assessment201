def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")


def instructions():
    print("**** How to Use the Recipe Cost Calculator ****")
    print()
    print("Instructions go here")
    print()

    return ""


used_before = yes_no("have you used the calculator before?")

if used_before == "no":
    instructions()

print()