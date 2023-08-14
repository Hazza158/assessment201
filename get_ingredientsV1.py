# functions go here

def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \n Please try again. \n".format(error))
            continue

        return response


def string_checker(question, num_letters, valid_responses):

    error = "ERROR: INCORRECT RESPONSE"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# checks users enter an integer t oa given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response


        except ValueError:
            print("please enter an integer")


# currency formatting
def currency(x):
    return f"${x:.2f}"
    # return "${:.2f}".format(x)


# main routine goes here
ingredients_given = 0

while True:

    ingredient_name = input("enter your ingredient / or xxx to quit: ")

    if ingredient_name == "xxx":
        break

    amount = num_check("Amount of the ingredient: ")

    if 1 <= amount <= 100:
        pass
    elif amount < 12:
        print("")
        continue
    else:
        print("")
        continue

    ingredients_given += 1

print(" you have put in {} ingredients".format(ingredients_given))
