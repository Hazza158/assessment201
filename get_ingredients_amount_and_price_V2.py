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


def string_checker(question, num_letters, valid_responses):

    error = "ERROR: INCORRECT RESPONSE"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \n Please try again. \n".format(error))
            continue

        return response


# currency formatting



# Gets expenses, returns list wish has the data frame and sub-total
def get_ingredients(var_fixed):
    # Set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []
    unit_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
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
                print("INCORRECT RESPONSE: Sorry that is the incorrect response.")

    # loop to get component, Amount and price
    item_name = ""

    while item_name.lower() != "xxx":

        print()
        # get name, amount and item

        if item_name.lower() == "xxx":
            break

        quantity = num_check("Quantity:", "The quantity must be a whole number which is more than zero", int)
        price = num_check("How much for a single item? $", "The price must be a number <more than 0>", float)
        unit = string_checker("what is the the measurement unit that you want to use? (g, kg, mL, L):", unit_list)
        # add item, quantity, price, and unit to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
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

print("Variable Costs: ${:.2f}".format(variable_sub))
