import pandas


# functions go here
# makes sure that when the user inputs a number it is not less than zero
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


# allows the user to only input variations of "yes" and "no" in response to a question
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


# makes sure the user cannot input a blank answer in response to a question
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \n Please try again. \n".format(error))
            continue

        return response


# main routine goes here
# asks user if they want to see the instructions
want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    print('''\n
    ***** Welcome To The Recipe Cost Calculator *****
    
    You will use this calculator by inputting:
    * The name of the recipe
    * How many people you are serving
    * Your ingredients
    * How much of the ingredient is needed (this is in grams)
    * How much of the ingredient you have already bought (this is in grams)
    * How much you have paid for the ingredients
    
    When you have finished inputting your ingredients (minimum of 3 ingredients),
    you can then input <xxx> to finish the program and it will print your recipe costs
    in a readable table/format.
    
    ***** Have Fun !! ***** 
    \n
    ''')

# main routine here

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
# asks user what the name of their recipe is and makes sure it cannot be blank
recipe_name = not_blank("What is the name of your recipe?",
                        "sorry the recipe name cannot be blank")
print()
# asks user for the amount of people they are serving for and makes sure the answer is more than zero
needed_size = num_check("how many people are you serving?", "sorry this must be more than zero", int)
print()

needed_amount = ""
bought_amount = ""
ingredient_price = ""
unit_cost = ""

while True:

    print("enter ingredients one at a time, enter <xxx> to finish")

    # asks user what their ingredient is
    get_ingredient = not_blank("what is your ingredient (enter <xxx> to end): ", "sorry this cannot be blank")
    print()
    # stop looping if <xxx> is entered and there are 3 or more ingredients entered
    if get_ingredient == "xxx" and len(ingredient_name) > 1:
        break

    elif get_ingredient == "xxx" and len(ingredient_name) < 3:
        print("Sorry you need at least 3 ingredients to proceed.")

    # asks user how much of the ingredient they need,
    # how much of the ingredient they have bought,
    # and how much they paid for the ingredient
    needed_amount = num_check("How much of the ingredient do you need? (in grams): ", "please enter a number more than zero", float)
    print()
    bought_amount = num_check("How much have you bought? (in grams): ", "please enter a number more than zero", float)
    print()
    ingredient_price = num_check("How much did you pay for the ingredient?: $", "please enter a number more than zero", float)
    print()
    unit_cost = (ingredient_price / bought_amount * needed_amount)

    # list
    ingredient_name.append(get_ingredient)
    total_ingredient_price.append(ingredient_price)
    total_needed_amount.append(needed_amount)
    total_bought_amount.append(bought_amount)
    total_production_cost.append(unit_cost)

# panda the goods
recipe_panda = pandas.DataFrame(recipe_dict)

# calculate the cost of each serving and total cost
# and then print the total cost and cost per serving to 2dp
total_cost = recipe_panda["*Production Cost*"].sum()
serving_cost = total_cost / needed_size
print(recipe_panda)
print("Total Cost: ${:.2f}".format(total_cost))
print("Cost per Serving: ${:.2f}".format(serving_cost))
