import pandas

#functions go here

def unit_checker(question):
    while True:
        response = input(question).lower()

        if response == "grams" or response == "g":
            return "grams"
        elif response == "kilograms" or response == "kg":
            return "kilograms"
        elif response == "millilitres" or response == "mL":
            return "millilitres"
        elif response == "litres" or response == "L":
            return "litres"
        elif response == "xxx":
            return "Next Question"
        else:
            print("INCORRECT RESPONSE: Please correct your response in order to proceed.")
