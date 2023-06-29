
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


def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \n Please try again. \n".format(error))
            continue

        return response


# currency formatting
def currency(x):
    return f"${x:.2f}"


def instructions():
    print("**** How to Use the Recipe Cost Calculator ****")
    print()
    print("Instructions go here")
    print()
    return ""

# main routine goes here
want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    print('''\n
    instructions go here
    ''')

item_list = []
amount_list = []
price_list = []


variable_dictionary = {
    "Item": item_list,
    "Amount": amount_list,
    "Price": price_list,
}



