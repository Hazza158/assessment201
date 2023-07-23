
# functions go here
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \n Please try again. \n".format(error))
            continue

        return response


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

        elif
