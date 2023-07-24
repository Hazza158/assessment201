
#functions here


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

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# ***** user input goes here *****

# get recipe name
recipe_name = not_blank("What is the name of your recipe?",
                        "sorry the recipe name cannot be blank")

# get serving size
serve_size = num_check("what is the serving size of your recipe?")
needed_size = num_check("")

