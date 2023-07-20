import pandas


#functions go here


def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


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


# Gets expenses, returns list wish has the data frame and sub-total
def get_ingredients(var_fixed):
    # Set up dictionaries and lists

    item_list = []
    amount_list = []
    price_list = []
    unit_list = []

    variable_dict = {
        "Item": item_list,
        "Amount": amount_list,
        "Price": price_list,
        "Unit": unit_list

    }

    def unit_checker(question):

        while True:
            response = input(question).lower()

            if response == "grams" or response == "g":
                return "grams"
            elif response == "kilograms" or response == "kg":
                return "kilograms"
            elif response == "millilitres" or response == "mL":
                return "millilitres"
            elif response == "litres" or response == "L":
                return "litres"
            elif response == "xxx":
                return "Next Question"
            else:
                print("INCORRECT RESPONSE: Please correct your response in order to proceed.")

    # loop to get component, Amount and price
    item_name = ""

    while item_name.lower() != "xxx":

        print()
        # get name, amount and item

        if item_name.lower() == "xxx":
            break

        amount = num_check("Amount:", "The amount must be a whole number which is more than zero", int)
        price = num_check("How much for a single item? $", "The price must be a number <more than 0>", float)
        unit = unit_checker("Please enter the measurement unit (g, kg, mL, L):", "Incorrect response", float)
        # add item, quantity, price, and unit to lists
        item_list.append(item_name)
        amount_list.append(amount)
        price_list.append(price)
        unit_list.append(unit)

        expense_frame = pandas.DataFrame(variable_dict)
        expense_frame = expense_frame.set_index('Item')

        expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['Price'] + unit_frame['Unit']
        # Find sub-total
        expense_sub = expense_frame['Cost'].sum()

        add_dollars = ['Price', 'Cost']
        for item in add_dollars:
            expense_frame[item] = expense_frame[item].apply(currency)

        return [expense_frame, expense_sub, unit_frame]


# main routine goes here
want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    print('''\n
    instructions go here
    \n
    ''')

# **** Main routine begins ****

# Get Recipe name
recipe_name = not_blank("Recipe name: ", "The recipe name can't be blank.")
ingredient_name = not_blank("Ingredient name: ", "Please choose an ingredient or type <xxx>.")

variable_ingredients = get_ingredients("variable")
variable_frame = variable_ingredients[0]
variable_sub = variable_ingredients[1]
unit_frame = variable_ingredients[2]

# **** Printing Area ****

print()
print(variable_frame)
print()

print("Variable Costs: ${:.2f}".format(variable_sub, unit_frame))





