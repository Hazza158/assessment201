# functions go here

def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \n Please try again. \n".format(error))
            continue

        return response


# checks users enter an integer t oa given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response


        except ValueError:
            print("please enter an integer")


# main routine goes here
ingredients_given = 0

while True:

    name = input("enter your name / xxx to quit: ")

    if name == "xxx":
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("sorry you are too young for this movie")
        continue
    else:
        print("?? that looks like a typo, please try again.")
        continue

    ingredients_given += 1

print(" you have put in {} ingredients".format(ingredients_given))
