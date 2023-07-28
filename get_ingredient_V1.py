

def get_ingredients():
    get_recipe = []

    stop = ""

    print("enter ingredients one at a time, enter <xxx> to finish")

    while stop != "xxx":
        # get ingredient
        get_ingredient = not_blank("what is your ingredient (enter <xxx> to end): ")

        # stop looping if <xxx> is entered and there are 3 or more ingredients entered
        if get_ingredient == "xxx" and len(ingredient_name) > 2:
            break

        elif get_ingredient == "xxx" and len(ingredient_name) <3:
            print("Sorry you need at least 3 ingredients to proceed.")

        else:
            get_recipe.append(get_ingredient)