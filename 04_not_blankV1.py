def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("that is blank, please try again".format(error))
            continue

        return response

testing = not_blank("what is your ingredient?", "this is blank, please try again")
