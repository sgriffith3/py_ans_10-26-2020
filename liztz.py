# my_grocery_list
#   - milk
#   - eggs
#   - bread


groceries = ["milk", 'eggs', "bread"]
#              0       1        2

sourdough = groceries.index('bread')
print(sourdough)

print(groceries)
print(type(groceries))

print("I want to eat some " + "eggs")

print("I want to eat some " + str(groceries) + ".")

print("I want to eat some " + groceries[1])

print("I want to eat some " + groceries[2])

print("I want to eat some " + groceries[sourdough])

# f-string
print(f"I want to eat some {groceries}.")



