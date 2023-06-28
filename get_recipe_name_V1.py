
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \n Please try again. \n".format(error))
            continue

        return response

def get_recipe_name():
    recipe_name = []

    break = ""
    print("what is the name of the recipe you want to make?. "
          "use 'xxx' when you are done")
    print()
    while break != "xxx":
