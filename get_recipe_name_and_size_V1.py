# functions here
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \n Please try again. \n".format(error))
            continue

        return response


def num_check(question, error, num_type):
    valid = False
    while not valid:

        error = "please enter a number that is more than zero"

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def get_ingredients():
    get_recipe = []

    stop = ""

    print("enter ingredients one at a time, enter <xxx> to finish")

    while stop != "xxx":
        # get ingredient
        get_ingredient = not_blank("what is your ingredient (enter <xxx> to end): ")

        # stop looping if <xxx> is entered and there are 3 or more ingredients entered
        if get_ingredient == "xxx" and len(get_recipe) > 2:
            break

        elif get_ingredient == "xxx" and len(get_recipe) <3:
            print("Sorry you need at least 3 ingredients to proceed.")

        else:
            get_recipe.append(get_ingredient)


# ***** user input goes here *****

# get recipe name
recipe_name = not_blank("What is the name of your recipe?",
                        "sorry the recipe name cannot be blank")

# get serving size
serve_size = num_check("what is the serving size of your recipe?", "sorry this cant be blank")
needed_size = num_check("how many people are you serving for?", "sorry this cant be more than zero", int)
print()





