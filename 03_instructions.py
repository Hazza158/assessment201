
# functions
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "Y":
            response = "yes"
            return response

        elif response == "no" or response == "N":
            response = "no"
            return response

        else:
            print("please answer yes / no")


want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    print('''\n
    ***** Welcome To The Recipe Cost Calculator *****

    You will use this calculator by inputting:
    * The name of the recipe
    * How many people you are serving
    * Your ingredients
    * How much of the ingredient is needed
    * How much of the ingredient you have already bought
    * How much you have paid for the ingredients

    When you have finished inputting your ingredients (minimum of 3),
    you can then finish the program and it will print your recipe costs
    in a readable table/format.

    ***** Have Fun !! ***** 
    \n
    ''')


