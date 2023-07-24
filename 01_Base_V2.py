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
            print("Sorry you need atleast 3 ingredients to proceed.")

        else:
            get_recipe.append(get_ingredient)


# main routine goes here
want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    print('''\n
    instructions go here
    \n
    ''')








