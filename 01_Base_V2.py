import pandas


# functions go here

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


# main routine goes here
want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    print('''\n
    ***** com To The Recipe Cost Calculator *****
    
    You will use this calculator by inputting:
    * The name of the recipe
    * How many people you are serving
    * Your ingredients
    * How much of the ingredient is needed
    * How much of the ingredient you have already bought
    * How much you have paid for the ingredients
    
    When you have finished inputting your ingredients (minimum of 3),
    you can then finish the program and it will print your recipe costs
    in a readable table/format.
    
    ***** Have Fun !! ***** 
    \n
    ''')

# main routine

ingredient_name = []
total_ingredient_price = []
total_needed_amount = []
total_bought_amount = []
total_production_cost = []

recipe_dict = {
    "*Ingredients*": ingredient_name,
    "*Ingredient Price*": total_ingredient_price,
    "*Needed Amount*": total_needed_amount,
    "*Bought Amount*": total_bought_amount,
    "*Production Cost*": total_production_cost
}

# ***** user input goes here *****
# get recipe name
recipe_name = not_blank("What is the name of your recipe?",
                        "sorry the recipe name cannot be blank")
print()
# get serving size
needed_size = num_check("how many people are you serving?", "sorry this cant be more than zero", int)
print()

needed_amount = ""
bought_amount = ""
ingredient_price = ""
unit_cost = ""

while True:

    print("enter ingredients one at a time, enter <xxx> to finish")

    # get ingredient
    get_ingredient = not_blank("what is your ingredient (enter <xxx> to end): ", "please enter a valid response")
    print()
    # stop looping if <xxx> is entered and there are 3 or more ingredients entered
    if get_ingredient == "xxx" and len(ingredient_name) > 1:
        break

    elif get_ingredient == "xxx" and len(ingredient_name) < 1:
        print("Sorry you need at least 3 ingredients to proceed.")

    needed_amount = num_check("How much of the ingredient do you need? (grams): ", "please enter a number", float)
    print()
    bought_amount = num_check("How much have you bought? (grams): ", "please enter a number", float)
    print()
    ingredient_price = num_check("How much did you pay for the ingredient?: $", "please enter a number", float)
    print()
    unit_cost = (ingredient_price / bought_amount * needed_amount)

    # list list list list
    ingredient_name.append(get_ingredient)
    total_ingredient_price.append(ingredient_price)
    total_needed_amount.append(needed_amount)
    total_bought_amount.append(bought_amount)
    total_production_cost.append(unit_cost)

# panda the goods
recipe_panda = pandas.DataFrame(recipe_dict)

# cost of each serving and total cost
total_cost = recipe_panda["*Production Cost*"].sum()
serving_cost = total_cost / needed_size
print(recipe_panda)
print("Total Cost: ${:.2f}".format(total_cost))
print("Cost per Serving: ${:.2f}".format(serving_cost))
