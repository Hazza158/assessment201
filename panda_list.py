import pandas

ingredient_name = []
total_ingredient_price = []
total_needed_amount = []
total_bought_amount = []
total_production_cost = []

recipe_dict = {
    "*Ingredients*": ingredient_name,
    "*Ingredient Price*": total_ingredient_price,
    "*Needed Amount*": total_needed_amount,
    "*Bought Amount*": total_bought_amount,
    "*Production Cost*": total_production_cost
}

needed_amount = ""
bought_amount = ""
ingredient_price = ""
unit_cost = ""

get_ingredient = "what is your ingredient"

# list list list list
ingredient_name.append(get_ingredient)
total_ingredient_price.append(ingredient_price)
total_needed_amount.append(needed_amount)
total_bought_amount.append(bought_amount)
total_production_cost.append(unit_cost)

# panda the goods
recipe_panda = pandas.DataFrame(recipe_dict)