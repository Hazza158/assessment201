import pandas

# ... (Previous code) ...

# main routine

# ... (Previous code) ...

# Create the "Total Cost" key in the recipe_dict
recipe_dict["*Total Cost*"] = []

while True:

    # ... (Previous code) ...

    unit_cost = (ingredient_price / bought_amount * needed_amount)

    # Add the unit_cost to the recipe_dict
    recipe_dict["*Total Cost*"].append(unit_cost)

    # ... (Previous code) ...

# panda the goods
recipe_panda = pandas.DataFrame(recipe_dict)

# Calculate the total cost and cost per serving
recipe_panda["Total Cost"] = recipe_panda["*Total Cost*"].sum()
total_cost = recipe_panda["Total Cost"].sum()
serving_cost = total_cost / needed_size

# Print the recipe DataFrame and cost information
print(recipe_panda)
print("Total Cost: $", total_cost)
print("Cost per Serving: $", serving_cost)
